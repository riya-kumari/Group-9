newTableList = [["pp","cc"],[''],[1,2],[1,2],[1,2],[1,2],[1,2]]
finalTableList = [["pp","cc"],[''],[1,2],[1,2],[1,2],[1,2],[1,2]]


        # Creating a writer object

        # [column1, column2]

index = 0
        # x = ['20','15']
count = len(newTableList) - 1
for i in range(count):
          if ' ' in newTableList[i] :
            newTableList.remove([' '])
print(newTableList)
for i in range(count):
    try:
        x = int(newTableList[i][0])
        y = int(newTableList[i][1])
        print(index)
        print(x)
        if " " in newTableList[i]:
                  newTableList.remove(" ")
        
                  
            # print(finalTableList[i][])
        finalTableList[index][0] = x
        finalTableList[index][1] = y
        index += 1

    except ValueError:
            pass

print(finalTableList)