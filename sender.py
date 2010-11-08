import os
import glob
import urllib
import httplib
import logging
from optparse import OptionParser

logging.basicConfig(filename="sender.log", level=logging.DEBUG)

class SenderException(Exception):
    """
    A class declared just to bother you
    """
    pass


class HTTPSender(object):
    """
    this class is legend... wait for it..

    ..dary, LEGENDARY!
    """

    def __init__(self, host, uri, path, port=80):
        """
        My *AWESOME* constructor
        """

        self.host = host
        self.path = path
        self.uri = uri
        self.port = int(port)

    def get_xml_files(self, path):
        """
        returns all the xml files in the given path
        """

        return glob.glob("%s/*.xml" % path)

    def send_file(self, filename):
        """
        Receives a filename and performs an HTTP Query against the server
        Creates an html file with the same name as the received and
        stores there the response from the server.

        If it doesn't like the server response, it raises a
        SenderException and poops the party for everyone

        """

        logging.debug("send_file(%s) " % filename)

        result_name, result_ext = os.path.splitext(filename)
        result_name += ".html"

        origin_file = open(filename)
        origin_data = origin_file.read()
        origin_file.close()

        headers = {"Content-type": "text/plain",
                   "Accept": "text/html"}

        conn = httplib.HTTPConnection(self.host, self.port)
        conn.request("POST", self.uri, origin_data, headers)

        response = conn.getresponse()

        if response.status == 200:
            result_file = open(result_name, "w")
            result_file.write(response.read())
            result_file.close()

            return True
        else:
            raise SenderException(response.reason)

    def run(self):
        """
        Runs sequentially a file list against send_file

        may be interrupted by a SenderException :(
        (lets try not to)
        """
        map(self.send_file, self.get_xml_files(self.path))
        return True


def main():
    options, args = parse_options()

    HTTPSender(options.host, options.uri, options.path,
               options.port).run()

def parse_options():
    """parse and return command line options"""
    parser = OptionParser()
    parser.add_option("-H", "--host", dest="host",
                      help="mediawiki host", metavar="HOST")
    parser.add_option("-u", "--uri", dest="uri", default="/mediawiki/dumper.php",
                      help="URI for the parser file", metavar="URI")
    parser.add_option("-p", "--port", dest="port", default=80,
                      help="port for the mediawiki", metavar="PORT")
    parser.add_option("-o", "--path", dest="path", default="out",
                      help="path to the given XML files", metavar="PATH")


    return parser.parse_args()

if __name__ == "__main__":

    main()
