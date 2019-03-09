fav_movies=["The Holy Grail","The Life of Brian"]
for each_flick in fav_movies:
    print(each_flick)

###############下面完成了同样的工作###################
count=0
while count<len(fav_movies):
    print(fav_movies[count])
    count=count+1
    # or: 
    # count += 1
    #经过试验没有发现 ++ 运算符
#########py是根据缩进来识别代码块而不是大括号########
