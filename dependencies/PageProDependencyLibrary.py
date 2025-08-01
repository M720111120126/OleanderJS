import dependencies.ArkOfObject as ark
import dependencies.ArkOfObjectPro as ArkPRO
import os
from dependencies.ReusableFunctions import  *
from dependencies.ObjectArkOfPython import UIComponent, loading_page, compilation
from dependencies.OleanderJsInformation import OleanderJS_project_path

def PageProCompilation(fapi_version: str, page) -> None:
    if fapi_version == "ArkPRO":
        page_init = compilation(ArkPRO.ArkPRO(loading_page(page, "init.yh"), "ArkPRO", get_all_subclasses(UIComponent)))
    elif fapi_version == "ark":
        page_init = compilation(ark.ark(loading_page(page, "init.yh"), "ark"))
    elif fapi_version == "object":
        page_init = compilation(loading_page(page, "init.yh"))
    else:
        page_init = compilation(ArkPRO.ArkPRO(loading_page(page, "init.yh"), "into", get_all_subclasses(UIComponent)))
    build_path = os.path.join(OleanderJS_project_path, "build")
    if not os.path.exists(build_path):
        os.makedirs(build_path)
    with open(os.path.join(OleanderJS_project_path, "build", f"{page['name']}.html"), "w", encoding="utf-8") as file:
        file.write(page_init)