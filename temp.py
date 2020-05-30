app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = '3008'
app.config['MYSQL_DATABASE_PASSWORD'] = '78679'
app.config['MYSQL_DATABASE_DB'] = 'otms'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql = MySQL(app)

conn = mysql.connect()
cursor = conn.cursor()