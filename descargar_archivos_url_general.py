import requests
from os import listdir
from datetime import datetime, timedelta

print(
    '''
    inidate: data inicial del període (format tupla: (dd,mm,yyyy))
    findate: data final del període (format tupla: (dd,mm,yyyy))
    directory: path del directori on desitja desar els fitxers
    '''
    )

def download_files(inidate,findate,directory):

    d1=datetime(inidate[0],inidate[1],inidate[2])
    d2=datetime(findate[0],findate[1],findate[2])
    dif=d2-d1
    list_date=[d1.strftime('%Y-%m')]
   
    for d in range(dif.days+1):
        list_date.append((d1 + timedelta(days=d)).strftime('%Y-%m'))

    result = []
    for item in list_date:
        if item not in result:
            result.append(item)
 
    l=[];
    for file in listdir(directory):
        l.append (file[:21])
     
    for t in result:
        url="https://www.omie.es/es/file-download?parents%5B0%5D=curva_pbc_uof&filename=curva_pbc_uof_"+t[:4]+t[-2:]+".zip";
        ubi=directory + r"\curva_pbc_uof_" + t[:4] + t[-2:] + ".zip"
        if url[-24:-4] not in l:
            myfile=requests.get(url)
            open(ubi,'wb').write(myfile.content)
     
            
  



