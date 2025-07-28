import json5, sys
from ReusableFunctions import  *
from typing import List, Dict, Any, Optional

class Node:
    def __init__(self, name: str):
        self.name = name
        self.props: List[Dict[str, Any]] = []
        self.children: List[Node] = []
    def to_string(self, indent: int = 0) -> str:
        sp = '  ' * indent
        lines = [f"{sp}{self.name}() {{"]
        for kv in self.props:
            for k, v in kv.items():
                lines.append(f"{sp}  \"{k}\" : {v},")
        for child in self.children:
            lines.append(child.to_string(indent + 1))
        lines.append(f"{sp}}}")
        return '\n'.join(lines)
def transform(s: str) -> str:
    try:
        re_inline = re.compile(r'^\s*(\w+)\(\)\s*{\s*}\s*$')
        re_open = re.compile(r'^\s*(\w+)\(\)\s*{\s*$')
        re_close = re.compile(r'^\s*}\s*$')
        re_style = re.compile(r'\.style\s*\(([^)]*)\)')
        re_data = re.compile(r'\.(\w+)\s*=\s*(.+)')
        re_method = re.compile(r'\.(\w+)\((.+)\)')
        stack: List[Node] = []
        last_closed: Optional[Node] = None
        for line in s.splitlines():
            line = line.strip()
            if not line:
                continue
            m = re_inline.match(line)
            if m:
                node = Node(m.group(1))
                if stack:
                    stack[-1].children.append(node)
                last_closed = node
                continue
            m = re_open.match(line)
            if m:
                node = Node(m.group(1))
                if stack:
                    stack[-1].children.append(node)
                stack.append(node)
                continue
            if re_close.match(line):
                last_closed = stack.pop()
                continue
            if last_closed is None:
                sys.exit("transform error")
            m = re_style.match(line)
            if m:
                body = m.group(1)
                for part in re.split(r'\s*,\s*', body):
                    if '=' in part:
                        k, v = part.split('=', 1)
                        k = k.strip().strip('"')
                        v = v.strip()
                        last_closed.props.append({k: v})
                continue
            m = re_data.match(line)
            if m:
                key, val = m.group(1), m.group(2).strip()
                last_closed.props.append({f"data_{key}": val})
                continue
            m = re_method.match(line)
            if m:
                key, arg = m.group(1), m.group(2).strip()
                last_closed.props.append({f"method_{key}": arg})
                continue
        root = stack[0] if stack else last_closed
        return root.to_string() if root else ''
    except:
        return s

def analyzing(s:dict) -> dict:
    key = list(s.keys())
    return {"type":re.sub(r'\d+', '', key[0]), "content": [{key: value} for key, value in s[key[0]].items()], "name": key[0]}
def render(s:dict, condition:str="") -> str:
    now = analyzing(s)
    out = ""
    out += "\n" + now["name"].translate(str.maketrans("0123456789", "abcdefghij")) + "=" + now["type"] + "()"
    content = []
    for i in now["content"]:
        key = list(i.keys())[0]
        if bool(re.search(r'\d', key)):
            content.append(key)
            if "quote" in key:
                out += "\n" + key.translate(str.maketrans("0123456789", "abcdefghij")) + "=" + i[key]
                out += "\n" + key.translate(str.maketrans("0123456789", "abcdefghij")) + '.condition("' + condition + '")'
            else:
                out += "\n" + render(i, condition)
        else:
            if "if_" in key:
                for i2 in i[key].keys():
                    i[key][i2]["method_condition"] = key.replace("if_", "")
                    content.append(i2)
                out += "\n" + render(i[key])
            elif "data_" in key:
                out += "\n" + now["name"].translate(str.maketrans("0123456789", "abcdefghij")) + "." + key.replace("data_", "") + '="' + i[key] + '"'
            elif "method_" in key:
                out += "\n" + now["name"].translate(str.maketrans("0123456789", "abcdefghij")) + "." + key.replace("method_", "") + '("' + i[key] + '")'
            else:
                out += "\n" + now["name"].translate(str.maketrans("0123456789", "abcdefghij")) + ".set_style(" + key + '="' + i[key] + '")'
    for i in content:
        out += "\n" + now["name"].translate(str.maketrans("0123456789", "abcdefghij")) + ".add_child(" + i.translate(str.maketrans("0123456789", "abcdefghij")) + ')'
    return out
def ark(s:str, m:str):
    text_list = replace_outside_quotes(s, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    return f'{text_list[0]}\n# UI_start\n{compilation(text_list[1], m)}'
def compilation(input_str:str, m:str):
    for i in find_lines_with_text_outside_quotes(input_str, "if("):
        input_str = replace_outside_quotes(input_str, [[i, str_encrypt(i.replace(") {", ""))+"_if() {"]], count=1)
    output_str = transform(input_str)
    for i in find_lines_with_text_outside_quotes(input_str, "_if"):
        output_str = replace_outside_quotes(output_str, [[i, str_decrypt(i.replace("() {", "").replace("_if", "", 1))+") {"]], count=1)
    for i2 in list(range(len(find_lines_with_text_outside_quotes(output_str, "if(")))):
        i = find_lines_with_text_outside_quotes(output_str, "if(")[0]
        output_str = replace_outside_quotes(output_str, [[i, replace_outside_quotes(i, [["if(", '"if_'], [") {", '":{']])]], count=1)
    for i2 in list(range(len(find_lines_with_text_outside_quotes(output_str, "() {")))):
        i = find_lines_with_text_outside_quotes(output_str, "() {")[0]
        output_str = replace_outside_quotes(output_str, [
            [i, '"' + str(i2) + replace_outside_quotes(i, [["() {", '"']]).replace(" ", "") + ":{"]], count=1)
    for i2 in list(range(len(find_lines_with_text_outside_quotes(output_str, ";")))):
        i = find_lines_with_text_outside_quotes(output_str, ";")[0]
        output_str = output_str.replace(i, '"quote' + str(i2) + '":"' + replace_outside_quotes(
            replace_outside_quotes(i.replace("'", r"\'").replace('"', r'\"'), [[";", '']]), [[" ", ""]]) + '",', 1)
    output_str = replace_outside_quotes(output_str, [["}", "},"]])
    try:
        output_str_original = json5.loads("{" + output_str + "}")
        output_str = output_str_original if isinstance(output_str_original, dict) else {}
        if len(output_str.keys()) > 1:
            sys.exit("""最外层只能使用一个组件
The outermost layer can only use one component""")
        return render(output_str) + "\n\nhtml = " + list(output_str.keys())[0].translate(str.maketrans("0123456789", "abcdefghij")) + ".render()"
    except:
        if m == "into":
            return input_str
        else:
            sys.exit("""ark版OleanderUI渲染出现错误
ark version OleanderUI rendering error""")
