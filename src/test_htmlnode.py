import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_repr_works(self):
        node = HTMLNode("p", "This is a paragraph.", None, {"href": "www.blizzard.com"})
        expect = "HTMLNode(p, This is a paragraph., children: None, {'href': 'www.blizzard.com'})"
        self.assertEqual(repr(node), expect)

    def test_props_to_html_works(self):
        props = HTMLNode("p", "text string", None, {"href": "www.blizzard.com"})
        expect = ' href="www.blizzard.com"'
        self.assertEqual(props.props_to_html(), expect)

    def test_props_to_html_twice(self):
        props = HTMLNode("p", "text string", None, {"href": "www.blizzard.com", "target": "_blank"})
        expect = ' href="www.blizzard.com" target="_blank"'
        self.assertEqual(props.props_to_html(), expect)

    def test_all_none(self):
        node = HTMLNode()
        expect = "HTMLNode(None, None, children: None, None)"
        self.assertEqual(repr(node), expect)

    def test_values(self):
        node = HTMLNode("div", "Eff you, I can read and write, too.")
        self.assertEqual(node.tag, "div")
        self.assertEqual(node.value, "Eff you, I can read and write, too.")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, None)



if __name__ == "__main__":
    unittest.main()