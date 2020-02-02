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
stats.insert(END, "Sum of X: " )
stats.insert(END, str(p.findSum("x"))+ "\n")

stats.insert(END, "Sum of Y: " )
stats.insert(END, str(p.findSum("y"))+ "\n")

stats.insert(END, "Mean of X: " )
stats.insert(END, str(p.findMean("x")) + "\n" )

stats.insert(END, "Mean of Y: " )
stats.insert(END, str(p.findMean("y")) + "\n" )

stats.insert(END, "Std Dev of X: "  )
stats.insert(END, str(p.findStdDev("x")) + "\n" )

stats.insert(END, "Std Dev of Y: " )
stats.insert(END, str(p.findStdDev("y")) + "\n" )

stats.insert(END, "Variance of X: " )
stats.insert(END, str(p.findVariance("x")) + "\n")

stats.insert(END, "Slope: " )
stats.insert(END, str(float(p.getSlope())) + "\n" )


stats.insert(END, "Y-Intercept:"  )
stats.insert(END, str(float(p.getIntercept())) + "\n" )

stats.insert(END, "Correlation Coefficient: " )
stats.insert(END, str(p.getCorrCoef()) + "\n" )
# p.displayBoth()


# stats.insert(END, "Line: " )
# stats.insert(END, str(p.getFormula()) + "\n")

# stats.insert(END, "Prediction for x: " )
# stats.insert(END, str(p.getPrediction("5")) + "\n" )

stats.pack()
first.grid(row = 0, column = 0)






root.mainloop()


