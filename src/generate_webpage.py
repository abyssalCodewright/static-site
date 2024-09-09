import os
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