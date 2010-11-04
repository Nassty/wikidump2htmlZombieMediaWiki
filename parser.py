import sys
import xml.parsers.expat

class Parser(object):
    def __init__(self, path):
        self.parser = xml.parsers.expat.ParserCreate()
        self.parser.buffer_text = True
        self.parser.returns_unicode = True

        self.in_page = False
        self.in_revision = False
        self.current_tag = ''
        self.title = None
        self.id = None
        self.text = None

        #connect handlers
        self.parser.StartElementHandler = self.start_element
        self.parser.EndElementHandler = self.end_element
        self.parser.CharacterDataHandler = self.char_data

        self.parser.ParseFile(path)

    def start_element(self, name, attrs):
        '''Start xml element handler'''
        if name == "page":
            self.in_page = True
            self.text = []
            self.id = []
            self.title = []
        elif name == "revision":
            self.in_revision = True

        self.current_tag = name

    def end_element(self, name):
        '''End xml element handler'''
        if name == "page":
            self.in_page = False
            print "id", u"".join(self.id).encode("utf-8")
            print "title", u"".join(self.title).encode("utf-8")
            print u"".join(self.text)[:20].encode("utf-8")
            print "-" * 79
        elif name == "revision":
            self.in_revision = False

    def char_data(self, data):
        '''Char xml element handler'''
        if not self.in_page or self.in_revision:
            if self.current_tag == "text":
                self.text.append(data)
            return

        if self.current_tag == "title":
            self.title.append(data)
        elif self.current_tag == "id":
            self.id.append(data)


if __name__ == '__main__':
    Parser(open(sys.argv[1]))

