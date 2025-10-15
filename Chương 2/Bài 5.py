import xml.dom.minidom 
def main(): 
   doc = xml.dom.minidom.parse("sample.xml"); 
   staff= doc.getElementsByTagName("staff") 
   print("%d staff:" % staff.length) 
   for i in staff:
    staff_id= i.getAttribute("id")
    name= i.getElementsByTagName("name")[0].firstChild.data
    salary= i.getElementsByTagName("salary")[0].firstChild.data
    print(f" - ID: {staff_id}, Tên: {name}, Lương: {salary}")
if __name__=="__main__": 
   main()