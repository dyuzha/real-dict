import sqlite3 as sq
import sys
sys.path.append('/home/dyuzha/.me/real-dic')
from db import *
import req

def answer(text)
    print(text)
    ans = input('[Y/N]')
    if ans == 'Y' or 'y'
        return True
    elif ans == 'N'or 'n'
        return False





class Kernel:

    def __init__(self, db):
        self.db = db

    def run():
        self.read(config)
        self.select(req, table)
        self.__grade(db)
        self.__compose(db)
        
        if self.save():
            self.__merge()

        self.__begin()
        

    def self.save():
        return answer('Do you want save result?')

    def read(self, config)
        pass


   def select(self, request, table):
        con = sq.connect(self.db)
        cur = con.cursor()
        cur.execute(req.words_tb)
        con.commit()

        try:
            cur.execute(request)
            tableTemp = cur.fetchall()

            con.commit()

            print('Date base temp is created.')

        except Exception as e:
            con.rollback()
            print(f'Error: {str(e)} Date base is not created')

        finally:
            con.close()

        return tableTemp


    def __grade(self, self.db)

    def __compose()

    def __merge()

    def __begin()
        ans = answer('You want go?')
        return ans


class Compose:
    
    def work(self, worker, word, word_id):
        worker.run(word)

    def check(self, word_id, word):
        true_word = table.llallala
        if word == true_word:
            pass
         

class Worker:
        
    def run(self, text):
        print(text)
        input(ans)
        return ans


class Grader(Kernel):
    def __init__(self, db, attr, mn, mx) 
        self.db = db
        self.main = attr
        self.mn
        self.mx

    def select(self, request):
        pass


    def grading(self, table): 
        for row in table:
            case row.rate == 

    def chaaining(self, a*, kw**):
        pass


class Table:

    sel_all = f'SELECT * FROM Words'
    sel_ru = 'SELECT ru FROM Words WHERE id = ?'
    sel_en = 'SELECT en FROM Words WHERE id = ?'
    del_row = f'DELETE FROM Words WHERE id = ?'
    add_row = f'INSERT INTO Words (en, ru, hint) VALUES (?, ?, ?)'

    def __init__(self, name):
        self.name = name 

    def get_all(self):
        cur.execute(self.sel_all)
        words = cur.fetchall()
        for word in words:
            print(word)

    def get_ru(self, ident):
        cur.execute(self.sel_ru, ident)
        return cur.fetchall()

    def get_en(self, ident):
        cur.execute(self.sel_en, ident)
        return cur.fetchall()

    def get_rate(self):
        cur.execute(req.sel_rate)
        words = cur.fetchall()
        for word in words:
            print(word)

    def win(self, ident):
        cur.execute(req.win, ident)

    def loss(self, ident):
        cur.execute(req.loss, ident)

    def set_row(self, en, ru, hint=None):
        value = (en, ru, hint)
        cur.execute(self.add_row, value)

    def rem_row(self, ident):
        cur.execute(self.del_row, ident)


#words = Table('Words.db')
    
class Kernel:
    def __init__(self, mode):
        self.mode = mode
        pass

    def give(self, count):
        pass
    
    def merge(self, table1, table2)

    def begin(self):
        pass



w.get_all()
w.get_rate()
#con.commit()

