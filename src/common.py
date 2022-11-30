''' common functions'''

import matplotlib.pyplot as plt
import sys
import getopt

from audiofiles import AudioFiles

def get_files():
  ''' read file path from cli '''
  argv = sys.argv[1:] 
  silent = False
  
  try:
    opts, args = getopt.getopt(argv, "s:r:S")
    
  except:
    print("Error")

  for opt, arg in opts:
    if opt in ['-s']:
      signal = arg
    elif opt in ['-r']:
      response = arg
    elif opt in ['-S']:
      silent = True

  return AudioFiles(signal, response), silent

def save_plot_buf(buf, path):
    ''' plot to file '''
    plt.clf()
    plt.plot(buf)
    plt.show()
    plt.savefig(path)