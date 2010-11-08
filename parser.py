import sys
import xml.parsers.expat

from optparse import OptionParser

class Parser(object):
    def __init__(self, path, output_path):
        self.parser = xml.parsers.expat.ParserCreate()
        self.parser.buffer_text = True
        self.parser.returns_unicode = True

        self.output_path = output_path

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
            id = u"".join(self.id).encode("utf-8").strip()
            title = u"".join(self.title).encode("utf-8").strip()
            content = u"".join(self.text).encode("utf-8").strip()

            with open("out/" + title + ".xml", "w") as fh:
                fh.write(content)

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

    def build_output_path(self, title):
        '''return the complete path using the base output path'''
        return os.path.join(self.output_path, title + ".xml")

def main():
    '''main function when called from the command line'''
    options, args = parse_options()

    Parser(open(options.xml), options.outputdir)

def parse_options():
    '''parse and return command line options'''
    parser = OptionParser()
    parser.add_option("-x", "--xml", dest="xml", default="eswiki.xml",
                      help="read xml input FILE", metavar="FILE")
    parser.add_option("-o", "--outputdir", dest="outputdir", default="out",
                      help="write files to DIR", metavar="DIR")

    return parser.parse_args()

if __name__ == '__main__':
    main()

