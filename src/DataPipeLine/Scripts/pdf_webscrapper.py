from urllib.request import urlopen, urlretrieve
from urllib.parse import urljoin, quote
import os

Directory='F:/Deeplearning/Datathon-1.0'

from bs4 import BeautifulSoup

url = 'http://www.epid.gov.lk/web/index.php?option=com_content&view=article&id=225&Itemid=518&lang=en'
u = urlopen(url)
try:
    html = u.read().decode('utf-8')
finally:
    u.close()

soup = BeautifulSoup(html)
for link in soup.select('p a'):
    href = link.get('href')
    # print(href)
    if href.startswith('javascript:'):
        continue

    filename = href.rsplit('/', 1)[-1]
    if (filename == 'sitrep-sl-en-30-03_10.pdf'):
        break

    parts = filename.split('-')
    dw_name = parts[4][:2] + '-' + parts[3] + '.pdf'

    #if (parts[1] == 'sl' and parts[2] == 'en' and filename != 'dailyreportcoronavirussin.pdf'):
    #    href = urljoin(url, quote(href))
    #    filepath = urlretrieve(href, './Datathon-1.0/data/daily_pdf/' + dw_name)


    try:
        if (parts[1] == 'sl' and parts[2] == 'en' and filename != 'dailyreportcoronavirussin.pdf'):
            href = urljoin(url, quote(href))

            # print(href)
            #print('../../../data/daily_pdf/'+dw_name)
            #filepath = urlretrieve(href,'./Datathon-1.0/data/daily_pdf/' + dw_name)
            try:
                filepath = urlretrieve(href, Directory + '/data/daily_pdf/' + dw_name)
                print('Sucess :- ', filepath[0], ' created')
            except:
                print('url:- ', href)
                print('date:- ', parts[4][:2] + '-' + parts[3])
                print('failed to download')
    except:
        print(filename)

