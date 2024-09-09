import unittest
from generate_webpage import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_get_heading(self):
        md = "    # This is a heading with some whitespace    "
        node = extract_title(md)
        enode = "This is a heading with some whitespace"
        self.assertEqual(node, enode)

    
    def test_no_heading_found(self):
        md = "This is not a heading"
        with self.assertRaises(Exception) as context:
            extract_title(md)
        self.assertEqual(str(context.exception), "No H1 found")