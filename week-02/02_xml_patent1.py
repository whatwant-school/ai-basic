from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("02_patent.xml", "r", encoding="utf8") as patent_xml:
        xml = patent_xml.read()

    soup = BeautifulSoup(xml, "lxml")

    invention_title_tag = soup.find("invention-title")
    print(invention_title_tag.get_text())
