import ArkOfObject as ark
import os

def PageProCompilation(loading_page, fapi_version, page, compilation, OleanderJS_project_path):
    if fapi_version == "ark":
        page_init = compilation(ark.ark(loading_page(page, "init.yh"), "ark"))
    elif fapi_version == "object":
        page_init = compilation(loading_page(page, "init.yh"))
    else:
        page_init = compilation(ark.ark(loading_page(page, "init.yh"), "into"))
    build_path = os.path.join(OleanderJS_project_path, "build")
    if not os.path.exists(build_path):
        os.makedirs(build_path)
    with open(os.path.join(OleanderJS_project_path, "build", f"{page["name"]}.html"), "w", encoding="utf-8") as file:
        file.write(page_init)