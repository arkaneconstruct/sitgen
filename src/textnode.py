class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, object):
        if (self.text == object.text and
            self.text_type == object.text_type and
            self.url == object.url):
            return True
    
    def __repr__(self):
        x = f"TextNode({self.text}, {self.text_type}, {self.url})"
        return x