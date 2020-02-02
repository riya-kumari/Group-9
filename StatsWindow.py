from tkinter import*
import PIL
from PIL import ImageTk
from PIL import Image
import plot
# Still need to do Line and Prediction for x

root = Tk()
p = plot.Graphs()
# p.displayBoth()
# All the Stats are recorded here
first = LabelFrame(root)
stats = Text(first, height = 20, width = 60)
stats.insert(END, "Count: " )
stats.insert(END, str(p.getCount()) + "\n")

# 0 = x; 1 = y
# x = true; y = false
stats.insert(END, "Sum of X: " )
stats.insert(END, str(p.findSum(0))+ "\n")

stats.insert(END, "Sum of Y: " )
stats.insert(END, str(p.findSum(1))+ "\n\n")

stats.insert(END, "Mean of X: " )
stats.insert(END, str(p.findMean(0)) + "\n" )

stats.insert(END, "Mean of Y: " )
stats.insert(END, str(p.findMean(1)) + "\n" )

stats.insert(END, "Std Dev of X: "  )
stats.insert(END, str(p.findStdDev_X()) + "\n" )

stats.insert(END, "Std Dev of Y: " )
stats.insert(END, str(p.findStdDev_Y()) + "\n" )

stats.insert(END, "Variance of X: " )
stats.insert(END, str(p.findVariance(0)) + "\n")

stats.insert(END, "Variance of Y: " )
stats.insert(END, str(p.findVariance(0)) + "\n\n")

stats.insert(END, "Slope: " )
stats.insert(END, str(float(p.getSlope())) + "\n" )


stats.insert(END, "Y-Intercept:"  )
stats.insert(END, str(float(p.getIntercept())) + "\n" )

stats.insert(END, "Correlation Coefficient: " )
stats.insert(END, str(p.getCorrCoef()) + "\n" )
# p.displayBoth()


stats.insert(END, "Line: " )
stats.insert(END, p.getFormula() + "\n")


# stats.insert(END, "What to never do with Regression : " + "\n")
# stats.insert(END, "1. Inferring Causation : THE TWO VARIABLE CAN BE CORRELATED BUT NEVER CAUSE ONE ANOTHER!!! " + "\n")
# stats.insert(END, "2. " + "\n")
# stats.insert(END, "What to never do with Regression : " + "\n")
# stats.insert(END, "What to never do with Regression : " + "\n")




# stats.insert(END, "Prediction for x: " )
# stats.insert(END, str(p.getPrediction("5")) + "\n" )

stats.pack()

first.grid(row = 0, column = 0)
buttons = LabelFrame(root)
b1 = Button(buttons, text = "View Scatterplot", command = lambda:p.displayScatter())
b1.pack()

b2 = Button(buttons, text = "View Residuals Plot", command = lambda:p.displayResid())
b2.pack()
buttons.grid(row = 1, column = 0)







root.mainloop()


