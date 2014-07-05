#coding:utf-8
import random
mylist=["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
class_names = [len(w) for w in mylist]
print class_names


#首字母大写
print "abc".capitalize() 

#统计某个字符或字符串个数
print "abc".count("a") 
print mylist.count("Day")

word_file=open("41-1.txt","r")
WORDS=[]

for word in word_file:
	WORDS.append(word.strip())
#print "\n".join(WORDS)


#随机生成一个WORDS的副本，元素个数为10，并不会改变WORDS
"""
print random.sample(WORDS,10)
print WORDS

classname=[name.capitalize() for name in random.sample(WORDS,10)]
print classname
"""
#把abcd中的abc替换为$$$
print "abcd".replace("abc","$$$",1)