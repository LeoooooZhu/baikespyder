# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 15:09:54 2017

@author: 祝晓泉
"""

import urllib

class HtmlDownloader(object):
    
    def download(self, url):
        if url is None:
            return None
        
        resp = urllib.request.urlopen(url)
        
        if resp.getcode() != 200:
            print("acess error")
            return None
        
        return resp.read().decode('utf-8')
        