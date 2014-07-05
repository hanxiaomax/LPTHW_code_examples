#coding:utf-8
import lexicon#不能from ex48，因为这两个文件在同一目录下

class ParserError(Exception):
	pass
class sentence(object):
	def __init__(self, subject,verb,object):
		self.subject=subject[1]
		self.verb=verb[1]
		self.object=object[1]	

#word_list是一个包含元组的列表
#peek查看该列表的头一个元组，并返回类别，但并不实际操作，相当于预览
def peek(word_list):
	if word_list:
		word=word_list[0]
		return word[0]
	else:
		return None

def match(word_list,expecting):
	if word_list:#列表不空
		word=word_list.pop(0)#弹出第一个列表元素(元组)
		if word[0]==expecting:#判断是否是所需的类型		
			return word
		else:
			return None

def skip(word_list,word_type):
	while peek(word_list)==word_type:
		match(word_list,word_type)#此处调用match只是为了pop，返回值未储存？

def parse_verb(word_list):
	skip(word_list,'stop')
	if peek(word_list)=='verb':
		return match(word_list,'verb')
	else:
		raise ParserError("Expected a verb next.")#异常类

def parse_object(word_list):
	skip(word_list,'stop')
	next=peek(word_list)#和上面没区别，只是分开了
	#宾语可以是一个名词或者地名
	if next=='noun':
		return match(word_list,'noun')
	if next=='direction':
		return match(word_list,'direction')
	else:
		raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list,subj):
	verb=parse_verb(word_list)
	obj=parse_object(word_list)

	return sentence(subj,verb,obj)

def parse_sentence(word_list):
	skip(word_list,'stop')
	start=peek(word_list)

	if start=='noun':#名词开头
		subj=match(word_list,'noun')
		return parse_subject(word_list,subj)
	elif start=='verb':#动词开头，默认名词是玩家
		return parse_subject(word_list,('noun','player'))
	else:
		raise ParserError("Must start with subject, object, or verb not: %s" % start)

"""
raw_sentence=lexicon.scan(raw_input('>'))
sentence=parse_sentence(raw_sentence)

print sentence.subject+" "+sentence.verb+" "+sentence.object
"""

#不能直接print sentence，它只是一个对象
