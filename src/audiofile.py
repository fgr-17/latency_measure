''' Audio file basic handling '''

import numpy as np
from scipy.io import wavfile

class AudioFile:
  ''' class to manage audio files'''

  def __init__(self, path):
    ''' read the file, print info and normalize to peak '''
    self.path = path
    self.read_wav()
    # self.print_info()
    self.normalize()

  def read_wav(self):
    ''' read wav from path and force to mono if stereo '''
    samplerate, data = wavfile.read(self.path)
    self.fs = samplerate
    raw_stereo_buf = data.astype(float)
    # get only left channel if stereo
    if(raw_stereo_buf.ndim == 2):
      self.buf = raw_stereo_buf[:, 0]
    else:
      self.buf = raw_stereo_buf

  def print_fs(self):
    ''' print sampling frequency '''
    print(f'fs: {self.fs}')

  def print_buf(self):
    ''' print data buf '''
    print(f'len: {len(self.buf)}')

  def print_path(self):
    ''' print file path '''
    print(f'path: {self.path}')

  def print_max(self):
    ''' print max of data '''
    print(f'max: {np.argmax(self.buf)}')

  def print_info(self):
    ''' print all info '''
    self.print_path()
    self.print_fs()
    self.print_buf()
    self.print_max()

  def normalize(self):
    ''' normalize the signal by its peak (order 0) '''
    self.max = self.buf[np.argmax(self.buf)]
    self.buf = self.buf / self.max