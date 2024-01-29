import sys
import os.path
import pandas as pd

print("version: " + str(pd.__version__))

fileToConvert = sys.argv[1]
fileName = fileToConvert.split('.')[0]


def xlsxToCsvConverter(inFile):
    if(os.path.isfile(inFile+".csv")):
        os.remove(inFile+'.csv')
        
    readInExcel = pd.read_excel(inFile+".xlsx", 
                                    header=0)
    readInExcel.to_csv(inFile+".csv",
                       index=None,
                       header=True)
    
    print("File exists: " + str(os.path.isfile(inFile+".csv")))


xlsxToCsvConverter(fileName)

