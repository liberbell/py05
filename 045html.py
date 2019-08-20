from html.parser import HTMLParser

class HTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('start tag: ', tag)
        for attr in attrs:
            print('attr:', attr)
    def handle_endtag(self, tag):
        print('End tag:', tag)
