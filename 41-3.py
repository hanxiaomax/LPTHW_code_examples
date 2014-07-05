#coding:utf-8
mylist=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
the_count = [1, 2, 3, 4, 5]
result=[]
#同时遍历多个列表
for i in mylist,the_count:
	result.append(i)

print result