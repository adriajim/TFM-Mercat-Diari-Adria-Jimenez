from os import listdir
from os import chdir

def replace_to_csv (directory):
    l=[]
    chdir(directory)
    for file in listdir(directory):
        if file not in l:
            fin=open(file,"r")
            fout=open(file[:-2]+".csv","w")

            buff=fin.read()
            rbuff=buff.replace(";","\t")

            fout.write(rbuff)

            fin.close()
            fout.close()

            l.append(file)
        
        
            
            
