import sqlite3



class Db:
    def __init__(self, name):
        self.name = name


    def begin(self):
        self.con = sqlite3.connect('self.name')
        self.cur = self.con.cursor()


    def save(self):
        con.commit()


    def reser(self):
        con.close()
        self.begin()


    def __del__(self):
        self.save()
        con.close()



class Table:
    def __init__(self, table, db):
        self.name = table 
        self.cur = db.cur

    def get_param(self, ident, param):
        self.cur.execute(f'SELECT {param} from {self.name} WHERE id = ?', (ident))
        value = cur.fetchall()
        return value


    def get_ru(self, ident):
        self.get_param(ident, 'en')
        return cur.fetchall()


    def get_en(self, ident):
        self.get_param(ident, 'ru')
        return cur.fetchall()


    def get_all(self):
        self.cur.execute(f'SELECT * FROM {self.name}')
        words = cur.fetchall()
        return cur.fetchall()


    def set_word(self, en, ru, hint=None):
        self.cur.execute(f'INSERT INTO {self.name} (en, ru, hint) VALUES (?, ?, ?)', (en, ru, hint))


    def update(self, ident, param, value): 
        cur.execute(f'UPDATE {self.name} SET {param} = ? WHERE ident = ?', (param, value, ident))


    def update_incr(self, ident, param):
        self.update(ident, param, param =+ 1) 


    def win(self, ident):
        self.update_incr(ident, 'win')


    def loss(self, ident):
        self.update_incr(ident, 'loss')


db = Db('words.db')
db.begin()
w = Table('Words', db)
w.get_all()






    


        



