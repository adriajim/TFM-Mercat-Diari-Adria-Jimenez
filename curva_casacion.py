import sqlite3
import matplotlib.pyplot as plt

def curva_casacion(database, fecha, hora):

    table='y'+fecha[-4:]
    con=sqlite3.connect(database)
    cursor=con.cursor()
    
    cursor.execute("SELECT "+table+".Unidad, "+table+".Tipo_Oferta, "+table+".'Energia_Compra/Venta', "+table+".'Precio_Compra/Venta' from "+table+" WHERE "+table+".Fecha='"+fecha+"' AND "+table+".Hora='"+hora+"' AND "+table+".'Tipo_Oferta'='C' AND "+table+".'Ofertada_(O)/Casada_(C)'='C' order by "+table+".'Precio_Compra/Venta' desc, "+table+".Unidad asc")
    compra_desc=cursor.fetchall()

    cursor.execute("SELECT "+table+".Unidad, "+table+".Tipo_Oferta, "+table+".'Energia_Compra/Venta', "+table+".'Precio_Compra/Venta' from "+table+" WHERE "+table+".Fecha='"+fecha+"' AND "+table+".Hora='"+hora+"' AND "+table+".'Tipo_Oferta'='V' AND "+table+".'Ofertada_(O)/Casada_(C)'='C' order by "+table+".'Precio_Compra/Venta' asc, "+table+".Unidad asc")
    venta_asc=cursor.fetchall()

    compra_acu=[]
    venta_acu=[]

    for t in compra_desc:
        if len(compra_acu)==0:
            compra_acu.append((t[3],round(t[2],1)))
            c=t[2]
        else:
            compra_acu.append((t[3],round((t[2]+c),1)))
            c=compra_acu[-1][1]

    for s in venta_asc:
        if len(venta_acu)==0:
            venta_acu.append((s[3],round(s[2],1)))
            c=s[2]
        else:
            venta_acu.append((s[3],round((s[2]+c),1)))
            c=venta_acu[-1][1]

    precio_compra=[]
    acu_compra=[]

    precio_venta=[]
    acu_venta=[]

    for i in compra_acu:
        precio_compra.append(i[0])
        acu_compra.append(i[1])

    for i in venta_acu:
        precio_venta.append(i[0])
        acu_venta.append(i[1])

    print("Precio marginal: "+ str(precio_compra[-1])+" €/MWh")

    plt.plot(acu_compra,precio_compra)
    plt.plot(acu_venta,precio_venta)
    plt.xlabel("Energía [MWh]")
    plt.ylabel("Precio [€/MWh]")
    plt.title("Curva casación "+fecha+" : Hora "+hora)
    plt.legend(['Oferta de Venta', 'Oferta de Compra'])
    plt.show()
    


