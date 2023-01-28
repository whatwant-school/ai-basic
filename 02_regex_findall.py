import re
import urllib.request

if __name__ == '__main__':

    url = "http://www.itemmania.com/notice/view.html?pub=PORTAL&type=all&nowPage=1&id=1542"
    html = urllib.request.urlopen(url)
    html_contents = str(html.read())

    id_results = re.findall(r"([A-Za-z0-9]+\*\*\*)", html_contents)

    for result in id_results:
        print(result)
