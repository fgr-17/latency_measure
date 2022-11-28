#!/opt/venv/bin/python

from scipy.io import wavfile
import sys
import getopt

def full_name():

  print("Hola")
  argv = sys.argv[1:] 
  
  try:
    opts, args = getopt.getopt(argv, "f:l:")
    
  except:
    print("Error")

  for opt, arg in opts:
    if opt in ['-f']:
      first_name = arg
    elif opt in ['-l']:
      last_name = arg
    
  print( first_name +" " + last_name)

if __name__ == '__main__':
  full_name()