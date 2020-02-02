from PIL import Image
import PIL
from pytesseract import image_to_string
from cv2 import cv2
import csv
import argparse

# python3 imageToText.py --image Images/Data1.png
# python3 imageToText.py --image ["whatever image file"]

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str,
	help="path to input image")
args = vars(ap.parse_args())
# Opening the image and coverting it to string
# Text is a string
img = Image.open(args["image"])
text = image_to_string(img, lang='eng')

# Splitting by every new line and placing in a list
tableList = list(text.split("\n"))

# Creating a new list that will contain just the pints(x and y values) we need
newTableList = []
finalTableList = []
TableList_noStrings = []

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


# print("Printing newTableList...")
# print(newTableList)

def removingSpaces():
    for x in newTableList:
        if '' in x:
            pass
        if ' ' in x:
            pass
        if len(x) == 1:
            pass
        else:
            finalTableList.append(x)

def removingStrings():
    index = 0
    for x in finalTableList:
        try:
            a = int(x[0])
            b = int(x[1])
            TableList_noStrings.append([[],[]])
            TableList_noStrings[index][0] = a
            TableList_noStrings[index][1] = b
            index +=1
        except ValueError:
            pass

def createCSV():
    with open('Data Files/mycsv.csv', 'w') as file:
        writer = csv.writer(file)
        for row in TableList_noStrings:
            writer.writerow(row)
        
removingSpaces()
# print(finalTableList)
removingStrings()

# print(TableList_noStrings)
createCSV()


            
#Adding it on a csv file
# def creatingCSV():
#     with open('Data Files/mycsv.csv', 'w') as file:

#         # Creating a writer object
#         writer = csv.writer(file)
#         # [column1, column2]
#         writer.writerow(["X values","Y values"])
#         index = 0
#         # x = ['20','15']
#         count = len(newTableList) - 1
#         for i in range(count):
#           if ' ' in newTableList[i] :
#             newTableList.remove([' '])
#         for i in range(count):
#             try:
#                 x = int(newTableList[i][0])
#                 y = int(newTableList[i][1])
#                 print(index)
#                 print(x)
                
#                 # print(finalTableList[i][])
#                 finalTableList[index][0] = x
#                 finalTableList[index][1] = y
#                 index+=1
                
#             except ValueError:
#                 pass
            

#         print(finalTableList)















#         # for 
#         # for x in newTableList:
#         #     count+=1
#         #     index = 0
#         #     for y in x:
#         #         try:
#         #             y = int(y)
#         #             # x = int(x)
#         #             finalTableList[count].append(y)
                  
#         #             index = 1


#         #         # If a valueError then delete that number from the list
#         #         except ValueError:
#         #             pass

                

#         # for x in finalTableList:
#         #     writer.writerow(x)

# # with open('valuetable.csv','w',newline='') as f:
# #     writer = csv.writer(f)
    
# #     writer.writerow(["x","y"])
# #     for i in newTableList:
# #         writer.writerow(i)


# # print(newTableList)