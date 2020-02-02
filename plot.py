from matplotlib import pyplot as plt 
from sklearn.linear_model import LinearRegression
# import argsparse
import numpy
import pandas

# TO RUN : python3 plot.py 
# TO EXIT ;: ctrl z

# dev_x = [4,5,6,7,7,9]
# dev_y = [4,5,6,7,7,9]
# data = pandas.read_csv('Data Files/values.csv')

class Graphs():

    def __init__(self):
        # self.data = pandas.read_csv("Data Files/mycsv.csv")
        self.data = pandas.read_csv("Data Files/values.csv")
        self.dev_x = self.data.iloc[:,0].values.reshape(-1,1)
        self.dev_y = self.data.iloc[:,1].values.reshape(-1,1)

        self.linReg = LinearRegression()
        self.linReg.fit(self.dev_x, self.dev_y)
        self.predicted_Y = self.linReg.predict(self.dev_x)

    def getCount(self):
        return str(len(self.dev_x))

    def findSum(self, axis):
        sum = 0
        if axis == "x":
            for x in self.dev_x: 
                sum += x
            sum = int (sum)
            return sum
        else :
            for y in self.dev_y: 
                sum += y
            sum = int (sum)
            return sum

    def findMean(self, axis):
        if axis == "x":
            return self.findSum("x")/len(self.dev_x)
        else:
            return self.findSum("y")/len(self.dev_x)

    def findStdDev(self, axis):
        if axis =="x":
            return numpy.std(self.dev_x, dtype=numpy.float64)
        else:
            return numpy.std(self.dev_y, dtype=numpy.float64)

    def findVariance(self, axis):
        if axis == "x":
            return self.findStdDev(self.dev_x)**2
        else:
            return self.findStdDev(self.dev_y)**2
        

    def getdev_x(self):
        return self.dev_x

    def getdev_y(self):
        return self.dev_y

    def getCorrCoef(self):
        return self.linReg.score(self.dev_x, self.dev_y) 

    def getIntercept(self):
        return self.linReg.intercept_

    def getSlope(self):
        return self.linReg.coef_

    def getFormula(self):
        return "y = " + str(self.removeZero(self.getSlope())) + "x + " + str(self.removeZero(self.getIntercept()))


    def getPrediction(self, x):
        return self.getSlope() * x + self.getIntercept()

    def getResidual(self,x, dev_x, dev_y):
        count = 0
        for xActual in self.dev_x:
            if x == xActual:
                return (float) (self.dev_y[count] - (self.getPrediction(x)))
            count += 1
        return "Error: No data collected for that x-value"

    def getLargest(self):
        largest = self.dev_x[0]
        for x in self.dev_x:
            if x > largest:
                largest = x
        return x

    def removeZero(self, extra):
        if not extra.is_integer():
            return self.roundToTwo(extra)
        else:
            return int(extra)

    def roundToTwo(self, toRound):
        if(type(toRound)==int):
            return toRound
        else:
            return(round(toRound, 2))

  #Finding and graphing residuals
    def createResiduals(self):
        self.residuals = []
        print("entered the method")
        for x in self.dev_x:
            self.residuals.append(self.getResidual(x, self.dev_x, self.dev_y))

        self.residLine = LinearRegression()
        self.residLine.fit(self.dev_x, self.residuals)
        self.residPredicted_Y = self.residLine.predict(self.dev_x)

    def displayResid(self):
        self.createResiduals()
        plt.scatter(self.dev_x, self.residuals)
        plt.plot(self.dev_x, self.residPredicted_Y, color='red')
        plt.show()

    def displayScatter(self):
        plt.scatter(self.dev_x, self.dev_y)
        plt.plot(self.dev_x, self.predicted_Y, color='red')
        plt.show()

    def displayBoth(self):
        plt.scatter(self.dev_x, self.dev_y)
        plt.plot(self.dev_x, self.predicted_Y, color='red')
        plt.show()

        self.createResiduals()
        plt.scatter(self.dev_x, self.residuals)
        plt.plot(self.dev_x, self.residPredicted_Y, color='red')
        plt.show()

# p = Graphs()
# # print(p.getFormula())
# print
# # # p.createResiduals()
# # # resid = p
# # # resid.displayResid()
# # # p.displayScatter()
# # p.displayBoth()