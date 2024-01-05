from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import pandas as pdp

# Reading file of episode names


# opening the file in read mode
my_file = open("Episode Title.txt", "r")

# reading the file
data = my_file.read()

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.split("\n")

# printing the data
print(data_into_list)
my_file.close()

#  Define the target URL
my_url = "https://kingofthehill.fandom.com/wiki/"

# Create csv file
filename = "koth_data.csv"
f = open(filename, "w")

headers = "Episode Name, Release Date, Wiki Link \n"
f.write(headers)

# Loop through textfile of episode names to scrape data from each page
for n in data_into_list:
    pageName = "".join([my_url,n])
    # print(pageName + '\n')
    # Fetch the HTML Content
    uClient = uReq(pageName)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")
    Episode_Name = page_soup.select('h2.pi-item')
    Air_Date = page_soup.select('div.pi-item:nth-child(4) > div:nth-child(2)')
    try:
        f.write('"' + Episode_Name[0].text + '"' + "," + '"' +Air_Date[0].text + '"' + "," + pageName + "\n")
        # print(Episode_Name[0].text)
        # print(Air_Date[0].text)
    except:
        print("End of list")
f.close()
