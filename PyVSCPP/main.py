import ctypes
import time

clibrary = ctypes.CDLL("./clibrary/InsertionSortInCPP.so")

def TimeEfficiency(func):
  '''
  Returns the total time 
  '''
  def wrapper(*args, **kwargs):
    startTime = time.time()
    func(*args, **kwargs)
    endTime = time.time()
    print(f" Start Time: {startTime} \n End Time: {endTime} \n Total Time: {endTime - startTime}\n")
    return endTime - startTime

  return wrapper

def OpenFile(fileName):
  file = open(fileName, "r").read().split()   
  for i in range(0, len(file)):
    file[i] = int(file[i])  

  return file  

@TimeEfficiency
def InsertionSortInCPP(arr):
  clibrary.InsertionSortInCPP.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int)
  clibrary.InsertionSortInCPP.restype = None

  c_array = (ctypes.c_int * len(arr))(*arr)
  
  clibrary.InsertionSortInCPP(c_array, len(c_array))     

@TimeEfficiency
def InsertionSortInPy(arr):
  '''
  Sort the Array using Insertion Sort
  '''
  comparisons = 0
  n = len(arr)  
  if n <= 1:
      return  
  for i in range(1, n): 
      key = arr[i]  
      j = i-1
      while j >= 0 and key < arr[j]: 
          comparisons += 1
          arr[j+1] = arr[j]  
          j -= 1          
      arr[j+1] = key  
  print(f"Total Amount of Comparisons For Insertion Sort in Py: {comparisons}") 
  
def main():

    fileNames = ['data/1000.txt', 'data/5000.txt', 'data/10000.txt', 'data/15000.txt', 'data/20000.txt', 'data/25000.txt', 'data/30000.txt', 'data/35000.txt', 'data/40000.txt', 'data/45000.txt', 'data/50000.txt', 'data/55000.txt', 'data/60000.txt', 'data/65000.txt', 'data/70000.txt', 'data/75000.txt', 'data/80000.txt', 'data/85000.txt', 'data/90000.txt', 'data/95000.txt', 'data/100000.txt']

    pyResults = []
    cppResults = []

    for fileName in fileNames:  
      print(f"=========={fileName[5:fileName.find('.')] if '.' in fileName else fileName}==========")
      file = OpenFile(fileName)

      totalTime = InsertionSortInCPP(file)
      cppResults.append(totalTime) 

      totalTime = InsertionSortInPy(file)  
      pyResults.append(totalTime) 

    print(f"CPP Insertion Sort: {cppResults}")
    print(f"Py Insertion Sort: {pyResults}")
    
    return 0
    
main()     