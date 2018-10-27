from dbfread import DBF
import regex as re

pattern = '^\P{C}'

for record in DBF('zaliznia.dbf', encoding='cp1251', char_decode_errors='replace'):
    word = record['WORD'][0] if re.match(pattern, record['WORD']) else None
    if word:
        grammar = record['GRAMMAR'][0] if re.match(pattern, record['GRAMMAR']) else ''
        trans = record['TRANS'][0] if re.match(pattern, record['TRANS']) else ''
        print(','.join([word, grammar, trans]))
