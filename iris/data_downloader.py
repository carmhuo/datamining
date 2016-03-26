# -*- coding: utf-8 -*-
'''
Created on 2016年3月16日

@author: carm
'''
import urllib2

class DataDownloader(object):
    """下载数据·http://aima.cs.berkeley.edu/data/iris.csv 鸢尾花（iris）数据集,存入文件    iris.csv
                            这是一个包含了三种鸢尾花（山鸢尾、维吉尼亚鸢尾和变色鸢尾）的各50个数据样本的多元数据集，
                            每个样本都有四个特征（或者说变量），即花萼（sepal）和花瓣（petal）的长度和宽度。以厘米为单位。
    """
    def download(self,url='http://aima.cs.berkeley.edu/data/iris.csv'):
        fd = urllib2.urlopen(url)
        with open('iris.csv','w') as f:
            if f is not None:
                f.write(fd.read())
        
        
if __name__=='__main__':
    dl = DataDownloader()
    dl.download()
    print dl.__doc__
    