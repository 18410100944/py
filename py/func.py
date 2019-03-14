BiologyList=["动物","植物",["猴头","木耳",["毒蘑菇","平菇"]]]

def print_lol(Blist):
    for each_item in Blist:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print(each_item)

print_lol(BiologyList)