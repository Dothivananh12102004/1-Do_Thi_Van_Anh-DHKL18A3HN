import xml.dom.minidom 
def main(): 
    doc=xml.dom.minidom.parse("sample.xml"); 
    print(doc.nodeName) 
    print(doc.firstChild.tagName)
    company_name = doc.getElementsByTagName("name")[0].firstChild.data
    print("Tên công ty:", company_name) 
if __name__=="__main__": 
    main()