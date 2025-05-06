import json
import os
import datetime

def file_exists(output_path: str) -> str | None:
    """ Checks if output file already and extends it's name with current timer

    Args:
        output_path (str): generated file path

    Returns:
        str | None: new path | nothing
    """

    if os.path.exists(output_path):
        current_datetime: str = datetime.datetime.now().strftime("%H_%M_%S_%f")[:-3]  # Remove milliseconds
        new_path:str = output_path + '_' + current_datetime + '.txt'
        return new_path
    else:
        return None

def json_to_xml(json_obj, indent=""):
    """ Recursively converts JSON to XML string with each tag on its own line/

    Args:
        json_obj: JSON data
        indent (str, optional): Defaults to "".

    Returns:
        XML data to be written in a new file.
    """

    result_list = []

    if isinstance(json_obj, dict):
        for tag_name, sub_obj in json_obj.items():
            if "$" in tag_name:
                continue  # Skip tags with <$>
            result_list.append(f"{indent}<{tag_name}>{json_to_xml(sub_obj, indent)}</{tag_name}>")
    elif isinstance(json_obj, list):
        for sub_obj in json_obj:
            result_list.append(json_to_xml(sub_obj, indent))
    else:
        return str(json_obj)

    return "\n".join(result_list)

def add_prefix(xml_file, prefix: str) -> None:
    import re
    with open(xml_file,'r', encoding='utf-8') as f:
        lines: list[str] = f.readlines()
    
    updated_lines: list[str] = []
    for line in lines:
        # Replace </ with </prof: and < with <prof:, but avoid double-replacing
        line: str = re.sub(r'</(\w+)', fr'</{prefix}:\1', line)
        line = re.sub(r'<(\w+)', fr'<{prefix}:\1', line)
        updated_lines.append(line)
    
    with open(xml_file, 'w', encoding='utf-8') as f:
        f.writelines(updated_lines)


def prepare_n_write(json_path:str, prefix: str) -> str:
    """ main function of the script

    Args:
        json_path (str): User's JSON file path.
        prefix (str): User's desired prefix to be added.

    Returns:
        str: Generated file's path.
    """
    # Load JSON from file
    with open(json_path, "r") as json_file:
        json_data = json.load(json_file)

    xml_string = json_to_xml(json_data, indent="")

    # Save to XML file
    output_file:str = "output.txt"
    check_file: str | None = file_exists(output_file)
    if check_file:
        output_file = check_file


    with open(output_file,'w', encoding='utf-8') as xm_file:
        xm_file.write(xml_string)
        
    if prefix.__len__() > 0:
        add_prefix(output_file, prefix)

    return output_file

# if __name__ == '__main__':
#     prepare_n_write()
