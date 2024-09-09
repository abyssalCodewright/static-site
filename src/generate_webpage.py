import os
from pathlib import Path
from markdown_blocks import markdown_to_html_node

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.strip()
        if line == "":
            continue
        if line.startswith("# "):
            return line[2:]
        raise Exception("No H1 found")
    

def generate_page_recursive(dir_path_content, template_path, dest_dir_path):

    for item in os.listdir(dir_path_content):
        if item.endswith(".md"):
            generate_page(f'{dir_path_content}/{item}', template_path, f'{dest_dir_path}/{item[:-3]}.html')
        else:
            os.makedirs(f'{dest_dir_path}/{item}')
            generate_page_recursive(f'{dir_path_content}/{item}', template_path, f'{dest_dir_path}/{item}')


def generate_page(from_path, template_path, dest_path):
    print(f"Generating path from {from_path} to {dest_path} using {template_path}...")

    m = open(from_path, 'r')
    t = open(template_path, 'r')
    md_contents = m.read()
    m.close()
    template_contents = t.read()
    t.close()

    html_contents = markdown_to_html_node(md_contents).to_html()

    title = extract_title(md_contents)

    webpage = template_contents.replace("{{ Title }}", title)
    webpage = webpage.replace("{{ Content }}", html_contents)

    file_path = os.path.join(dest_path)
    with open(file_path, 'w') as file:
        file.write(webpage)