#!/opt/venv/bin/python

import matplotlib.pyplot as plt

from scipy.io import wavfile
from scipy import signal

import sys
import getopt
import numpy as np


class AudioFiles:
  def __init__(self, signal, response):
    self.signal = signal
    self.response = response

class AudioFile:

  def __init__(self, path):
    self.path = path
    self.read_wav()
    self.print_info()
    self.normalize()

  def read_wav(self):
    samplerate, data = wavfile.read(self.path)
    self.fs = samplerate
    raw_stereo_buf = data.astype(float)
    # get only left channel if stereo
    if(raw_stereo_buf.ndim == 2):
      self.buf = raw_stereo_buf[:, 0]
    else:
      self.buf = raw_stereo_buf

  def print_fs(self):
    print(f'fs: {self.fs}')

  def print_buf(self):
    print(f'len: {len(self.buf)}')

  def print_path(self):
    print(f'path: {self.path}')

  def print_max(self):
    print(f'max: {np.argmax(self.buf)}')

  def print_info(self):
    self.print_path()
    self.print_fs()
    self.print_buf()
    self.print_max()

  def normalize(self):
    self.max = self.buf[np.argmax(self.buf)]
    self.buf = self.buf / self.max

  def save_plot_buf(self, path):
    plt.clf()
    plt.plot(self.buf)
    plt.show()
    plt.savefig(path)

class LatencyMeasurement:

  def __init__(self, sgn, res, fs):
    self.sgn = sgn
    self.res = res
    self.fs = fs

    if len(self.sgn) < len(self.res):
      self.res = self.res[:len(self.sgn)]
    elif len(self.sgn) > len(self.res):
      self.sgn = self.sgn[:len(self.res)]

  def get_latency(self):
    c = signal.correlate(self.sgn, self.res, mode='valid', method='fft')
    peak = np.argmax(c)
    print(f'sgn len: {len(self.sgn)} - res len : {len(self.res)}')
    print(f'peak {peak}')

def get_files():

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

  s1 = AudioFile(files.signal)
  s2 = AudioFile(files.response)

  s1.save_plot_buf('./s1.png')
  s2.save_plot_buf('./s2.png')

  msr = LatencyMeasurement(s1.buf, s2.buf, s1.fs)
  msr.get_latency()

