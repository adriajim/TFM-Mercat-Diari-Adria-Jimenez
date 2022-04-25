import pandas as pd
import sqlite3
from os import listdir

def import_to_sql (database, tables, directory):

    con=sqlite3.connect(database)
    l=[]
    for t in tables:

        for file in listdir(directory):
          
            if file not in l:
                if file[14:18] == t[1:]:
                    
                    f=pd.read_csv(directory+'/'+file, sep='\t')
                    f.to_sql(t, con, if_exists='append',index=False)
                    l.append(file)
                else:
                    pass
                
            
            
        
