# update_query = "UPDATE student SET age = 26, email = 'michael.scott26@example.com' WHERE name = 'Michael Scott';"
# delete_query = "DELETE FROM student WHERE name = 'Michael Scott';"

import mysql.connector
con = mysql.connector.connect(host="localhost",port=3306,user="root",passwd="root",database="mydb")
try:
    curs=con.cursor() #create cursor

    # curs.execute("INSERT INTO student (name, age, gender, email, admission_date) VALUES ('Michael Scott', 25, 'Male', 'michael.scott@example.com', '2024-02-10');")  #perform query
    # curs.execute(update_query)
    # curs.execute(delete_query)
    con.commit() #committing transaction
    con.close()  #closing connection
except:
    print("Connection unsuccessful")

print("Database query done")