#!/opt/venv/bin/python

from scipy.io import wavfile
import sys
import getopt

class AudioFiles:
  def __init__(self, signal, response):
    self.signal = signal
    self.response = response

class AudioFile:

  def __init__(self, path):
    self.path = path
    self.read_wav()
    self.print_info()

  def read_wav(self):
    samplerate, data = wavfile.read(self.path)
    self.fs = samplerate
    raw_stereo_buf = data.astype(float)
    # get only left channel
    self.buf = raw_stereo_buf[:, 0]

  def print_fs(self):
    print(f'fs: {self.fs}')

  def print_buf(self):
    print(f'len: {len(self.buf)}')

  def print_info(self):
    self.print_fs()
    self.print_buf()


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

  s1 = AudioFile(files.signal)
  s2 = AudioFile(files.response)

