from peewee import *


con = SqliteDatabase('words.db')

class BaseModel(Model):
    class Meta:
        database = con


class Words(BaseModel):
                
    word_id = AutoField(column_name='id')
    en = TextField(column_name='en', null=False)
    ru = TextField(column_name='ru', null=False)
    hint = TextField(column_name='hint', null=True)
    all_count = IntegerField(column_name='count', default=0)
    win_count = IntegerField(column_name='win', default=0)
    
    hz = FloatField(column_name='hz')


    class Meta:
        table_name = 'Words'

cur = con.cursor

#cur = con.cursor()
#
#word = Words.get(Words.word_id ==  1)
#print('word: ', word.word_id, word.ru)
#query = Words.select()
#print(query) 
#
#con.close()
