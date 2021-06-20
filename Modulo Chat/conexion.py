import mysql.connector

class conexion:

    def Conectar(self, user, password):
        conexion=mysql.connector.connect(host="localhost", 
                                              user=user, 
                                              passwd=password, 
                                              database="tesis2")
        print("Conexion establecida")
        return conexion

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion, precio from articulos where codigo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()