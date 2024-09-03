import unittest
from markdown_blocks import markdown_to_blocks, block_to_block_type
from markdown_blocks import (
    block_type_olist,
    block_type_code,
    block_type_heading,
    block_type_paragraph,
    block_type_quote,
    block_type_ulist
)

class TestMarkdownToBlocks(unittest.TestCase):
    def test_does_it_work(self):
        markdown_text = """
# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""

        node = markdown_to_blocks(markdown_text)
        enode = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", "* This is the first list item in a list block\n* This is a list item\n* This is another list item"]
        self.assertListEqual(node, enode)


    def test_white_space(self):
        mdown = """
# This is a heading



This is a paragraph."""
        node = markdown_to_blocks(mdown)
        enode = ["# This is a heading", "This is a paragraph."]
        self.assertListEqual(node, enode)


    def test_blocktype_heading(self):
        script = "### This is a heading of three"
        self.assertEqual(block_to_block_type(script), block_type_heading)


    def test_blocktype_code(self):
        script = "```This is a code block.```"
        self.assertEqual(block_to_block_type(script), block_type_code)


    def test_blocktype_quote(self):
        script = ">This is a quote"
        self.assertEqual(block_to_block_type(script), block_type_quote)


    def test_blocktype_paragraph(self):
        script = "Ain't nobody here but us paragraphs."
        self.assertEqual(block_to_block_type(script), block_type_paragraph)


    def test_blocktype_unordered_list(self):
        script = """
* This is an unordered list with an asterisk
* Another item in list

- This is an unordered list with a dash
- Another item in this list"""
        node = markdown_to_blocks(script)
        asterisk_block = block_to_block_type(node[0])
        dash_block = block_to_block_type(node[1])
        self.assertEqual(asterisk_block, block_type_ulist)
        self.assertEqual(dash_block, block_type_ulist)


    def test_blocktype_ordered_list(self):
        script = """
1. first item
2. second item
3. third item"""
        node = markdown_to_blocks(script)
        self.assertEqual(block_to_block_type(node[0]), block_type_olist)


    def test_not_heading_blocktype(self):
        script = "######## This is an incorrect heading"
        self.assertEqual(block_to_block_type(script), block_type_paragraph)


    def test_not_quote_blocktype(self):
        script = """
>This is the beginning of the quote
but this line is wrong
>so this should be a paragraph"""
        node = markdown_to_blocks(script)
        self.assertEqual(block_to_block_type(node[0]), block_type_paragraph)


    def test_not_ordered_list_blocktype(self):
        script = """
1. this is number one
5. this is not number two
3. this is number 3"""
        node = markdown_to_blocks(script)
        self.assertEqual(block_to_block_type(node[0]), block_type_paragraph)