from textnode import TextNode
from htmlnode import HTMLNode

def main():
    node = HTMLNode("a", "no words", None, {"href": "https://www.google.com", "target": "_blank"})
    fixed_props = node.props_to_html()
    print(fixed_props)

main()