import requests
from math import ceil

proxy_link = str(input('Geonode Proxies link\n>>> '))

if proxy_link[51] == '5':
	link = proxy_link[:51] + '200' + proxy_link[53:] ## Correcting 2-digit limits
else:
	link = proxy_link

## Total Proxy Count.
total = requests.get(link).json()['total']

## Proxy limit in each page.
## 50, 100, 150, 200
limit = int(requests.get(link).json()["limit"])

page_count = int(ceil(total/limit))

## IP:PORT Format
for n in range(1, page_count+1):
    r = requests.get(f'https://proxylist.geonode.com/api/proxy-list?limit={limit}&page={n}{link[61:]}')
    with open('geonode_proxies.txt', 'a') as f:
        for DICTedData in r.json()["data"]: f.write(f'{DICTedData["ip"]}:{DICTedData["port"]}\n')

## {"PROTOCOL":"'IP':'PORT'"} Format
## Uncomment the lines 28-37 to scrape in dictionary/JSON format.
## Don't forget to comment lines 19-22 if using this

#with open('geonode_proxies.txt', 'a') as f:
#    f.write('{\n')
#
#for n in range(1, page_count+1):
#    r = requests.get(f'https://proxylist.geonode.com/api/proxy-list?limit={limit}&page={n}{link[61:]}')
#    with open('geonode_proxies.txt', 'a') as f:
#        for DICTedData in r.json()["data"]: f.write(f'\t\t"{DICTedData["protocols"][0]}": "{DICTedData["ip"]}:{DICTedData["port"]}",\n')
#
#with open('geonode_proxies.txt', 'a') as f:
#    f.write('}\n')

input("\nFinished scraping proxies!\nPress ENTER to exit.")
