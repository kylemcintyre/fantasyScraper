import requests
from bs4 import BeautifulSoup

# get the data from source website
data = requests.get('https://www.fantasypros.com/nfl/rankings/ros-dst.php')

# load data into bs4
soup = BeautifulSoup(data.text, 'html.parser')

# set ranks variable to proper table and set tbody
ranks = soup.find('table', {'id': 'rank-data'})
tbody = ranks.find('tbody')

# loop to scan tr elements for td elements assign:
# team rank, name, best rank, worst rank
for tr in tbody.find_all('tr'):
    rank = tr.find_all('td')[0].text.strip()
    name = tr.find_all('td')[2].text.split("(", 1)[0].rstrip()
    best = tr.find_all('td')[4].text.strip()
    worst = tr.find_all('td')[5].text.strip()
    
    # print (rank, name, best, worst)
    
    # create file and write results to it
    f = open('dstdata.txt', 'a')
    f.write(rank + " " + name + " " + best + " " + worst + '\n')
    f.close()
