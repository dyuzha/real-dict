

def selectReq(db, table, commmand):  #-> date(format ?????)
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


        
    pass

def grade(table): #-> date( на 1 столбец больше )
    pass

def makeChain(table): #-> list/iter (из id)
    pass



def run(ram_tb, chain):
    for word_id in chain:
        word_en, word_ru = ram_tb.getWords(i)
        while True:
            print(word_ru)
            userWord = input(': ')
            if userWord == wordEn:
                print(win_word_banner)
                brake 
                ram_tb.update_error(word_id)
            else:
                error += 1
                print(loss_word_banner)
    print(win_banner)

def merge()
    pass

db = '?'
table = '?'
command = '?'
winWordBanner = '^*^'
lossWordBanner = 'try once more...'
winBanner = f"*********\n
              *sucsess*\n
              *********"


ram_tb = selectReq(db, table, commmand)

grade(ram_tb)

chain = makeChain(ram_tb)

run(ram_tb, chain)

merge(main_tb, ram_tb)









ь

