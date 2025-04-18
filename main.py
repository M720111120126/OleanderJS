import os, json5, re, json, sys, argparse
import BetaOfAlpha as Beta

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
print(args)
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
class UIComponent:
    def __init__(self):
        self.styles = {}
        self.children = []
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
    def render(self):
        raise NotImplementedError("""呈现方法必须由子类实现
render method must be implemented by subclasses""")
class Button(UIComponent):
    def __init__(self, text=""):
        super().__init__()
        self.text = text
        self.on_click = ""
    def set_on_click(self, callback):
        self.on_click = callback
        return self
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f"<button style='{style_str}' onclick='{self.on_click.replace("'", '"')}'>{self.text}</button>"
class Radio(UIComponent):
    def __init__(self, name="", value=""):
        super().__init__()
        self.name = name
        self.value = value
        self.checked = False
    def set_checked(self, checked):
        self.checked = checked
        return self
    def render(self):
        checked_attr = 'checked' if self.checked else ''
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<input type="radio" name="{self.name}" value="{self.value}" {checked_attr} style="{style_str}"/>'
class Toggle(UIComponent):
    def __init__(self, label_on="", label_off=""):
        super().__init__()
        self.label_on = label_on
        self.label_off = label_off
        self.checked = False
    def set_checked(self, checked):
        self.checked = checked
        return self
    def render(self):
        label = self.label_on if self.checked else self.label_off
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<button style="{style_str}">{label}</button>'
class Progress(UIComponent):
    def __init__(self, value=0):
        super().__init__()
        self.value = value
    def set_value(self, value):
        self.value = value
        return self
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<progress value="{self.value}" max="100" style="{style_str}"></progress>'
class Image(UIComponent):
    def __init__(self, src=""):
        super().__init__()
        self.src = src
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<img src="{self.src}" style="{style_str}"/>'
class Row(UIComponent):
    def render(self):
        self.set_style(display='flex', flex_direction='row')
        style_str = " ".join([f'{k}: {v};' for k, v in json.loads(json.dumps(self.styles).replace("_", "-")).items()])
        children_str = "".join([child.render() for child in self.children])
        return f'<div style="{style_str}">{children_str}</div>'
class Column(UIComponent):
    def render(self):
        self.set_style(display='flex', flex_direction='column')
        style_str = " ".join([f'{k}: {v};' for k, v in json.loads(json.dumps(self.styles).replace("_", "-")).items()])
        children_str = "".join([child.render() for child in self.children])
        return f'<div style="{style_str}">{children_str}</div>'
class Dialog(UIComponent):
    def __init__(self, title="", content=""):
        super().__init__()
        self.title = title
        self.content = content
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<div class="dialog" style="{style_str}"><h1>{self.title}</h1><p>{self.content}</p></div>'
class Menu(UIComponent):
    def __init__(self):
        super().__init__()
        self.items = []
    def add_item(self, item):
        self.items.append(item)
        return self
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        items_str = "".join([f'<li>{item}</li>' for item in self.items])
        return f'<ul style="{style_str}">{items_str}</ul>'
class Iframe(UIComponent):
    def __init__(self, src="", width="600", height="400"):
        super().__init__()
        self.src = src
        self.width = width
        self.height = height
        self.style = ""
    def set_style(self, **kwargs):
        self.style = "; ".join([f"{key}: {value}" for key, value in kwargs.items()])
    def render(self):
        for page in app_json5["page"]:
            if page["name"] == self.src:
                # 返回一个iframe标签，包含src和其他属性
                return f'<iframe width="{self.width}" height="{self.height}" style="{self.style}">{compilation(loading_page(page, "init.yh"))}</iframe>'
def replace_outside_quotes(text: str, signDic: list, rule: str = r'(["\']).*?\1', count: int = -1) -> str:
    quoted = []
    def save_quoted(match):
        quoted.append(match.group(0))
        return 'QUOTED_TEXT'
    text_with_placeholders = re.sub(rule, save_quoted, text)
    if signDic:
        for i in signDic:
            text_with_placeholders = text_with_placeholders.replace(i[0], i[1], count)
    for q in quoted:
        text_with_placeholders = text_with_placeholders.replace('QUOTED_TEXT', q, 1)
    return text_with_placeholders
def find_lines_with_text_outside_quotes(text: str, txt: str) -> list[str]:
    lines = text.splitlines()
    result_lines = []
    for line in lines:
        modified_line = re.sub(r'(["\']).*?\1', '', line)
        if txt in modified_line:
            result_lines.append(line)
    return result_lines
def loading_page(page, name):
    with open(os.path.join(page["srcPath"], name), "r", encoding='utf-8') as file:
        f = file.read()
        include = []
        for i in page["dependencies"]:
            if not i == name:
                include.append([f'#include {i}', loading_page(page, i)])
        for i in find_lines_with_text_outside_quotes(f, "#define "):
            include.append([i.split(" ")[1], i.split(" ")[2]])
        return replace_outside_quotes(f, include)

# 编译
def compilation(text):
    text_list = replace_outside_quotes(text, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    exec(text_list[1], globals())
    return f"<!-- Project: {build_json5['name']} --><!-- Version: {build_json5['version']} --><script>{text_list[0]}</script>" + html
page_init = ""
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