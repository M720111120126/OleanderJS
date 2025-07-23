import os, json5, json, sys, argparse
import ArkOfObjectPro as ArkPRO
import ArkOfObject as ark
from PageProDependencyLibrary import PageProCompilation
from ReusableFunctions import  *
from RightsManagement import ImportModulesThatRequirePermission
from VersionManager import VersionManager

# 读取文件
if os.path.exists("app.json5"):
    OleanderJS_project_path = ""
else:
    OleanderJS_project_path = input("OleanderJS_project_page $ ")
OleanderJS_api_path = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(OleanderJS_project_path, 'app.json5'), 'r', encoding='utf-8') as file:
    app_json5 = json5.loads(file.read())
with open(os.path.join(OleanderJS_project_path, 'build.json5'), 'r', encoding='utf-8') as file:
    build_json5 = json5.loads(file.read())
with open(os.path.join(OleanderJS_api_path, 'OleanderJS.json5'), 'r', encoding='utf-8') as file:
    OleanderJS_json5 = json5.loads(file.read())

# 检查环境
def compare_versions(version1, version2):
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    max_length = max(len(v1_parts), len(v2_parts))
    v1_parts += [0] * (max_length - len(v1_parts))
    v2_parts += [0] * (max_length - len(v2_parts))
    for v1, v2 in zip(v1_parts, v2_parts):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return 2
    return 0
parser = argparse.ArgumentParser()
parser.add_argument("-fver", "--fapi-version", help="""指定 API 版本
Specify API version""", type=str, required=False)
parser.add_argument("-v", "--version", help="""获取 API 版本
Get the API version""", action="store_true")
parser.add_argument("-V", "--verbose", help="""打印出工具链依赖的相关信息以及编译过程中执行的命令
Print out information about toolchain dependencies and commands executed during the compilation process""", action="store_true")
parser.add_argument("-e", "--skip-env-check", help="""跳过环境检查
Get the API version""", action="store_true")
args = vars(parser.parse_args())
compile_option = build_json5["compile-option"]
args.update(compile_option)
if args["fapi_version"]:
    fapi_version = args["fapi_version"]
else:
    fapi_version = ""
if args["version"]:
    print(OleanderJS_json5["API-version"])
if not args["skip_env_check"]:
    if args["verbose"]:
        print("The environment is being inspected")
    OleanderJS_json5 = VersionManager(OleanderJS_json5, OleanderJS_api_path, args)
    if compare_versions(OleanderJS_json5["API-version"], build_json5["Minimum-required-API-version"]) == 2:
        sys.exit("""最低兼容的API版本高于当前API
The minimum compatible API version is higher than the current API""")
    elif compare_versions(OleanderJS_json5["API-version"], build_json5["Target-API-version"]) == 2:
        print("""警告：当前API低于目标的API版本（可能能够正常运行）
Warning: The current API is lower than the target API version (may be able to run normally)""")
    elif compare_versions(OleanderJS_json5["API-version"], build_json5["Target-API-version"]) == 11:
        print("""警告：当前API高于目标的API版本（可能能够正常运行）
Warning: The current API is higher than the target API version (may be able to run normally)""")

# 依赖函数
def path(file_path):
    return os.path.join(OleanderJS_project_path, "APP_Scope", file_path.split(": ")[0].replace("$", ""), file_path.split(": ")[1])
def Oleander_r(file_path):
    return file_to_data_url(path(file_path))
ids = []
class UIComponent:
    def __init__(self):
        self.styles = {}
        self.children = []
        self.id = ""
        self.text = ""
    def set_style(self, **kwargs):
        self.styles.update(kwargs)
        return self
    def style(self, **kwargs):
        return self.set_style(**kwargs)
    def set_attributes(self, key, value):
        setattr(self, key, value)
        return self
    def SA(self, key, value):
        return self.set_attributes(key, value)
    def add_child(self, *childs):
        childs = list(childs)
        for child in childs:
            self.children.append(child)
        return self
    def condition(self, condition):
        self.render2 = self.render
        def a():
            return "<script>document.write(\""+self.render2().replace('"', r'\"')+"\");setInterval(() => {document.getElementById('"+self.id+"').style.display = 'none';if ("+condition+") {document.getElementById('"+self.id+"').style.display = 'block';}}, 100)</script>"
        self.render = a
        return self
    def if_render(self, condition):
        self.condition(condition)
        return self
    def for_render(self, f):
        self.render2 = self.render
        def a():
            return "<script>" + f + ".forEach(item => {document.write(`"+self.render2().replace('"', r'\"')+"`);});</script>"
        self.render = a
        return self
    def render_original(self):
        raise NotImplementedError("""呈现方法必须由子类实现
render method must be implemented by subclasses""")
    def render(self):
        self.id = str(id(self))
        ids.append(self.id)
        if "js_" in self.text:
            self.text = "<script>document.getElementById('"+self.id+"').innerHTML = "+self.text.replace("js_", "")+";function autoUpdateButton() {document.getElementById('"+self.id+"').innerHTML = "+self.text.replace("js_", "")+";}setInterval(autoUpdateButton, 100);</script>"
        return self.render_original()
class Text(UIComponent):
    def __init__(self, text="", size=1):
        super().__init__()
        self.text = text
        self.size = size
    def render_original(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f"<h{self.size} id=\"{self.id}\" style='{style_str}'>{self.text}</h{self.size}>"
class Button(UIComponent):
    def __init__(self, text=""):
        super().__init__()
        self.text = text
        self.on_click = ""
    def set_on_click(self, callback):
        self.on_click = callback
        return self
    def render_original(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f"<button id=\"{self.id}\" style='{style_str}' onclick='" + self.on_click.replace("'", '"') + f"'>{self.text}</button>"
class Radio(UIComponent):
    def __init__(self, name="", value=""):
        super().__init__()
        self.name = name
        self.value = value
        self.checked = False
    def set_checked(self, checked):
        self.checked = checked
        return self
    def render_original(self):
        checked_attr = 'checked' if self.checked else ''
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<input id=\"{self.id}\" type="radio" name="{self.name}" value="{self.value}" {checked_attr} style="{style_str}"/>'
class Toggle(UIComponent):
    def __init__(self, label_on="", label_off=""):
        super().__init__()
        self.label_on = label_on
        self.label_off = label_off
        self.checked = False
    def set_checked(self, checked):
        self.checked = checked
        return self
    def render_original(self):
        label = self.label_on if self.checked else self.label_off
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<button id=\"{self.id}\" style="{style_str}">{label}</button>'
class Progress(UIComponent):
    def __init__(self, value=0):
        super().__init__()
        self.value = value
    def set_value(self, value):
        self.value = value
        return self
    def render_original(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<progress id=\"{self.id}\" value="{self.value}" max="100" style="{style_str}"></progress>'
class Image(UIComponent):
    def __init__(self, src=""):
        super().__init__()
        self.src = src
    def render_original(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<img id=\"{self.id}\" src="{self.src}" style="{style_str}"/>'
class Linear(UIComponent):
    def __init__(self):
        super().__init__()
    def render_original(self):
        style_str = " ".join([f'{k}: {v};' for k, v in json.loads(json.dumps(self.styles).replace("_", "-")).items()])
        children_str = "".join([child.render() for child in self.children])
        return f'<div id=\"{self.id}\" style="{style_str}">{children_str}</div>'
class Row(Linear):
    def __init__(self):
        super().__init__()
    def render_original(self):
        self.set_style(display='flex', flex_direction='row')
        return super().render_original()
class Column(Linear):
    def __init__(self):
        super().__init__()
    def render_original(self):
        self.set_style(display='flex', flex_direction='column')
        return super().render_original()
class Dialog(UIComponent):
    def __init__(self, title="", content=""):
        super().__init__()
        self.title = title
        self.content = content
    def render_original(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<div id=\"{self.id}\" class="dialog" style="{style_str}"><h1>{self.title}</h1><p>{self.content}</p></div>'
class Menu(UIComponent):
    def __init__(self):
        super().__init__()
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        return self
    def render_original(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        items_str = "".join([f'<li>{item}</li>' for item in self.items])
        return f'<ul id=\"{self.id}\" style="{style_str}">{items_str}</ul>'
class Iframe(UIComponent):
    def __init__(self, src="", width="600", height="400"):
        super().__init__()
        self.src = src
        self.width = width
        self.height = height
        self.style = ""
    def render_original(self):
        for Iframe_page in app_json5["page"]:
            if Iframe_page["name"] == self.src:
                # 返回一个iframe标签，包含src和其他属性
                return f'<iframe id=\"{self.id}\" width="{self.width}" height="{self.height}" style="{self.style}">{compilation(loading_page(page, "init.yh"))}</iframe>'
        return None
class if_UIComponent(UIComponent):
    def __init__(self, condition=""):
        super().__init__()
        self.condition = condition
    def render_original(self):
        self.children[0].if_render(self.condition)
        return self.children[0].render()
def loading_page(page_loading, name, mode="init"):
    with open(os.path.join(OleanderJS_project_path, page_loading["srcPath"], name), "r", encoding='utf-8') as f:
        if args["verbose"]:
            print(f'Loading page {name}:page_loading="{page_loading}";mode="{mode}"')
        f = f.read()
        include = []
        for i in page_loading["dependencies"]:
            if not i == name:
                include.append([f'#include {i}', loading_page(page_loading, i, "self")])
        library_path = os.path.join(OleanderJS_api_path, "library")
        for i in [f for f in os.listdir(library_path) if os.path.isfile(os.path.join(library_path, f))]:
            with open(os.path.join(library_path, i), "r", encoding='utf-8') as f2:
                i2 = i.replace(".js", "")
                include.append([f'#include {i2}', f2.read()])
        for i in find_lines_with_text_outside_quotes(f, "#define "):
            include.append([i.split(" ")[1], i.split(" ")[2]])
        if mode == "self":
            return replace_outside_quotes(f, include)
        return ImportModulesThatRequirePermission(replace_outside_quotes(f, include), OleanderJS_project_path, page_loading, name, loading_page)

# 编译
def compilation(text):
    text_list = replace_outside_quotes(text, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    if args["verbose"]:
        print(f'Compiling.object-OleanderUI-yh=```{replace_outside_quotes(text_list[1], [["$", "Oleander_"]])}```')
    exec(replace_outside_quotes(text_list[1], [["$", "Oleander_"]]), globals())
    try:
        icon_path = path(app_json5['APP_Scope']['icon'])
        mime_type = filetype.guess(icon_path)
        if mime_type is None:
            mime_type = "image/png"
        else:
            mime_type = mime_type.mime
        return f"<!DECTYPE HTML><html lang='{app_json5['APP_Scope']['lang']}'><head><!-- Project: {build_json5['name']} --><!-- Version: {build_json5['version']} --><script>let ProjectName = '{build_json5['name']}';let rights_name_json;"+"try {rights_name_json = JSON.parse(localStorage.getItem(ProjectName + '/rights')) || [];} catch (error) {rights_name_json = [];}"+f"{text_list[0]}</script><meta charset='utf-8'><title>{app_json5['APP_Scope']['name']}</title><link rel='icon' type='{mime_type}' href='{file_to_data_url(icon_path)}'></head><body>{html}</body></html>"
    except:
        return f"<!DECTYPE HTML><html><head><!-- Project: {build_json5['name']} --><!-- Version: {build_json5['version']} --><script>let ProjectName = '{build_json5['name']}';let rights_name_json;"+"try {rights_name_json = JSON.parse(localStorage.getItem(ProjectName + '/rights')) || [];} catch (error) {rights_name_json = [];}"+f"{text_list[0]}</script><meta charset='utf-8'></head><body>{html}</body></html>"
page_init = ""
html = ""
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
        PageProCompilation(loading_page, fapi_version, page, compilation, OleanderJS_project_path, UIComponent)
build_dir = os.path.join(OleanderJS_project_path, "build")
if not os.path.exists(build_dir):
    if args["verbose"]:
        print("Creating compilation output folder")
    os.makedirs(build_dir)
with open(os.path.join(OleanderJS_project_path, "build", "app.html"), "w", encoding="utf-8") as file:
    if args["verbose"]:
        print("Writing build.html file")
    file.write(page_init)
