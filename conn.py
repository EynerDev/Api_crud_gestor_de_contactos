import pymysql

connection = None
cursor = None
try:
    # Establecer la conexión
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        database='prueba',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    cursor = connection.cursor()

    print("conexion exitosa.....")

    # Consulta SELECT
    sql = "SELECT * FROM users"
    cursor.execute(sql)

    # Obtener los resultados
    rows = cursor.fetchall()
    print(rows)

    # Operaciones CRUD aquí

except pymysql.MySQLError as e:
    print(f"Error de conexión a MySQL: {e}")

finally:
    if 'connection' in locals():
        connection.close()
