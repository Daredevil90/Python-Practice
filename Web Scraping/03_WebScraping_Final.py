import pandas as pd
import requests
from bs4 import BeautifulSoup
# import warnings
#  Ignore all warnings
# warnings.filterwarnings("ignore", category=FutureWarning)
#  url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
#  data = requests.get(url).text
# data2=BeautifulSoup(data,"html.parser")
# data = pd.read_html(url)
#  d1= data[0]
#  print(d1[["Date","Open","High","Low","Close*","Volume"]].head(1))
url="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/amazon_data_webpage.html"
html_data =requests.get(url).text
d1= BeautifulSoup(html_data,"html.parser")
print(d1.title)
amazon_data = pd.DataFrame(columns=["Date", "Open", "High", "Low", "Close", "Volume"])
table_rows=d1.find("tbody").find_all("tr")
for x in table_rows:
      col=x.find_all("td")
      date=col[0].text
      open=col[1].text
      high=col[2].text
      low=col[3].text
      close=col[4].text
      vol=col[6].text
      amazon_data = pd.concat([amazon_data, pd.DataFrame({"Date":[date], "Open":[open], "High":[high], "Low":[low], "Close":[close],  "Volume":[vol]})], ignore_index=True)
print(amazon_data.tail(1))