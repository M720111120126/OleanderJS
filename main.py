import os, json5, re

# 读取文件
project = os.getcwd()
with open('app.json5', 'r', encoding='utf-8') as file:
    app_json5 = json5.loads(file.read())
with open('build.json5', 'r', encoding='utf-8') as file:
    build_json5 = json5.loads(file.read())

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
    def render(self):
        raise NotImplementedError("""呈现方法必须由子类实现
render method must be implemented by subclasses""")
class Button(UIComponent):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.on_click = None
    def set_on_click(self, callback):
        self.on_click = callback
        return self
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f"<button style='{style_str}' onclick='{self.on_click.replace("'", '"')}'>{self.text}</button>"
class Radio(UIComponent):
    def __init__(self, name, value):
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
    def __init__(self, label_on, label_off):
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
    def __init__(self, src):
        super().__init__()
        self.src = src
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        return f'<img src="{self.src}" style="{style_str}"/>'
class Row(UIComponent):
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        children_str = "".join([child.render() for child in self.children])
        return f'<div style="{style_str}">{children_str}</div>'
class Column(UIComponent):
    def render(self):
        style_str = " ".join([f'{k}: {v};' for k, v in self.styles.items()])
        children_str = "".join([child.render() for child in self.children])
        return f'<div style="{style_str}">{children_str}</div>'
class Dialog(UIComponent):
    def __init__(self, title, content):
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
    def __init__(self, src, width="600", height="400"):
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
def replace_outside_quotes(text, signDic):
    quoted = []
    def save_quoted(match):
        quoted.append(match.group(0))
        return 'QUOTED_TEXT'
    text_with_placeholders = re.sub(r'(["\']).*?\1', save_quoted, text)
    if signDic:
        for i in signDic:
            text_with_placeholders = text_with_placeholders.replace(i[0], i[1])
    for q in quoted:
        text_with_placeholders = text_with_placeholders.replace('QUOTED_TEXT', q, 1)
    return text_with_placeholders
def find_lines_with_text_outside_quotes(text, txt):
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
    exec(text.split("# UI_start")[1], globals())
    return f"<script>{text.split('# UI_start')[0]}</script>" + html
page_init = ""
for page in app_json5["page"]:
    if page["name"] == "init":
        page_init = compilation(loading_page(page, "init.yh"))
with open("app.html", "w", encoding="utf-8") as file:
    file.write(page_init)