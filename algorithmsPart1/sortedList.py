items = [20,6,  8, 19, 56, 23, 87, 41, 49, 53]

def binarySearch(item, itemlist):
    listsize = len(itemlist)-1
    lowerIdx = 0
    upperIdx = listsize

    while lowerIdx <=upperIdx:
        midpoint = (lowerIdx+upperIdx//2)

        if itemlist[midpoint]== item:
            return  midpoint

        if item>itemlist[midpoint]:
            lowerIdx=midpoint+1
        else:
            upperIdx = midpoint+1

    if lowerIdx>upperIdx:
        return  None

print (binarySearch(23,items))