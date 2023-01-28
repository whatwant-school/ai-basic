from bs4 import BeautifulSoup

if __name__ == '__main__':
    with open("02_patent.xml", "r", encoding="utf8") as patent_xml:
        xml = patent_xml.read()

    soup = BeautifulSoup(xml, "xml")

    invention_title_tag = soup.find("invention-title")
    print(invention_title_tag.get_text())

    publication_reference_tag = soup.find("publication-reference")
    p_document_id_tag = publication_reference_tag.find("document-id")
    p_country = p_document_id_tag.find("country").get_text()
    p_doc_number = p_document_id_tag.find("doc-number").get_text()
    p_kind = p_document_id_tag.find("kind").get_text()
    p_date = p_document_id_tag.find("date").get_text()
    print(p_doc_number, p_kind, p_date)

    application_reference_tag = soup.find("application-reference")
    a_document_id_tag = publication_reference_tag.find("document-id")
    a_country = p_document_id_tag.find("country").get_text()
    a_doc_number = p_document_id_tag.find("doc-number").get_text()
    a_date = p_document_id_tag.find("date").get_text()
    print(a_country, a_doc_number, a_date)
