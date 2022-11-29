

''' Measure latency from 2 signals'''

from scipy import signal
import numpy as np
from common import save_plot_buf

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