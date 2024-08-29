import unittest
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node


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

class TestParentNode(unittest.TestCase):
    def test_no_tag(self):
        with self.assertRaises(ValueError):
            dictx = {"href":"https://www.google.com", "target":"_blank",}
            child_node = LeafNode(tag="a", value="Navigate to Google", props=dictx)
            node = ParentNode(children=[child_node])
            node.to_html()

    def test_no_child(self):
        with self.assertRaises(ValueError):
            node = ParentNode(tag="p")        
            node.to_html()
    
    def test_many_parents(self):
        leaf1 = LeafNode(None, "Regular text")
        leaf2 = LeafNode("em", "Emphasized text")
        inner_parent = ParentNode("p", [leaf1, leaf2])
        outer_parent = ParentNode("div", [inner_parent])
        result = outer_parent.to_html()
        expected = "<div><p>Regular text<em>Emphasized text</em></p></div>"
        assert result == expected

class TestTextToHTMLNode(unittest.TestCase):
    def invalid_type(self):
        with self.assertRaises(Exception):
            x = TextNode(text="Welcome.",text_type="backflip")
            testNode = text_node_to_html_node(x)
            testNode.to_html()

    def test_text(self):
        x = TextNode(text="Welcome.",text_type="text")
        testNode = text_node_to_html_node(x)
        assert testNode.to_html() == "Welcome."
    
    def test_link(self):
        x = TextNode(text="Welcome.",text_type="link",url="google.com")
        testNode = text_node_to_html_node(x)
        assert testNode.tag == "a" and testNode.props == {"href":x.url}
    
if __name__ == "__main__":
    unittest.main()