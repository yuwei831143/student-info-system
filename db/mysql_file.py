import mysql.connector.pooling


config = {
    'host':'localhost',
    'user':'root',
    'password':'a123456',
    'port':3306,
    'database':'school',
    'auth_plugin':'mysql_native_password'
}

pool = mysql.connector.pooling.MySQLConnectionPool(**config,pool_size=10)
