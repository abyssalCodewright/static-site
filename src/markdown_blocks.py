def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    blocks = []

    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)

    return blocks