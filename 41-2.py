#coding:utf-8
import random
PHRASES = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}
#字典的key没有顺序可言
snippets = PHRASES.keys()

print "\n--------\n".join(snippets)

PHRASESS = {
    "A":
      "1",
    "B" :
      "2",
    "C":
      "3",
}

alpha=PHRASESS.keys()
print alpha
random.shuffle(alpha)
