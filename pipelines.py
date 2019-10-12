# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo as py
import db.settings as st


class DbPipeline(object):
    def __init__(self):
        # host = settings['MONGODB_HOST']
        host = st.stuff['Mongodb_host']
        # port = settings['MONGODB_PORT']
        port = st.stuff['Mongodb_port']
        # db_name = settings['MONGODB_DB']
        db_name = st.stuff['Mongodb_db']
        # db_post = settings['MONGODB_DOC']
        db_post = st.stuff['Mongodb_doc']
        client = py.MongoClient(host=host, port=port)
        # client = py.MongoClient('mongodb://localhost:27017/')
        db = client[db_name]
        # data base >> db_name
        self.post = db[db_post]
        # collection table >>

    def process_item(self, item, spider):
        person_info = dict(item)
        self.post.insert(person_info)
        return item
