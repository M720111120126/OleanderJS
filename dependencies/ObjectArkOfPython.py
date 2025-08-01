import os, json
from dependencies.ReusableFunctions import  *
from dependencies.RightsManagement import ImportModulesThatRequirePermission
from dependencies.OleanderJsInformation import OleanderJS_project_path, OleanderJS_api_path, args, app_json5, build_json5
import dependencies.ArkOfObjectPro as ArkPRO
from typing import Literal, Union

def Oleander_r(file_path: str) -> str:
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
class if_UIComponent(UIComponent):
    def __init__(self, condition=""):
        super().__init__()
        self.condition_text = condition
    def render_original(self):
        self.children[0].if_render(self.condition_text)
        return self.children[0].render()
def loading_page(page_loading: dict[str, str | list[str]], name: str, mode:Literal["init", "self"]="init"):
    assert type(page_loading["name"]) == str, "OleanderJsAPI Error: app_json5[\"page\"][\"name\"] must be a string"
    assert type(page_loading["srcPath"]) == str, "OleanderJsAPI Error: app_json5[\"page\"][\"srcPath\"] must be a string"
    assert type(page_loading["dependencies"]) == list[str], "OleanderJsAPI Error: app_json5[\"page\"][\"dependencies\"] must be a list of strings"
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
        return ImportModulesThatRequirePermission(replace_outside_quotes(f, include), page_loading, name, loading_page)

def compilation(text: str) -> str:
    text_list = replace_outside_quotes(text, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    if args["verbose"]:
        print(f'Compiling.object-OleanderUI-yh=```{replace_outside_quotes(text_list[1], [["$", "Oleander_"]])}```')
    local_vars = {}
    exec(replace_outside_quotes(text_list[1], [["$", "Oleander_"], ["eval", "eval_new"]]), globals(), local_vars)
    html = local_vars['html']
    try:
        icon_path = path(app_json5['APP_Scope']['icon'])
        mime_type = dependencies.filetype.guess(icon_path)
        if mime_type is None:
            mime_type = "image/png"
        else:
            mime_type = mime_type.mime
        return f"<!DECTYPE HTML><html lang='{app_json5['APP_Scope']['lang']}'><head><!-- Project: {build_json5['name']} --><!-- Version: {build_json5['version']} --><script>let ProjectName = '{build_json5['name']}';let rights_name_json;"+"try {rights_name_json = JSON.parse(localStorage.getItem(ProjectName + '/rights')) || [];} catch (error) {rights_name_json = [];}function eval_new(s) {if (window.confirm('允许执行：'+s+'？')) {try {return eval(s);} catch (e) {console.error('执行失败：', e);}}}"+f"{text_list[0]}</script><meta charset='utf-8'><title>{app_json5['APP_Scope']['name']}</title><link rel='icon' type='{mime_type}' href='{file_to_data_url(icon_path)}'></head><body>{html}</body></html>"
    except:
        return f"<!DECTYPE HTML><html><head><!-- Project: {build_json5['name']} --><!-- Version: {build_json5['version']} --><script>let ProjectName = '{build_json5['name']}';let rights_name_json;"+"try {rights_name_json = JSON.parse(localStorage.getItem(ProjectName + '/rights')) || [];} catch (error) {rights_name_json = [];}function eval_new(s) {if (window.confirm('允许执行：'+s+'？')) {try {return eval(s);} catch (e) {console.error('执行失败：', e);}}}"+f"{text_list[0]}</script><meta charset='utf-8'></head><body>{html}</body></html>"
def CompilationLow(text: str, name:str) -> str:
    text_list = replace_outside_quotes(ArkPRO.ArkPRO(text, "into", get_all_subclasses(UIComponent)), [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    local_vars = {}
    # print(text_list[1])
    exec(replace_outside_quotes(text_list[1], [["$", "Oleander_"], ["eval", "eval_new"]]), globals(), local_vars)
    html = local_vars['html']
    return f"<!DECTYPE HTML><html><head><script>let ProjectName = '{name}';let rights_name_json;"+"try {rights_name_json = JSON.parse(localStorage.getItem(ProjectName + '/rights')) || [];} catch (error) {rights_name_json = [];}function eval_new(s) {if (window.confirm('允许执行：'+s+'？')) {try {return eval(s);} catch (e) {console.error('执行失败：', e);}}}"+f"{text_list[0]}</script><meta charset='utf-8'></head><body>{html}</body></html>"
