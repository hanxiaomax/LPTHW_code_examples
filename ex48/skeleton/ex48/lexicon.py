#coding:utf-8
lexicon={
		"direction": 	"north, south, east, west, down, up, left, right, back",
		"verb": 		"go, stop, kill, eat open",
		"stop": 	"the, in, of, from, at, it,through",
		"noun": 		"door, bear, princess, cabinet",
		}
#sentence=[] 不能作为全局变量，否则测试错误，因为每次调用函数，前面的内容没有清除
def scan(user_sentence):
	sentence=[]
	user_words=user_sentence.split()
	words_copy=user_words
	for word in words_copy: #for word.lower() in words_copy:是不行的,后面还是大写
		if word.lower() in lexicon["direction"] :
			sentence.append(('direction',word))
		elif  word.lower() in lexicon["verb"]:
			sentence.append(('verb',word))
		elif word.lower() in lexicon["stop"]:
			sentence.append(('stop',word))
		elif word.lower() in lexicon["noun"]:
			sentence.append(('noun',word))
		else:
			try:
				int(word.lower()) #如果不是数字的话，int()会引发异常
				sentence.append(('number',int(word)))
			except:
				sentence.append(('error',word))
		#else :
			
	return sentence

#user_sentence=raw_input("> ")
#print scan(user_sentence)