# from bs4 import BeautifulSoup
# import requests
# html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
# document= BeautifulSoup(html,"html.parser") 
# print(document)
# print(document.prettify())
# tag_object= document.title
# tag_object1= document.h3
# tag_child= tag_object1.b
# print(tag_child.attrs)
# print("h3:",tag_object1)
# print("title:",tag_object)
# print("Parent Tag:",tag_child.parent)
# print("Child Tag:",tag_child)
# print("Sibling Tag:",tag_object1.next_sibling)
# sibling_1=tag_object1.next_sibling
# sibling_2=sibling_1.next_sibling
# tag_string= tag_child.string
# print("Sibling2:",sibling_2)
# print(tag_child.get("id"))
# print("String contained in:",tag_string)
# print(type(tag_object))
# print("Tag String Type:",type(tag_string))
# table="<table><tr><td id='flight' >Flight No</td><td>Launch site</td><td>Payload mass</td></tr><tr><td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a> </td><td>80 kg</td></tr></table>"
# table_doc= BeautifulSoup(table,"html.parser")
# print(table_doc.prettify())
# table_obj=table_doc.table
# print(table_obj.prettify())
# table_rows=table_obj.find_all("tr")
# print(table_rows)
# for k,i in enumerate(table_rows):
#     print("row no:"+str(k))
#     for j,x in enumerate(i):
#         print("row values["+str(j)+"]: "+str(x))
# print(table_obj.find_all(id="flight"))
# print(table_obj.find_all(href=True))
# #  Downloading Content from a Website
# url = "http://www.ibm.com"
# data = requests.get(url).text
# print(data)
# print(type(data))
# document2= BeautifulSoup(data,"html.parser")
# #  Scrape all Links
# l1=[]
# for x in document2.find_all("a",href=True):
#     l1.append(x.get("href"))
# for x in document2.find_all("img",src=True):
#     print(x.get("src"))
# url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"
# document3= requests.get(url2).text
# doc3= BeautifulSoup(document3,"html.parser")
# for x in doc3.find("table"):
#     print(x)
# print(l1)
# import pandas as pd
# url3 = "https://en.wikipedia.org/wiki/World_population"
# data4=requests.get(url3).text
# doc4= BeautifulSoup(data4,"html.parser")
# tables=doc4.find_all("table")
# print("No. of Tables:",len(tables))
# links=doc4.find_all("a",href=True)
# for x in links:
#     print("Links:",x.get("href"))`
# for idx, table in enumerate(tables):
#     if("10 most densely populated countries" in str(table)):
#         content=table.find_all("tr")
# population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
# for idx,row in enumerate(list(content)):
#     col= row.find_all("td")
#     if (col != []):
#         rank = col[0].text
#         country = col[1].text
#         population = col[2].text.strip()
#         area = col[3].text.strip()
#         density = col[4].text.strip()
#         population_data = population_data._append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)
# print(population_data)
# print(pd.read_html(str(tables[5]),flavor="bs4")[0])
# Dataframe_list= pd.read_html(url3,flavor="bs4")
# print(Dataframe_list[25])
# print(pd.read_html(url3,match="10 most densely populated countries",flavor="bs4")[0])
