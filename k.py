import sys
import sqlite3 as sq
sys.path.append('/home/dyuzha/.me/real-dic')
from db import *
from pprint import pprint



word = Words.get(Words.word_id == 1)
print('word: ', word.word_id, word.ru)

query = Words.select().where((Words.win_count / Words.all_count) > 0.9)
words_selected = query.dicts().execute()

for row in words_selected:
    print(row)
    
con.close()

mem_con = SqliteDatabase(":memory:", &db)


class Mem_words(Words):
    local_count = IntegerField(column_name='local_count', default=0)
    class Meta:
        table_name = 'temp_words'


mem_cur = mem_con.cursor

    





