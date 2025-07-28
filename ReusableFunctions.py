import re, base64, filetype, os
from urllib.parse import quote_plus
from OleanderJsInformation import OleanderJS_project_path

def str_encrypt(text: str) -> str:
    return str(int.from_bytes(text.encode('utf-8'), byteorder='big')).translate(str.maketrans("0123456789", "abcdefghij"))
def str_decrypt(text:str):
    decoded_text = text.translate(str.maketrans("abcdefghij", "0123456789"))
    integer_rep = int(decoded_text)
    byte_length = (integer_rep.bit_length() + 7) // 8
    return integer_rep.to_bytes(byte_length, byteorder='big').decode('utf-8')
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
def get_all_subclasses(cls: type) -> list:
    subclasses = []
    for subclass in cls.__subclasses__():
        subclasses.append(subclass)
        subclasses.extend(get_all_subclasses(subclass))
    return subclasses
def compare_versions(version1, version2):
    v1_parts = list(map(int, version1.split('.')))
    v2_parts = list(map(int, version2.split('.')))
    max_length = max(len(v1_parts), len(v2_parts))
    v1_parts += [0] * (max_length - len(v1_parts))
    v2_parts += [0] * (max_length - len(v2_parts))
    for v1, v2 in zip(v1_parts, v2_parts):
        if v1 > v2:
            return 1
        elif v1 < v2:
            return 2
    return 0
def path(file_path):
    return os.path.join(OleanderJS_project_path, "APP_Scope", file_path.split(": ")[0].replace("$", ""), file_path.split(": ")[1])
