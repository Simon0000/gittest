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
