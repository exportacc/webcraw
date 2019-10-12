# -*- coding: utf-8 -*-
import scrapy
# from bs4 import BeautifulSoup
# import requests as rq
# import pandas as pd
from db.items import DbItem
# from datetime import datetime
# import time


class YahooSpider(scrapy.Spider):
    name = 'yahoo'
    allowed_domains = ['yahoo.com']
    '''
    start_urls = [i.strip() for i in open('url.txt').readlines()]
    print(start_urls)
    '''
    start_urls = ['https://finance.yahoo.com/quote/2330.TW/history?period1=968515200&period2=1568044800&interval=1d&filter=history&frequency=1d']
    # call back collection using parse function
    def parse(self, response):
        rows = response.css('tr.BdT')
        # df = pd.DataFrame({'date': {}, 'open': {}, 'high': {}, 'low': {}, 'close': {}, 'volume': {}})
        for t in rows:
            item = DbItem()
            try:
                item['date'] = t.css('td')[0].css('span::text').extract_first()
                '''
                string transaction to datetime %B Mon %d day %Y Year
                '''
            except ValueError:
                item['date'] = float('nan')
            except IndexError:
                item['date'] = float('nan')
            try:
                item['open'] = float(t.css('td')[1].css('span::text').extract_first())
            except IndexError:
                item['open'] = float('nan')
            except ValueError:
                item['open'] = float('nan')
            try:
                item['high'] = float(t.css('td')[2].css('span::text').extract_first())
            except IndexError:
                item['high'] = float('nan')
            except ValueError:
                item['high'] = float('nan')
            try:
                item['low'] = float(t.css('td')[3].css('span::text').extract_first())
            except IndexError:
                item['low'] = float('nan')
            except ValueError:
                item['low'] = float('nan')
            try:
                item['close'] = float(t.css('td')[4].css('span::text').extract_first())
            except IndexError:
                item['close'] = float('nan')
            except ValueError:
                item['close'] = float('nan')
            '''
            return [5] >> adjust close , same as close 
            '''
            try:
                item['volume'] = float(t.css('td')[6].css('span::text').extract_first().replace(',', ''))
                '''
                , >> not space and transaction to float
                '''
            except IndexError:
                item['volume'] = float('nan')
            yield item
        print('>> spider finished')