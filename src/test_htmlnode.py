import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):

    def test_none(self):
        dictx = {}
        node = HTMLNode(props=dictx)
        print("Test 1:" + str(node.props_to_html()))

    def test_single(self):
        dictx = {"href":"https://www.google.com"}
        node = HTMLNode(props=dictx)
        print("Test 2:" + str(node.props_to_html()))

    def test_multi(self):
        dictx = {"href":"https://www.google.com", "target":"_blank",}
        node = HTMLNode(props=dictx)
        print("Test 3:" + str(node.props_to_html()))

class TestLeafNode(unittest.TestCase):

    def test_no_val(self):
        with self.assertRaises(ValueError):
            node = LeafNode()
            node.to_html()
    
    def test_no_tag(self):
        node = LeafNode(value="Hello world.")
        self.assertIsInstance(node.to_html(),str)

    def test_pos(self):
        dictx = {"href":"https://www.google.com", "target":"_blank",}
        node = LeafNode(tag="a", value="Navigate to Google", props=dictx)
        print("Leaf Pos Test: " + str(node.to_html()))

if __name__ == "__main__":
    unittest.main()