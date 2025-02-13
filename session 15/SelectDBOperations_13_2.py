import mysql.connector
con = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
try:
    curs=con.cursor() #create cursor

    curs.execute("select * from student")
    for rows in curs:
        print(rows[0],rows[1],rows[2],rows[3],rows[4],rows[5])


    con.close()  #closing connection
except:
    print("Connection unsuccessful")

print("Database query done")