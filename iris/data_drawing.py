# _*_ encoding: utf-8 _*_
'''
Created on 2016年3月16日

@author: carm
'''
from pylab import plot, show, figure, subplot, hist, xlim

class DataDrawing(object):
   
    def draw_two_dimension_spot(self,data,target):
        
        """
    使用第一和第三维度（花萼的长和宽）
    在上图中有150个点，不同的颜色代表不同的类型；
    蓝色点代表山鸢尾(setosa)，
    红色点代表变色鸢尾(versicolor)，
    绿色点代表维吉尼亚鸢尾(virginica)。
        """
        plot(data[target=='setosa',0],data[target=='setosa',2],'bo')
        plot(data[target=='versicolor',0],data[target=='versicolor',2],'ro')
        plot(data[target=='virginica',0],data[target=='virginica',2],'go')
        show()
    
    def draw_histogram(self, data, target):
        """
        绘制数据中每一类型的第一个特性（花萼的长度）
        """
        xmin = min(data[:,0])
        xmax = max(data[:,0])
        figure()
        subplot(411) # distribution of the setosa class (1st, on the top)
        hist(data[target=='setosa',0],color='b',alpha=.7)
        xlim(xmin,xmax)
        subplot(412) # distribution of the versicolor class (2nd)
        hist(data[target=='versicolor',0],color='r',alpha=.7)
        xlim(xmin,xmax)
        subplot(413) # distribution of the virginica class (3rd)
        hist(data[target=='virginica',0],color='g',alpha=.7)
        xlim(xmin,xmax)
        subplot(414) # global histogram (4th, on the bottom)
        hist(data[:,0],color='y',alpha=.7)
        xlim(xmin,xmax)
        show()
    
    
