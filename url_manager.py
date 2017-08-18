# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:09:02 2017

@author: 祝晓泉
"""

class UrlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    
#    向管理器中添加一个新的URL
    def add_new_url(self, url):
        if url is None:
            return
        else:
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)
    
#    判断是否有新的URL
    def has_new_url(self):
        return len(self.new_urls) != 0
    
#    从管理器中获取一个新的URL
    def get_new_url(self):
        new_url = self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
    
#    向管理器中添加批量URL
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        else:
            for url in urls:
                self.add_new_url(url)
    