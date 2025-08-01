import sys
import dependencies.ArkOfObject as ark
from dependencies.ReusableFunctions import  *

def ArkPRO(s: str, m: str, UIComponent_Subclasses: list[type]) -> str:
    text_list = replace_outside_quotes(s, [["# UI_start", "§⁋•“௹"]]).split("§⁋•“௹")
    return f'{text_list[0]}\n# UI_start\n{compilation(replace_outside_quotes(text_list[1], [["if", "if_UIComponent"]]), UIComponent_Subclasses, m)}'
def compilation(input_str: str, UIComponent_Subclasses: list[type], m: str="into") -> str:
    try:
        for UIComponent_Subclasse in UIComponent_Subclasses:
            UIComponent_Subclasse = UIComponent_Subclasse.__name__
            for UIComponent_Subclasse_quote in find_lines_with_text_outside_quotes(input_str, UIComponent_Subclasse):
                if not find_lines_with_text_outside_quotes(UIComponent_Subclasse_quote, "{"):
                    UIComponent_Subclasse_quote_new = replace_outside_quotes(UIComponent_Subclasse_quote, [[")", "§⁋•“௹"]])
                    input_str = input_str.replace(UIComponent_Subclasse_quote, UIComponent_Subclasse_quote_new)
        input_str = replace_outside_quotes(input_str, [["§⁋•“௹", ") {}"]])
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