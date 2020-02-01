from tkinter import*
import PIL
from PIL import ImageTk
from PIL import Image
# import LinearRegStats, plot


# class window:
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Stats-Window")
#         self.root.geometry("200x200")

#         self.graph = LabelFrame(self.root)
#         self.graph.grid(row = 0, column =0)
        

#         self.stats = LabelFrame(self.root)
#         sel
#         self.count = Text(self.stats, "Count : ")
#         self.sum = Text(self.stats, "Text : ")
#         self.stats.grid(row = 1, column = 0)
        
#         self.root.mainloop()

# result = window()

        
root = Tk()
root.title("Stats-Window")

stats = Text(root, height = 20, width = 60)
stats.insert(END, "Count:\n"  )
stats.insert(END, "Sum:\n"  )
stats.insert(END, "Mean:\n"  )
stats.insert(END, "Std Dev of X:\n"  )
stats.insert(END, "Std Dev of Y:\n"  )
stats.insert(END, "Variance of X:\n\n\n"  )

stats.insert(END, "Slope:\n"  )
stats.insert(END, "Y-Intercept\n"  )
stats.insert(END, "Correlation Coefficient:\n"  )
stats.insert(END, "Line:\n"  )
stats.insert(END, "Prediction for x\n"  )



stats.pack()

root.mainloop()

