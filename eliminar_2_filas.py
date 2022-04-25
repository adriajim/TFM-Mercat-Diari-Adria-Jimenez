from os import listdir

def delete_lines (directory,ini,n):
    l=[]
    for file in listdir(directory):
        if file not in l:
            f=open(file,"r")
            lineas = f.readlines()
            f.close()
            
            f=open(file,"w")
            for i in range(ini,len(lineas)-n):
                f.write(lineas[i+n])
            f.close()
            l.append(file)
        
        
            
            
