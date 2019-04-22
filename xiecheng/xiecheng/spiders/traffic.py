import requests
from lxml import etree


def Get_traffic(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
    }
    response = requests.get(url=url,headers=headers)

    html = etree.HTML(response.text)

    traffic = html.xpath('//div[@class="text_style"]/text()')
    if len(traffic) <=0:
        traffic = 'None'
    else:
        traffic = html.xpath('//div[@class="text_style"]/text()')[0].replace('\r\n','').replace('\n\r\n','').replace(' ','').replace('\n','')

    return traffic
