# -*- coding: utf-8 -*-
'''
Created on 2016年3月16日

@author: carm
'''
# from iris.data_downloader import DataDownloader
from numpy import genfromtxt  # @UnresolvedImport
from iris.data_drawing import DataDrawing

class DataMining(object):
    
    
    def dataMining(self):
#         downloader = DataDownloader()
        painter = DataDrawing()
        
        # read the first 4 columns
        data = genfromtxt('iris.csv',delimiter=',',usecols={0,1,2,3})
        print data
        print data[:,0]
        # read the fifth column
        target = genfromtxt('iris.csv',delimiter=',',usecols={4},dtype=str)
#         print data.shape
#         print data
#         print target.shape
#         print set(target)
#        画一个二维散点图 

        painter.draw_two_dimension_spot(data, target)
        painter.draw_histogram(data,target)
    



if __name__ =='__main__' :
    dm = DataMining()
    dm.dataMining()