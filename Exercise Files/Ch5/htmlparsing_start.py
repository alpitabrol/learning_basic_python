# 
# Example file for parsing and processing HTML
#
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
  def handle_starttag(self, tag,attrs):

    print(tag)



def main():
  # instantiate the parser and feed it some HTML
  parser = MyHTMLParser()
  f= open("samplehtml.html")
  parser.feed(f.read())
  
if __name__ == "__main__":
  main();
  