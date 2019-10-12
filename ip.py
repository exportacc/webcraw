# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

'''
測試代理ip是否有轉換成功 
'''
class IpSpider(scrapy.Spider):
    name = 'ip'
    allowed_domains = ['whatismyip.com']
   #  start_urls = ('https://whatismyipaddress.com/',
   #  'https://whatismyipaddress.com/',
   #  'https://whatismyipaddress.com/',
   # 'https://whatismyipaddress.com/',
   # 'https://whatismyipaddress.com/',
   #  )
    start_urls = ['http://checkip.amazonaws.com/','http://checkip.amazonaws.com/','http://checkip.amazonaws.com/']

    def parse(self, response):
        '''
         print(' ip address -> %s '%(response.css('#ipv4 a')[0].css('a::text').get()))
        print('')
        rows = response.css('table')[0].css('tr')
        df = pd.DataFrame({'title': {}, 'context': {}})
        for row in rows:
            x = row.css('th::text').get()
            # print(x)
            y = row.css('td::text').get()
            # print(y)
            df = df.append({'title': x, 'context': y}, ignore_index=True)
        print(df)
        '''
        print(response.body.decode())
        # pass


