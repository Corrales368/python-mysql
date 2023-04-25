import mysql.connector

try:
    # Crea una conexión con la base de datos
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="123456",
      database="superdb"
    )

    # Verifica si la conexión se ha establecido correctamente
    if mydb.is_connected():
      print("Conexión exitosa a MySQL")
    else:
       print("Conexión fallida a MySQL")

    # Elimina todos los registros de la tabla empleados
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM empleados")

    # Crea una tabla de empleados 
    # mycursor.execute("CREATE TABLE empleados (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT, salario DOUBLE)")

    # Ejemplo 1
    sql = "INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s)"
    val = ("Juan", 25, 3000.0)
    mycursor.execute(sql, val)

    # Ejemplo 2
    sql = "INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s)"
    val = ("María", 30, 3500.0)
    mycursor.execute(sql, val)

    # Ejemplo 3
    sql = "INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s)"
    val = ("Pedro", 28, 3200.0)
    mycursor.execute(sql, val)

    # Ejemplo 4
    sql = "INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s)"
    val = ("Laura", 22, 2800.0)
    mycursor.execute(sql, val)

    # Ejemplo 5
    sql = "INSERT INTO empleados (nombre, edad, salario) VALUES (%s, %s, %s)"
    val = ("Roberto", 35, 4000.0)
    mycursor.execute(sql, val)

    # Realiza una consulta SELECT para obtener los datos de la tabla empleados
    mycursor.execute("SELECT * FROM empleados")
    empleados = mycursor.fetchall()
    for empleado in empleados:
        print(empleado)

    # Verifica si la tabla se ha creado correctamente
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
      print(x)

except Exception as error:
    print("Error {}".format(error))

finally:
    # Cierra la conexión
    if mydb.is_connected():
        mydb.close()
        print("Conexión cerrada")
