import urllib.request, json5, os

def VersionManager(OleanderJS_json5, OleanderJS_api_path, args):
    if args["verbose"]:
        print("VersionManager")
    with urllib.request.urlopen("https://oleanderjs.xn--jzh-k69dm57c4fd.xyz/OleanderJS.json5", timeout=5) as response:
        if args["verbose"]:
            print("urllib.request.urlopen OleanderJS.json5")
        content: dict[str: int] = json5.loads(response.read().decode('utf-8'))
        if content["API-version"] == OleanderJS_json5:
            for key in OleanderJS_json5["library"].keys():
                if content["library"][key] > OleanderJS_json5["library"][key]:
                    if args["verbose"]:
                        print(f"Updata {key}")
                    with urllib.request.urlopen(f"https://oleanderjs.xn--jzh-k69dm57c4fd.xyz/library/{key}.js", timeout=5) as response_key:
                        js_new = json5.loads(response_key.read().decode('utf-8'))
                        OleanderJS_json5["library"][key] = content["library"][key]
                        js_path = os.path.join(OleanderJS_api_path, "library", "rights" if "com.oleander." in key else "", f"{key}.js")
                        with open(js_path, "w", encoding="utf-8") as file:
                            file.write(js_new)
            with open(os.path.join(OleanderJS_api_path, "OleanderJS.json5"), "w", encoding="utf-8") as file:
                file.write(json5.dumps(OleanderJS_json5))
        else:
            print("""当前API版本与更新服务器版本不一致，无法进行自动标准库库升级
The current API version is inconsistent with the version of the update server, making it impossible to automatically upgrade the standard library""")
    return OleanderJS_json5
