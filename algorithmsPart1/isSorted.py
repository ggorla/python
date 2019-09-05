items1 = [20,6,  8, 19, 56, 23, 87, 41, 49, 53]

items2 = [20,6,  8, 19, 56, 23, 87, 41, 49, 53]


def is_sorted(itemlist):

    for i in range((0,len(itemlist))-1):
        if(itemlist[i]> itemlist[i+1]):
            return False

    return True

print(is_sorted(items1))