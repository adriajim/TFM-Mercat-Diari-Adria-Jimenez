import sqlite3

print(
    '''name = nom de la base de dades ('database.db')''''
    '''years = tupla amb els noms dels anys  que formaràn les taules ('''2016''')'''
    )

def crear_database(name, years):

    connection = sqlite3.connect(name)
    cursor = connection.cursor()

    for c in years:
        cursor.execute('''CREATE TABLE IF NOT EXISTS y'''+c+''' ("Hora" INTEGER,"Fecha" TEXT,"Pais" TEXT,"Unidad" TEXT,"Tipo_Oferta" TEXT,"Energia_Compra/Venta" REAL,"Precio_Compra/Venta" REAL,"Ofertada_(O)/Casada_(C)" TEXT)''')

    connection.commit()
    connection.close()
