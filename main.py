import os, json5, json, sys, argparse, filetype
import BetaOfAlpha as Beta
from ReusableFunctions import  *

# 读取文件
project = os.getcwd()
with open('app.json5', 'r', encoding='utf-8') as file:
    app_json5 = json5.loads(file.read())
with open('build.json5', 'r', encoding='utf-8') as file:
    build_json5 = json5.loads(file.read())
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'OleanderTS.json5'), 'r', encoding='utf-8') as file:
    OleanderTS_json5 = json5.loads(file.read())

# 检查环境
parser = argparse.ArgumentParser()
parser.add_argument("-fver", "--fapi-version", help="""指定 API 版本
Specify API version""", type=str, required=False)
parser.add_argument("-v", "--version", help="""获取 API 版本
Get the API version""", action="store_true")
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
    print(OleanderTS_json5["API-version"])
if not args["skip_env_check"]:
    if build_json5["Minimum-required-API-version"] > OleanderTS_json5["API-version"]:
        sys.exit("""最低兼容的API版本高于当前API
The minimum compatible API version is higher than the current API""")
    elif build_json5["Target-API-version"] > OleanderTS_json5["API-version"]:
        print("""警告：当前API低于目标的API版本（可能能够正常运行）
Warning: The current API is lower than the target API version (may be able to run normally)""")


# 依赖函数
def js(s, id_this=None):
    if id_this is None:
        return f"<script>{s}</script>"
    else:
        id_this = str(id_this)
        return "<script>document.getElementById('"+id_this+"').innerHTML = "+s+";function autoUpdateButton() {document.getElementById('"+id_this+"').innerHTML = i;};setInterval(autoUpdateButton, 1000);</script>"
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
    def add_child(self, child):
        self.children.append(child)
        return self
    def condition(self, condition):
        self.render2 = self.render
        def a():
            return "<script>if ("+condition+") {document.write(\""+self.render2().replace('"', r'\"')+"\");}</script>"
        self.render = a
    def for_render(self, f):
        self.render2 = self.render
        def a():
            return "<script>" + f + ".forEach(item => {document.write(`"+self.render2().replace('"', r'\"')+"`);});</script>"
        self.render = a
    def render_original(self):
            raise NotImplementedError("""呈现方法必须由子类实现
    render method must be implemented by subclasses""")
    def render(self):
        self.id = id(self)
        ids.append(self.id)
        if "js_" in self.text:
            self.text = js(self.text.replace("js_", ""), self.id)
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
    def set_style(self, **kwargs):
        self.style = "; ".join([f"{key}: {value}" for key, value in kwargs.items()])
    def render_original(self):
        for Iframe_page in app_json5["page"]:
            if Iframe_page["name"] == self.src:
                # 返回一个iframe标签，包含src和其他属性
                return f'<iframe id=\"{self.id}\" width="{self.width}" height="{self.height}" style="{self.style}">{compilation(loading_page(page, "init.yh"))}</iframe>'
        return None
def loading_page(page_loading, name):
    with open(os.path.join(page_loading["srcPath"], name), "r", encoding='utf-8') as f:
        f = f.read()
        include = []
        for i in page_loading["dependencies"]:
            if not i == name:
                include.append([f'#include {i}', loading_page(page_loading, i)])
        for i in find_lines_with_text_outside_quotes(f, "#define "):
            include.append([i.split(" ")[1], i.split(" ")[2]])
        return replace_outside_quotes(f, include)

# 编译
def compilation(text):
    text_list = replace_outside_quotes(text, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    exec(text_list[1], globals())
    icon_path = "APP_Scope/" + app_json5['APP_Scope']['icon'].split(": ")[0].replace("$", "") + "/" + app_json5['APP_Scope']['icon'].split(": ")[1]
    mime_type = filetype.guess(icon_path)
    if mime_type is None:
        mime_type = "image/png"
    else:
        mime_type = mime_type.mime
    return f"<!DECTYPE HTML><html lang='{app_json5['APP_Scope']['lang']}'><head><!-- Project: {build_json5['name']} --><!-- Version: {build_json5['version']} --><script>{text_list[0]}</script><meta charset='utf-8'><title>{app_json5['APP_Scope']['name']}</title><link rel='icon' type='{mime_type}' href='{file_to_data_url(icon_path)}'></head><body>" + html + "</body></html>"
page_init = ""
html = ""
for page in app_json5["page"]:
    if page["name"] == "init":
        if fapi_version == "":
            page_init = compilation(Beta.beta(loading_page(page, "init.yh")))
        elif fapi_version == "beta":
            page_init = compilation(Beta.beta(loading_page(page, "init.yh")))
        elif fapi_version == "alpha":
            page_init = compilation(loading_page(page, "init.yh"))
with open("app.html", "w", encoding="utf-8") as file:
    file.write(page_init)