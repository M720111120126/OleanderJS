import urllib.request, dependencies.json5, os
from typing import Union
from dependencies.OleanderJsInformation import OleanderJS_json5, OleanderJS_api_path, args

def VersionManager() -> dict[str, Union[str, int, dict[str, int]]]:
    try:
        if args["verbose"]:
            print("VersionManager")
        with urllib.request.urlopen("https://oleanderjs.xn--jzh-k69dm57c4fd.xyz/OleanderJS.json5", timeout=5) as response:
            if args["verbose"]:
                print("urllib.request.urlopen OleanderJS.json5")
            dict_original = dependencies.json5.loads(response.read().decode('utf-8'))
            content: dict = dict_original if isinstance(dict_original, dict) else {}
            assert type(content["library"]) == dict, """标准库更新服务器出现问题，请尝试绕过环境检测
The standard library update server has encountered an issue, please try bypassing the environment check"""
            assert type(OleanderJS_json5["library"]) == dict, """API版本文件出现问题
The API version file has encountered an issue"""
            if content["API-version"] == OleanderJS_json5["API-version"]:
                for key in OleanderJS_json5["library"].keys():
                    if content["library"][key] > OleanderJS_json5["library"][key]:
                        if args["verbose"]:
                            print(f"Updata {key}")
                        print(f"""正在更新标准库 {key}。 请在更新完毕后自行在 github.com 上下载最新文档
Updating the standard library {key}. Please download the latest documentation from github.com after the update is complete""")
                        with urllib.request.urlopen(f"https://oleanderjs.xn--jzh-k69dm57c4fd.xyz/library/{key}.js", timeout=5) as response_key:
                            js_new = response_key.read().decode('utf-8')
                            OleanderJS_json5["library"][key] = content["library"][key]
                            js_path = os.path.join(OleanderJS_api_path, "library", "rights" if "com.oleander." in key else "", f"{key}.js")
                            with open(js_path, "w", encoding="utf-8") as file:
                                assert type(js_new) == str, """标准库更新服务器出现问题，请尝试绕过环境检测
The standard library update server has encountered an issue, please try bypassing the environment check"""
                                file.write(js_new)
                with open(os.path.join(OleanderJS_api_path, "OleanderJS.json5"), "w", encoding="utf-8") as file:
                    file.write(dependencies.json5.dumps(OleanderJS_json5))
            else:
                print("""当前API版本与更新服务器版本不一致，无法进行自动标准库库升级
The current API version is inconsistent with the version of the update server, making it impossible to automatically upgrade the standard library""")
    except Exception as e:
        print(e)
        print("""标准库更新服务器出现问题，检测标准库版本失败
The standard library update server has encountered an issue, failed to detect the standard library version""")
    return OleanderJS_json5
