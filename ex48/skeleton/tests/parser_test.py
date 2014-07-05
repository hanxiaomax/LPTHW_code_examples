from nose.tools import *
from ex48 import parser
from ex48 import lexicon



def test_sentence():
    raw_sentence=lexicon.scan("go THROUGH the door")
    sentence=parser.parse_sentence(raw_sentence)
    result=sentence.subject+" "+sentence.verb+" "+sentence.object
    assert_equal(result,"player go door")

   # assert_raises