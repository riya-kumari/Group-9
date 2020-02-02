from matplotlib import pyplot as plt 
# import matplotlib.ba
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
        self.data = pandas.read_csv("Data Files/mycsv.csv")
        self.dev_x = self.data.iloc[:,0].values.reshape(-1,1)
        self.dev_y = self.data.iloc[:,1].values.reshape(-1,1)

        self.linReg = LinearRegression()
        self.linReg.fit(self.dev_x, self.dev_y)
        self.predicted_Y = self.linReg.predict(self.dev_x)
        self.createResiduals()

    def fixNumber(self,value):
        actualVal = int(value) * 1.0
        valueTup = actualVal.as_integer_ratio()
        value1st = valueTup[0]
        value2nd = valueTup[1]

        if(value2nd==1):
            return(str(int(value1st)))
        else:
            return(str(float(round(actualVal, 2))))
    def getCount(self):
        return str(len(self.dev_x))

    def findSum(self, axis):
        sum = 0
        if axis == 0:
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
        if axis == 0:
            return self.findSum(0)/len(self.dev_x)
        else:
            return self.findSum(1)/len(self.dev_x)


    def findStdDev_X(self):
        return numpy.std(self.dev_x, dtype=numpy.float64)

    def findStdDev_Y(self):
        return numpy.std(self.dev_y, dtype=numpy.float64)

    def findVariance(self, axis):
        if axis == 0:
            return self.findStdDev_X()**2
        else:
            return self.findStdDev_Y()**2
        

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

    # def getFormula(self):
    #     return ("y = " + str(self.fixNumber(self.getSlope())) + "x + " + str(self.fixNumber(self.getIntercept())))
    def getFormula(self):
        thisSlope = self.fixNumber(self.getSlope())
        thisInt = self.fixNumber(self.getIntercept())
        thisInt = int(thisInt)
        if(thisInt == 0):
            return ("y = " + str(thisSlope) + "x")
        elif(thisInt < 0):
            tempInt = thisInt * -1
            return ("y = " + str(thisSlope) + "x - " + str(tempInt))
        else:
            return ("y = " + str(thisSlope) + "x + " + str(thisInt))

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
        plt.title("Residual Plot")
        plt.scatter(self.dev_x, self.residuals)
        plt.plot(self.dev_x, self.residPredicted_Y, color='red')
        plt.show()

    def displayScatter(self):
        plt.title("ScatterPlot with Regression")
        plt.scatter(self.dev_x, self.dev_y)
        plt.plot(self.dev_x, self.predicted_Y, color='red')
        plt.show()

    def displayBoth(self):
        
        plt.figure()
        plt.subplot(2,2,1)
        plt.scatter(self.dev_x, self.residuals)
        plt.plot(self.dev_x, self.predicted_Y, color='red')
        
        plt.title("Original")

        plt.subplot(2,2,2)
        plt.scatter(self.dev_x, self.residuals)
        plt.plot(self.dev_x, self.residPredicted_Y, color='red')
        plt.title("Residuals Plot")

        plt.show()

        # fig = plt.figure()
        # ax1 = fig.add_subplot(221)
        # ax2 = fig.add_subplot(222, sharex=ax1, sharey=ax1)
        # ax3 = fig.add_subplot(223, sharex=ax1, sharey=ax1)
        # ax3 = fig.add_subplot(224, sharex=ax1, sharey=ax1)
        # plt.show()

        # fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey=True)
        # ax1.plot(x)

# p = Graphs()
# # # # # print(p.getFormula())
# # # # print
# # # # # # p.createResiduals()
# # # # # # resid = p
# # # # # # resid.displayResid()
# # # # # # p.displayScatter()
# p.displayScatter()
# p.displayResid()