from matplotlib import pyplot as plt 
from sklearn.linear_model import LinearRegression
import numpy
import pandas
import plot


class Stats:

  def _init_(self, p):
      self.p = p
    # print("Hello")

    # self.data = pandas.read_csv('values.csv')
    # self.dev_x = self.data.iloc[:,0].values.reshape(-1,1)
    # self.dev_y = self.data.iloc[:,1].values.reshape(-1,1)
    # self.x = [2,3,4,5,6,7,8]
    # self.y = [10,20,30,40,50,60,70]
    



    # self.linReg = LinearRegression()
    # self.linReg.fit(self.dev_x,self.dev_y)
    # self.predicted_Y = self.linReg.predict(self.dev_x)

  # plt.scatter(self.dev_x, self.dev_y)
  # plt.plot(self.dev_x, predicted_Y, color='red')
  # plt.show()

  
      

  
  
  

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

    residLine = LinearRegression()
    residLine.fit(self.dev_x, self.residuals)
    residPredicted_Y = residLine.predict(self.dev_x)



p = plot()
obj = Stats(p)
obj.createResiduals()
print(1)

# # import string
# from matplotlib import pyplot as plt 
# from sklearn.linear_model import LinearRegression
# import numpy
# import pandas

# data = pandas.read_csv('Data Files/ris1.csv')
# dev_x = data.iloc[:,0].values.reshape(-1,1)
# dev_y = data.iloc[:,1].values.reshape(-1,1)

# linReg = LinearRegression()
# linReg.fit(dev_x,dev_y)
# predicted_Y = linReg.predict(dev_x)

# plt.scatter(dev_x, dev_y)
# plt.plot(dev_x, predicted_Y, color='red')
# plt.show()

# def findSum(list):
#     sum = 0
#     for x in list: 
#         sum += x
#     sum = int (sum)
#     return sum

# def findMean(list):
#     return findSum(list)/len(list)

# def findStdDev(list):
#     return numpy.std(list, dtype=numpy.float64)

# def findVariance(list):
#     return findStdDev(list)**2

# def getIntercept():
#     return linReg.intercept_

# def getSlope():
#     return linReg.coef_

# def getCorrCoef():
#     return linReg.score(dev_x, dev_y) 

# print("x count: " + str(len(dev_x)))
# print("x sum: " + str(findSum(dev_x)))

# print(str(findSum(dev_x)))
# print("x average: " + str(findMean(dev_x)))
# print("x std dev: " + str(findStdDev(dev_x)))
# print("y std dev: " + str(findStdDev(dev_y)))
# print("x variance: " + str(findVariance(dev_x)))

# print("Line: y = " + str(getSlope()) + " * x + " + str(getIntercept()))

# def getFormula():
#     return "Line: y = " + str(getSlope()) + " * x + " + str(getIntercept())

# def getPrediction(x):
#     return getSlope() * x + getIntercept()

# def getResidual(x, dev_x, dev_y):
#     count = 0
#     for xActual in dev_x:
#         if x == xActual:
#             return (float) (dev_y[count] - getPrediction(x))
#         count += 1
#     return "Error: No data collected for that x-value"