from unicodedata import name
import re

def question_01():
    return 'São Paulo'.isascii()

def question_02():
    octets = b'Montr\xe9al'
    return octets.decode('cp1252')

def question_03():
  open('cafe.txt', 'w', encoding='utf_8').write('café')
  return open('cafe.txt', encoding='cp1252').read()

def question_04():
    return name('e')

def question_05():
    re_words_str = re.compile(r'\w+')
    re_words_bytes = re.compile(rb'\w+')
    text_str = ("10³")
    text_bytes = text_str.encode('utf_8')
    return (re_words_bytes.findall(text_bytes), re_words_str.findall(text_str))

def byte_questions():
    return [
            (question_05, [False, True, 'Error']),
            (question_04, [False, True, 'Error']),
            (question_03, [False, True, 'Error']),
            (question_02, [False, True, 'Error']),
            (question_01, [False, True, 'Error']),
        ]