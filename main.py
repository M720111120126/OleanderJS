import os, json5, re, sys

# 读取文件
project = os.getcwd()
with open('app.json5', 'r', encoding='utf-8') as file:
    app_json5 = json5.loads(file.read())
with open('build.json5', 'r', encoding='utf-8') as file:
    build_json5 = json5.loads(file.read())

# 依赖函数
def replace_outside_quotes(text, signDic):
    quoted = []
    def save_quoted(match):
        quoted.append(match.group(0))
        return 'QUOTED_TEXT'
    text_with_placeholders = re.sub(r'(["\']).*?\1', save_quoted, text)
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
        include = []
        for i in app_json5["dependencies"]:
            include.append([f'#include "{i}"', loading_page(page["srcPath"], i)])
        for i in find_lines_with_text_outside_quotes(file.read(), "#define "):
            include.append([i.split(" ")[1], i.split(" ")[2]])
        for i in find_lines_with_text_outside_quotes(file.read(), "#include "):
            include.append([i, f"import {i.split(" ")[1]}"])
        return replace_outside_quotes(file.read(), include)

# 编译
dependencies_code = """
const_list = []
var_list = []
def const(key, data):
    if key in const_list or key in var_list:
        sys.exit("Error！已定义")
    else:
        const_list.append(key)
        exec(f"{key} = {data}")
def var(key, data):
    if key in const_list or key in var_list:
        sys.exit("Error！已定义")
    else:
        var_list.append(key)
        exec(f"{key} = {data}")
def modify(key, data):
    if key in const_list:
        sys.exit("Error！无法修改常量")
    elif key in var_list:
        exec(f"{key} = {data}")
    else:
        sys.exit("Error！未定义")
"""
def compilation(text):
    key = {
        "&\\": "\\",
        "\\": "#",
        ";": "\n",
        "/*": "'''",
        "*/": "'''"
    }
    for i in find_lines_with_text_outside_quotes(text, "var"):
        text = text.replace(i, i.replace("=", ",").replace("var ", "var(")+")")
        for i in find_lines_with_text_outside_quotes(text, "const"):
            text = text.replace(i, i.replace("=", ",").replace("const ", "const(") + ")")
    for i in find_lines_with_text_outside_quotes(text, "="):
        text = text.replace(i, "modify("+i.replace("=", ",")+")")
    return replace_outside_quotes(text, key)
page_init = ""
pages = {}
for page in app_json5["page"]:
    if page["name"] == "init":
        page_init = compilation(loading_page(page, "init.yh"))
    else:
        pages.update({page["name"], compilation(loading_page(page, "init.yh"))})
with open("app.py", "w", encoding="utf-8") as file:
    file.write(dependencies_code+page_init)