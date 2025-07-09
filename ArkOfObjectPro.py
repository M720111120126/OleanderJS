import sys
import ArkOfObject as ark
from ReusableFunctions import  *

def ArkPRO(s:str, m:str):
    text_list = replace_outside_quotes(s, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    return f'{text_list[0]}\n# UI_start\n{compilation(replace_outside_quotes(text_list[1], [["if", "if_UIComponent"]]), m)}'
def compilation(input_str:str, m:str="into"):
    try:
        def find_UIComponent(text: str) -> str:
            for i in find_lines_with_text_outside_quotes(text, ") {"):
                if not find_lines_with_text_outside_quotes(i, ","):
                    return i
            return ""
        while find_UIComponent(input_str):
            UIComponent_quote = find_UIComponent(input_str)
            input_str = input_str.replace(UIComponent_quote, "," + replace_outside_quotes(UIComponent_quote, [[" ", ""]]), 1)
        input_str_sign_dic = [["{", ".add_child("], ["}", ")"], [" ", ""], ["\n", ""], ["(,", "("]]
        return f"html={replace_outside_quotes(input_str, input_str_sign_dic)[1:]}.render()"
    except:
        if m == "into":
            return ark.ark(input_str, "into")
        else:
            sys.exit("""ArkPRO版OleanderUI渲染出现错误
    ark version OleanderUI rendering error""")