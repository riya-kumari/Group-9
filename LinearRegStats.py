# import string
from matplotlib import pyplot as plt 
from sklearn.linear_model import LinearRegression
import numpy
import pandas

data = pandas.read_csv('Data Files/ris1.csv')
dev_x = data.iloc[:,0].values.reshape(-1,1)
dev_y = data.iloc[:,1].values.reshape(-1,1)

linReg = LinearRegression()
linReg.fit(dev_x,dev_y)
predicted_Y = linReg.predict(dev_x)

plt.scatter(dev_x, dev_y)
plt.plot(dev_x, predicted_Y, color='red')
plt.show()

def findSum(list):
    sum = 0
    for x in list: 
        sum += x
    sum = int (sum)
    return sum

def findMean(list):
    return findSum(list)/len(list)

def findStdDev(list):
    return numpy.std(list, dtype=numpy.float64)

def findVariance(list):
    return findStdDev(list)**2

def getIntercept():
    return linReg.intercept_

def getSlope():
    return linReg.coef_

def getCorrCoef():
    return linReg.score(dev_x, dev_y) 

print("x count: " + str(len(dev_x)))
print("x sum: " + str(findSum(dev_x)))

print(str(findSum(dev_x)))
print("x average: " + str(findMean(dev_x)))
print("x std dev: " + str(findStdDev(dev_x)))
print("y std dev: " + str(findStdDev(dev_y)))
print("x variance: " + str(findVariance(dev_x)))

print("Line: y = " + str(getSlope()) + " * x + " + str(getIntercept()))

def getFormula():
    return "Line: y = " + str(getSlope()) + " * x + " + str(getIntercept())

def getPrediction(x):
    return getSlope() * x + getIntercept()

def getResidual(x, dev_x, dev_y):
    count = 0
    for xActual in dev_x:
        if x == xActual:
            return (float) (dev_y[count] - getPrediction(x))
        count += 1
    return "Error: No data collected for that x-value"