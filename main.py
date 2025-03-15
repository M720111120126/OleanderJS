import os, json5, re, zipfile, json
from io import BytesIO

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
        return replace_outside_quotes(file.read(), include)

project = os.getcwd()
with open('app.txt', 'r', encoding='utf-8') as file:
    app_json5 = json5.loads(file.read())
with open('build.txt', 'r', encoding='utf-8') as file:
    build_json5 = json5.loads(file.read())
pages = []
for page in app_json5["page"]:
    pages.append({"name": page["name"], "code": loading_page(page, "init.yh")})
with zipfile.ZipFile('init.app', 'w') as zip_ref:
    for i in pages:
        file_data = BytesIO(i["code"].encode('utf-8'))
        zip_ref.writestr(f'{i["name"]}.ojs', file_data.getvalue())
        file_data = BytesIO(json.dumps(app_json5).encode('utf-8'))
        zip_ref.writestr('app.json', file_data.getvalue())
        file_data = BytesIO(json.dumps(build_json5).encode('utf-8'))
        zip_ref.writestr('build.json', file_data.getvalue())
        zip_ref.write('resources.zip', arcname='resources.zip')
# sc嵌入，未开发完毕