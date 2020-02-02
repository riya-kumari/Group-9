from PIL import Image
import PIL
from pytesseract import image_to_string
from cv2 import cv2
import csv

# Opening the image and coverting it to string
# Text is a string
img = Image.open("images/Data1.png")
text = image_to_string(img, lang='eng')

# Splitting by every new line and placing in a list
tableList = list(text.split("\n"))

# Creating a new list that will contain just the pints(x and y values) we need
newTableList = []
finalTableList = []

# An X list and a Y list
final_X = []
final_Y = []

# ex of x is 'Audi A4 200 32'
for x in tableList:

    # Split x by blank-spaces and put that in a list so you 
    # end up with a 2-d array
    x = list(x.split(" "))

    # Reverse it so the numbers we need are in the front
    x.reverse()

    # Changing the list to the just the x and y values we need
    x = x[:2]
    
    # Appending this list to the final list - acts as a 2d array
    # Each index in list  --> ['30','40']
    newTableList.append(x)
    #final_X.append(x[0])
    #final_Y.append(x[1])
    
#     ['32', '200', 'A4', 'Audi]
    # final_X.append(newTableList)


    
    #points = [final_X,final_Y]
    # print(final_X)
    # print(final_Y)
print("Printing newTableList...")
print(newTableList)
# print(newTableList[7])
# print(newTableList[8])
# int("green")
# print(final_X)
# print(final_Y)

#Adding it on a csv file
def creatingCSV():

    with open('Data Files/mycsv.csv', 'w') as file:

        # Creating a writer object
        writer = csv.writer(file)
        # [column1, column2]
        writer.writerow(["X values","Y values"])
        index = -1
        # x = ['20','15']
        for x in newTableList:
            # '20'
            for y in x:
                index+=1
                print("Printing y : ")
                print(y)
                try:
                    point = int(y)
                    finalTableList[x(index)] = point
                # If a valueError then delete that number from the list
                except ValueError:
                    pass
                    # del newTableList[index(x)]
        for x in newTableList:
            writer.writerow(x)

# with open('valuetable.csv','w',newline='') as f:
#     writer = csv.writer(f)
    
#     writer.writerow(["x","y"])
#     for i in newTableList:
#         writer.writerow(i)

creatingCSV()
# print(newTableList)