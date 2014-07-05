#coding: utf-8

words=("All good things come to those who wait.".strip('.')).split(' ')
word_copy=words
#先把.号去掉，然后再分离成一个列表
print words
print word_copy
for i in range(1,len(words)+1):
	print words.pop(0)

print word_copy.pop(-1)
