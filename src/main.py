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


class LatencyMeasurement:

  def __init__(self, sgn, res, fs):
    self.sgn = sgn
    self.res = res
    self.fs = fs
    print(f'sgn shape {np.shape(sgn)}')
    print(f'res shape {np.shape(res)}')

    if len(self.sgn) < len(self.res):
      self.res = self.res[:len(self.sgn)]
    elif len(self.sgn) > len(self.res):
      self.sgn = self.sgn[:len(self.res)]

  def get_latency(self):
    print('Calculating the latency...')
    save_plot_buf(self.sgn, 'sgn.png')
    save_plot_buf(self.res, 'res.png')
    c = signal.correlate(self.sgn, self.res, mode='full', method='fft')
    # c = np.correlate(a=self.sgn, v=self.res)
    save_plot_buf(c, 'corr.png')
    print(f'corr: {c}')
    # search for the max and correct the zero padding
    peak = len(self.res) - np.argmax(c)
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

def save_plot_buf(buf, path):
    plt.clf()
    plt.plot(buf)
    plt.show()
    plt.savefig(path)

if __name__ == '__main__':

  files = get_files()

  s1 = AudioFile(files.signal)
  s2 = AudioFile(files.response)

  save_plot_buf(s1.buf, './s1.png')
  save_plot_buf(s2.buf, './s2.png')

  msr = LatencyMeasurement(s1.buf, s2.buf, s1.fs)
  msr.get_latency()

