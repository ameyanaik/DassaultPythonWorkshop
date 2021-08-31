#/Users/ameya/Projects/DassaultPythonWorkshop
import sys
print(sys.path)
sys.path.append("/Users/ameya/Projects/DassaultPythonWorkshop")

from fileio.utils import read_csv

mycsv = read_csv("/Users/ameya/Projects/DassaultPythonWorkshop/fileio/test.csv")

print(mycsv)