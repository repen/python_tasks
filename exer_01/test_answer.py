from answer import *

with open('history.txt') as f_obj:
    text1 = f_obj.read()

def test_open_file():
    assert isinstance(open_file('history.txt'), str)
    assert len(open_file('history.txt')) == 2335

def test_serialize_txt_file():
    assert len(serialize_txt_file(text1)) == 1764

def test_analize_text():
    assert analize_text(text1, 'а') == 123
    assert isinstance(analize_text(text1, 'а'), int)

def test_top_letter():
    assert  top_letter == [('о', 260), ('е', 163), ('к', 151), ('а', 123), ('л', 108)]

