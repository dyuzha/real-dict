
words_tb = '''
    CREATE TABLE IF NOT EXISTS Words(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        en TEXT NOT NULL,
        ru TEXT NOT NULL,
        hint TEXT,
        count INTEGER DEFAULT 0,
        win INTEGER DEFAULT 0,
        hz REAL 
        );
'''

selRate = '''
    SELECT 
        *,
        (CAST(win AS REAL)/count) AS 'rate'
    FROM 
        Words
    ORDER BY 
        rate ASK,
        count ASK
    LIMIT 8
'''

winInc = '''
	UPDATE Words
	SET win = win + 1,
		count = count + 1
	WHERE ID = ?
'''

lossInc = '''
	UPDATE Words
    SET count = count + 1
	WHERE ID = ?
'''
