import csv
import pandas as pd



def using_builtin_libary(file):
     
     with open(file) as csv_file:
            
        csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', escapechar="\\")
        
        #previous_key=""    
        
        for row in csv_reader:
            print(row)
            
            
            
def using_pandas(file):
    
    data_frame = pd.read_csv(file, sep=',', quotechar='"',escapechar="\\")    
    
    for row in data_frame.itertuples(index=True, name='Pandas'):
        print(row)
        




using_builtin_libary("worldcities-free-100.csv")
using_pandas("worldcities-free-100.csv")