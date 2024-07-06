import sqlite3 as sq
import sys
sys.path.append('/home/dyuzha/.me/real-dic')
import req


con = sq.connect('words.db')
cur = con.cursor()


cur.execute(req.words_tb)


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

