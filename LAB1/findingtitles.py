import urllib.request
from bs4 import BeautifulSoup

wikiURL = "https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"
fpURL = urllib.request.urlopen(wikiURL)


soup = BeautifulSoup(fpURL, "html.parser")


title = soup.find('title')
print("Title --> ", title.text)


tables=soup.find_all('table')
right_table=soup.find('table', {"class":'wikitable sortable plainrowheaders'})
outF = open("output.txt", "w")
print("states")
for line in right_table:
  outF.write(str(line))
outF.close()