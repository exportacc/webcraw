# -*- coding: utf-8 -*-
import scrapy
import pandas as pd

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['yahoo']
    start_urls = ['https://www.fairfaxcounty.gov/FIDO/complaints/comp_display.aspx?type=sr&servno=3679']

    def parse(self, response):
        ''' 分析報告
        td::text ， inside text from td
        '''
        rows = response.css('table.tbBorder tr')
        df = pd.DataFrame({'A': {}, 'B':{}})
        for row in rows :
            df = df.append({'A':row.css('td::text').extract_first(),
                            'B':row.css('td')[1].css('span::text').extract_first()},
                           ignore_index=True)
        print(df)
