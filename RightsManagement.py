import os, json5
from ReusableFunctions import  *

def ImportModulesThatRequirePermission(str, OleanderJS_project_path, page_loading, name, loading_page):
    include = []
    OleanderJS_api_path = os.path.dirname(os.path.abspath(__file__))
    ModulesThatRequirePermission_path = os.path.join(OleanderJS_api_path, "library\\rights")
    for i in [f for f in os.listdir(ModulesThatRequirePermission_path ) if os.path.isfile(os.path.join(ModulesThatRequirePermission_path , f))]:
        with open(os.path.join(ModulesThatRequirePermission_path , i), "r", encoding='utf-8') as f2:
            i2 = i.replace(".js", "")
            include.append([f'#include {i2}', f2.read()])
    with open(os.path.join(OleanderJS_project_path, 'app.json5'), 'r', encoding='utf-8') as file:
        app_json5 = json5.loads(file.read())
        for i in page_loading["dependencies"]:
            if not i == name:
                include.append([f'#include {i}', loading_page(page_loading, i)])
    ModulesThatRequirePermission = ""
    for modules in app_json5["APP_Scope"]["require"]:
        with open(os.path.join(ModulesThatRequirePermission_path, modules)+".js", 'r', encoding='utf-8') as file:
            ModulesThatRequirePermission = ModulesThatRequirePermission + file.read()
    return ModulesThatRequirePermission + replace_outside_quotes(str, include)