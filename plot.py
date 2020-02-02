from matplotlib import pyplot as plt 
from sklearn.linear_model import LinearRegression
import argsparse
import numpy
import pandas

# TO RUN : python3 plot.py 
# TO EXIT ;: ctrl z

# dev_x = [4,5,6,7,7,9]
# dev_y = [4,5,6,7,7,9]
# data = pandas.read_csv('Data Files/values.csv')
data = pandas.read_csv("Data Files/mycsv.csv")
dev_x = data.iloc[:,0].values.reshape(-1,1)
dev_y = data.iloc[:,1].values.reshape(-1,1)

linReg = LinearRegression()
linReg.fit(dev_x,dev_y)
predicted_Y = linReg.predict(dev_x)

def getIntercept():
    return linReg.intercept_

def getSlope():
    return linReg.coef_

print("Intercept : " + str(getIntercept()))
print("Slope : "+ str(getSlope()))
print(linReg.score(dev_x, dev_y ))

# print('Coefficients: \n', linReg.coef_)x


plt.scatter(dev_x, dev_y)
plt.plot(dev_x, predicted_Y, color='red')
# plt.plot(dev_x)
plt.show()
