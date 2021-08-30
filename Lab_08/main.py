print("////////////_ZAD1_/////////////")
def readFile(file_in,n):
  with open(file_in) as file:
    getLines = file.readlines()
  print("n początkowych wierszy pliku\n",getLines[:n])
  print("n końcowych wierszy pliku\n",getLines[-n:])
  print("co n-tego wiersza pliku\n",getLines[::n])
  print("n-tego słowa ze wszystkich wierszy\n",[line.split(" ")[n-1] for line in getLines])
  print("n-tego znaku ze wszystkich wierszy\n",[line[n-1] for line in getLines])
readFile("2000.txt",2)

print("////////////_ZAD2_/////////////")
import numpy
import glob
listData = glob.glob('data*.in')
listOut = open('data.out','w+')
allLines = []
for file_name in listData:
  lines=[]
  fileRead = open(file_name, 'r')
  for i in fileRead.readlines():
    lines.append(float(i))
  for j in range(len(lines)):
    if len(allLines) <= j:
      allLines.append([])    
    allLines[j].append(lines[j])
  fileRead.close()
for row in range(len(allLines)):
  listOut.write(str(row)+"   "+str(numpy.average(allLines[row]))+"   "+str(numpy.std(allLines[row]))+"\n")
listOut.close()

