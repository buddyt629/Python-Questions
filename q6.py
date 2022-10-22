
def swapList(newList,pos1,pos2):
   
    temp = newList[pos1-1]
    newList[pos1-1] = newList[pos2-1]
    newList[pos2-1] = temp
     
    return newList

newList = [23, 65, 19, 90]
pos1=1
pos2=3
 
print(swapList(newList,pos1,pos2))