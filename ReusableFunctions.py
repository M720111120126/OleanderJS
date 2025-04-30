import re, base64, filetype
from urllib.parse import quote_plus


def file_to_data_url(file_path):
    mime_type = filetype.guess(file_path)
    if mime_type is None:
        mime_type = "application/octet-stream"
    else:
        mime_type = mime_type.mime
    with open(file_path, 'rb') as file:
        file_data = file.read()
        file_data_encoded = base64.b64encode(file_data).decode('utf-8')
        data_url = f"data:{mime_type};base64,{quote_plus(file_data_encoded)}"
    return data_url
def replace_outside_quotes(text: str, sign_dic: list, rule: str = r'(["\']).*?\1', count: int = -1) -> str:
    quoted = []
    def save_quoted(match):
        quoted.append(match.group(0))
        return 'QUOTED_TEXT'
    text_with_placeholders = re.sub(rule, save_quoted, text)
    if sign_dic:
        for i in sign_dic:
            text_with_placeholders = text_with_placeholders.replace(i[0], i[1], count)
    for q in quoted:
        text_with_placeholders = text_with_placeholders.replace('QUOTED_TEXT', q, 1)
    return text_with_placeholders
def find_lines_with_text_outside_quotes(text: str, txt: str) -> list:
    lines = text.splitlines()
    result_lines = []
    for line in lines:
        modified_line = re.sub(r'(["\']).*?\1', '', line)
        if txt in modified_line:
            result_lines.append(line)
    return result_lines