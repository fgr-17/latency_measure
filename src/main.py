#!/opt/venv/bin/python

from scipy.io import wavfile
import sys
import getopt

class AudioFiles:
  def __init__(self, signal, response):
    self.signal = signal
    self.response = response

def get_files():

  print("Hola")
  argv = sys.argv[1:] 
  
  try:
    opts, args = getopt.getopt(argv, "s:r:")
    
  except:
    print("Error")

  for opt, arg in opts:
    if opt in ['-s']:
      signal = arg
    elif opt in ['-r']:
      response = arg

  return AudioFiles(signal, response)

if __name__ == '__main__':
  files = get_files()
  print(f'signal: {files.signal}')
  print(f'response: {files.response}')