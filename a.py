class linearRegress(object):   
    def __init__(self,LRDict = None,  **args):   
        '''currently support OLS, ridge, LWLR            
        '''  
        obj_list = inspect.stack()[1][-2]   
        self.__name__ = obj_list[0].split('=')[0].strip()   
        if not LRDict:   
            self.LRDict = {}   
        else:   
            self.LRDict = LRDict   
            #to Numpy matraix  
            if 'OLS' in self.LRDict:   
                self.LRDict['OLS'] = mat(self.LRDict['OLS'])   
            if 'ridge' in self.LRDict:   
                self.LRDict['ridge'][0] = mat(self.LRDict['ridge'][0])   
                self.LRDict['ridge'][2] = mat(self.LRDict['ridge'][2])   
                self.LRDict['ridge'][3] = mat(self.LRDict['ridge'][3])   
                self.LRDict['ridge'][4] = mat(self.LRDict['ridge'][4])  

                
##新的算法

import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np
 
# 加载数据
# 备用地址: http://cdn.powerxing.com/files/lr-binary.csv
df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")
 
# 浏览数据集
print df.head()
#    admit  gre   gpa  rank
# 0      0  380  3.61     3
# 1      1  660  3.67     3
# 2      1  800  4.00     1
# 3      1  640  3.19     4
# 4      0  520  2.93     4
 
# 重命名'rank'列，因为dataframe中有个方法名也为'rank'
df.columns = ["admit", "gre", "gpa", "prestige"]
print df.columns
# array([admit, gre, gpa, prestige], dtype=object)


##这是一个修改测试