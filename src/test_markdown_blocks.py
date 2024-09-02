import unittest
from markdown_blocks import markdown_to_blocks

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