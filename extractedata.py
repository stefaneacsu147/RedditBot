import requests
import bs4
from bs4 import BeautifulSoup

xkcd_id = 1024

url = 'http://www.explainxkcd.com/wiki/index.php/' + str(xkcd_id)

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')


def main():
    tag = soup.find('p')
    data = ''
    while True:
        if isinstance(tag, bs4.element.Tag):
            if (tag.name == 'h2'):
                break
            if (tag.name == 'h3'):
                tag = tag.nextSibling
            else:
                data = data + '\n' + tag.text
                tag = tag.nextSibling
        else:
            tag = tag.nextSibling
    print (data)


if __name__ == '__main__':
    main()