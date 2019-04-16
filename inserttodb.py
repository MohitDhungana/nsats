import mysql.connector
import datetime

from mysql.connector import errorcode

dt = datetime.datetime.now()
dt = (dt.strftime("%Y-%m-%d %H:%M:%S"))
try:
    mydb = mysql.connector.connect(user="root", database="nsats", )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    print("Connected to Database")


def insert_to_db(jid, percentage):
    junction_id = 10
    id = 1
    if percentage == 0:
        x = 0
    else:
        x = float(((percentage) - 80) * 13.2648)
    y = float(0.3455 * x)
    print("traffic density = " + str(x) + " %")
    mycursor = mydb.cursor()
    sql = "INSERT INTO densities (ID,right_density,straight_density,lane_id,created_at) values (%s,%s,%s,%s,%s)"
    val = (id, y, x, jid, dt)
    mycursor.execute(sql, val)

    sql = "UPDATE density_fetch set id='%s',a_right='%s',a_straight='%s',b_right='%s',b_straight='%s',c_right='%s'," \
          "c_straight='%s',d_right='%s',d_straight='%s',junction_id='%s' WHERE id=1 "
    val = (id, x, y, abs(x - 50), abs(x - 22), abs(x - 13), abs(x - 5), abs(x - 25), abs(x - 30), junction_id)
    mycursor.execute(sql, val)

    mydb.commit()

    print("Successfully inserted to NSATS database.\n")
