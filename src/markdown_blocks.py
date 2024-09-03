block_type_paragraph = "paragraph"
block_type_code = "code"
block_type_heading = "heading"
block_type_quote = "quote"
block_type_ulist = "unordered_list"
block_type_olist = "ordered_list"


def markdown_to_blocks(markdown):
    lines = markdown.split("\n\n")
    blocks = []

    for line in lines:
        if line == "":
            continue
        line = line.strip()
        blocks.append(line)

    return blocks


def block_to_block_type(markdown_block):
    lines = markdown_block.split("\n")
    
    if (
        markdown_block.startswith("# ")
        or markdown_block.startswith("## ")
        or markdown_block.startswith("### ")
        or markdown_block.startswith("#### ")
        or markdown_block.startswith("##### ")
        or markdown_block.startswith("###### ")
    ):
        return block_type_heading
        
    if all(line.startswith(">") for line in lines):
        return block_type_quote
    if all(line.startswith("* ") for line in lines):
        return block_type_ulist
    if all(line.startswith("- ") for line in lines):
        return block_type_ulist
    
    if markdown_block.startswith("```") and markdown_block.endswith("```"):
        return block_type_code
    
    if markdown_block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_olist
        
    return block_type_paragraph