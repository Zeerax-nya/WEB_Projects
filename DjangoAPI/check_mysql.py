import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='OralCumShot',
                             db='mytestdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT *  from mytestdb.EmployeeApp_department"
        # sql = "SELECT *  from mytestdb.EmployeeApp_employees"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()