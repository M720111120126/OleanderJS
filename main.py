import os, sys
import ArkOfObjectPro as ArkPRO
import ArkOfObject as ark
from PageProDependencyLibrary import PageProCompilation
from ReusableFunctions import  *
from VersionManager import VersionManager
from OleanderJsInformation import OleanderJS_project_path, OleanderJS_api_path, app_json5, args, OleanderJS_json5, build_json5
from ObjectArkOfPython import UIComponent, loading_page, compilation

# 检查环境
if args["fapi_version"]:
    fapi_version = args["fapi_version"]
else:
    fapi_version = ""
if args["version"]:
    print(OleanderJS_json5["API-version"])
if not args["skip_env_check"]:
    if args["verbose"]:
        print("The environment is being inspected")
    OleanderJS_json5 = VersionManager()
    if compare_versions(OleanderJS_json5["API-version"], build_json5["Minimum-required-API-version"]) == 2:
        sys.exit("""最低兼容的API版本高于当前API
The minimum compatible API version is higher than the current API""")
    elif compare_versions(OleanderJS_json5["API-version"], build_json5["Target-API-version"]) == 2:
        print("""警告：当前API低于目标的API版本（可能能够正常运行）
Warning: The current API is lower than the target API version (may be able to run normally)""")
    elif compare_versions(OleanderJS_json5["API-version"], build_json5["Target-API-version"]) == 11:
        print("""警告：当前API高于目标的API版本（可能能够正常运行）
Warning: The current API is higher than the target API version (may be able to run normally)""")

# 编译
page_init = ""
for page in app_json5["page"]:
    if args["verbose"]:
        print(f'Reading page:"{page}"')
    if page["name"] == "init":
        if fapi_version == "ArkPRO":
            page_init = compilation(ArkPRO.ArkPRO(loading_page(page, "init.yh"), "ArkPRO", get_all_subclasses(UIComponent)))
        elif fapi_version == "ark":
            page_init = compilation(ark.ark(loading_page(page, "init.yh"), "ark"))
        elif fapi_version == "object":
            page_init = compilation(loading_page(page, "init.yh"))
        else:
            page_init = compilation(ArkPRO.ArkPRO(loading_page(page, "init.yh"), "into", get_all_subclasses(UIComponent)))
    else:
        PageProCompilation(fapi_version, page)
build_dir = os.path.join(OleanderJS_project_path, "build")
if not os.path.exists(build_dir):
    if args["verbose"]:
        print("Creating compilation output folder")
    os.makedirs(build_dir)
with open(os.path.join(OleanderJS_project_path, "build", "app.html"), "w", encoding="utf-8") as file:
    if args["verbose"]:
        print("Writing build.html file")
    file.write(page_init)
