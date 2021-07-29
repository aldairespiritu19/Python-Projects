import sqlite3
import os


# created a table
conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_file (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT)")
    conn.commit()

# connected to the database
conn = sqlite3.connect('test.db')



# created a filelist 
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
   


# loop through filelist to find files ending with .txt
# and printing them out
for file in fileList:
    if file.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_file (file_name) VALUES (?)", (file,))
            print(file)

conn.close()
