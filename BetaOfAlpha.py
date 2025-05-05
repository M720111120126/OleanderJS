import json5, sys
from ReusableFunctions import  *

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
def beta(s:str):
    text_list = replace_outside_quotes(s, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    return f'{text_list[0]}\n# UI_start\n{compilation(text_list[1])}'
def compilation(input_str:str):
    output_str = input_str
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
        output_str = json5.loads("{" + output_str + "}")
        if len(output_str.keys()) > 1:
            sys.exit("""最外层只能使用一个组件
The outermost layer can only use one component""")
        return render(output_str) + "\n\nhtml = " + list(output_str.keys())[0].translate(str.maketrans("0123456789", "abcdefghij")) + ".render()"
    except:
        return input_str
