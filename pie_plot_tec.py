import sqlite3
import matplotlib.pyplot as plt

def pie_plot_tec(database, fecha, hora):

    table='y'+fecha[-4:]
    con=sqlite3.connect(database)
    cursor=con.cursor()
    
    cursor.execute("SELECT "+table+".Unidad, "+table+".Tipo_Oferta, "+table+".'Energia_Compra/Venta', "+table+".'Precio_Compra/Venta', UNITEC.TEC from "+table+" INNER JOIN UNITEC ON "+table+".Unidad = UNITEC.CODIGO WHERE "+table+".Fecha='"+fecha+"' AND "+table+".Hora='"+hora+"' AND "+table+".'Tipo_Oferta'='V' AND "+table+".'Ofertada_(O)/Casada_(C)'='C' order by "+table+".'Precio_Compra/Venta' asc, "+table+".Unidad asc")    
    venta_asc=cursor.fetchall()

    tec=[]
    for i in venta_asc:
        tec.append(i[4])
        
    tecnologies=list(dict.fromkeys(tec))
    venta_acu=[0]*len(tecnologies)

    for i in tecnologies:
        for s in venta_asc:
            if i==s[4]:
                venta_acu[tecnologies.index(i)]+=s[2]
            else:
                pass
                    
    plt.pie(venta_acu,labels=tecnologies,autopct='%1.1f%%')
    plt.title("Tecnologías Casación "+fecha+" : Hora "+hora)
    plt.axis('equal')
    plt.show()
    


