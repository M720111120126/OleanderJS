import os, dependencies.json5, sys, argparse
import dependencies.toml

parser = argparse.ArgumentParser()
parser.add_argument("-fver", "--fapi-version", help="""指定 API 版本
Specify API version""", type=str, required=False)
parser.add_argument("-v", "--version", help="""获取 API 版本
Get the API version""", action="store_true")
parser.add_argument("-V", "--verbose", help="""打印出工具链依赖的相关信息以及编译过程中执行的命令
Print out information about toolchain dependencies and commands executed during the compilation process""", action="store_true")
parser.add_argument("-e", "--skip-env-check", help="""跳过环境检查
Get the API version""", action="store_true")
parser.add_argument("-b", "--build", help="""构建项目
Build the project""", action="store_true")
parser.add_argument("-i", "--init", help="""初始化项目
Initialize the project""", action="store_true")
try:
    args = vars(parser.parse_args())
    args["OJC"] = False
except:
    args = {"init": False, "OJC": True}

# 读取文件
if os.path.exists("app.json5") or os.path.exists("app.toml") or args["init"] or args["OJC"]:
    OleanderJS_project_path = ""
else:
    OleanderJS_project_path = input("OleanderJS_project_page $ ")
OleanderJS_api_path = os.path.dirname(os.path.abspath(__file__))
build_json5 = {"compile-option":{}}
app_json5 = {}
OleanderJS_json5 = {}
if not (args["init"] or args["OJC"]):
    if os.path.exists(os.path.join(OleanderJS_project_path, "app.toml")):
        with open(os.path.join(OleanderJS_project_path, 'app.toml'), 'r', encoding='utf-8') as file:
            app_json5_original = dependencies.toml.loads(file.read())
            app_json5 = app_json5_original if isinstance(app_json5_original, dict) else {}
        with open(os.path.join(OleanderJS_project_path, 'build.toml'), 'r', encoding='utf-8') as file:
            build_json5_original = dependencies.toml.loads(file.read())
            build_json5 = build_json5_original if isinstance(build_json5_original, dict) else {}
            build_json5 = build_json5_original if isinstance(build_json5_original, dict) else {}
    elif os.path.exists(os.path.join(OleanderJS_project_path, "app.json5")):
        with open(os.path.join(OleanderJS_project_path, 'app.json5'), 'r', encoding='utf-8') as file:
            app_json5_original = dependencies.json5.loads(file.read())
            app_json5 = app_json5_original if isinstance(app_json5_original, dict) else {}
        with open(os.path.join(OleanderJS_project_path, 'build.json5'), 'r', encoding='utf-8') as file:
            build_json5_ = dependencies.json5.loads(file.read())
            build_json5 = build_json5_ if isinstance(build_json5_, dict) else {}
    else:
        print("""未找到项目配置文件
No project configuration file found""")
        sys.exit(1)
    with open(os.path.join(OleanderJS_api_path, 'OleanderJS.json5'), 'r', encoding='utf-8') as file:
        OleanderJS_json5_original = dependencies.json5.loads(file.read())
        OleanderJS_json5 = OleanderJS_json5_original if isinstance(OleanderJS_json5_original, dict) else {}

compile_option = build_json5["compile-option"]
args.update(compile_option)
