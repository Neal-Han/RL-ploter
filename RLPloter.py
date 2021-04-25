import numpy as np
import pandas as pd
import seaborn as sns
from copy import deepcopy
import matplotlib.pyplot as plt
sns.set()


class RlPloter():
    def __init__(self):
        self.reset()

    def setTitle(self,title,label_fontSize = 15):
        self.__title = title
        self.__titleSize = label_fontSize
    
    def setLabel(self,xlabel,ylabel,label_fontSize = 13):
        self.__xLabel = xlabel
        self.__yLabel = ylabel
        self.__labelSize = label_fontSize
    
    def setXScale(self,xScale):
        self.__xScale = xScale

    def setYScale(self,yScale):
        self.__yScale = yScale
    
    def addData(self,data,label,markerstyle=None,color=None):
        self.__linesArr.append(data)
        self.__labelArr.append(label)
        self.__markerstyleArr.append(markerstyle)
        self.__colorArr.append(color)
    
    def reset(self):
        self.__linesArr = []
        self.__colorArr = []
        self.__labelArr = []
        self.__title = None
        self.__xLabel = None
        self.__yLabel = None
        self.__xScale = 1
        self.__yScale = 1
        self.__titleSize = 15
        self.__labelSize = 13
        self.__markerstyleArr = []
        self.__colorArr = []

    def showFigure(self, show = True, save = False, fileName= "figure"):
        df=[]
        fig = plt.figure()
        for i,line in enumerate(self.__linesArr):
            line = np.array(line)
            df.append(pd.DataFrame(line).melt(
                var_name=self.__xLabel,value_name=self.__yLabel))
            df[i][self.__xLabel] *= self.__xScale              # scale X
            df[i][self.__yLabel] *= self.__yScale              # scale Y
            df[i]['label']= self.__labelArr[i]          # set label
            df[i]['markerstyle'] = self.__markerstyleArr[i] # set style

        df=pd.concat(df)
        
        g = sns.lineplot(x=self.__xLabel, y=self.__yLabel,
            hue='label',style='label',data=df,markers=self.__markerstyleArr)
        g.legend_.set_title(None)
        plt.xlabel(self.__xLabel)
        plt.ylabel(self.__yLabel)
        plt.title(self.__title, fontsize=self.__titleSize)

        if show:
            plt.show()
        if save:
            figureName = deepcopy(fileName)
            figureName += '.jpg'
            plt.savefig(figureName)



if __name__ == '__main__':


    a = RlPloter()
    a.setTitle('Example')
    a.setLabel('x-axis','y-axis')

    data1 = [[23, 19, 20, 19, 11, 15, 14],             
             [19, 24, 19, 21, 20, 15, 12],             
             [19, 20, 20, 20, 17, 10, 9],             
             [20, 20, 20, 20, 12, 19, 13]]   

    data2 = [[22, 23, 22, 20, 19, 17, 4],            
             [18, 20, 22, 20, 20, 19, 9],            
             [19, 20, 20, 19, 19, 15, 4],
             [19, 21, 21, 19, 19, 14, 2]]   


    a.addData(data1,'test1')
    a.addData(data2,'test2')
    a.setXScale(2) 
    a.setYScale(2)   
    a.showFigure(show = True,save = False, fileName = 'figure')

## markerstyle

# 'o'                   Circle
# '+'                   Plus sign
# '*'                   Asterisk
# '.'                   Point
# 'x'                   Cross
# '_'                   Horizontal line
# '|'                   Vertical line
# 'square' or 's'       Square
# 'diamond' or 'd'      Diamond
# '^'                   Upward-pointing triangle
# 'v'                   Downward-pointing triangle
# '>'                   Right-pointing triangle
# '<'                   Left-pointing triangle
# 'pentagram' or 'p'    Five-pointed star (pentagram)
# 'hexagram' or 'h'     Six-pointed star (hexagram)
# 'none'                No markers
