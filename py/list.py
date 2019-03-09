movies=["the Holy grail",
"The Life of Brial"]
print(movies[0])
print(len(movies))
print(movies)
movies.append("The Meaning of Life")
cast=["Cleese","Ralin","Jonse","Idle"]
movies.extend(cast)
print(movies)
cast.append("chapman")
cast.remove("Cleese")
print(cast)
cast.insert(0,"Cleese")
###########################单行注释##############
''' 多行注释 
以上列出了列表的基本操作
下面重新开始
如果想要为一个列表插入年份，这明显是一个数字但却是可行的
'''
movies=["the Holy grail",
"The Life of Brial",
"The Meaning of Life"]
movies.insert(3,1983)
movies.insert(2,1979)
movies.insert(1,1975)
########上面第一句insert直接插入了列表的第三个元素这在其它语言中貌似是一个越界操作##
####我们来试验一下#######
movies.insert(8,"test")
print(movies)
#print(movies[8]) 越界访问是不可行的
###指定到8插入，但却出现在了第六个位置也就是最后一个位置
