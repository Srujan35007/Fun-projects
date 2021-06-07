from bs4 import BeautifulSoup as BS 
from tqdm import tqdm 
import requests
import time

url = 'https://lite.ip2location.com/ip-address-ranges-by-country'
soup = BS(requests.get(url).content, 'html.parser')

links = []
for foo in soup.find_all('a'):
    if 'ip-address-ranges' in foo['href'] and '/ip-address-ranges-by-country' not in foo['href']:
        country = str(foo).split('>')[-2].replace('</a', '').lower().title()
        link = 'https://lite.ip2location.com' + foo['href']
        links.append((country, link))

links.sort()
bef = time.time()
count = 0
with open('./All_IPs.csv', 'a') as writeFile:
    writeFile.write('Country,StartingIP,EndingIP,NumberOfIPs\n')
    for idx, link in enumerate(links):
        print(f'\nProcessing {link[0]} ({idx}/{len(links)}) country.')
        soup = BS(requests.get(link[1]).content, 'html.parser')
        for foo in soup.find_all('tr'):
            if 'begin ip address' not in str(foo).lower():
                raw = str(foo).split('\n')
                from_IP = raw[1].split('>')[1].replace('</td', '')
                to_IP = raw[2].split('>')[1].replace('</td', '')
                num_IPs = raw[3].split('>')[-2].replace('</td', '').replace(',','')
                writeFile.write(f'{link[0]},{from_IP},{to_IP},{num_IPs}\n')
                count += 1
            else:
                pass
        print(f'{link[0]} - Done - {count} upto now - {round((time.time()-bef)/60, 2)} Min. elapsed.\n')
