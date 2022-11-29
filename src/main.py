#!/opt/venv/bin/python

from common import get_files, save_plot_buf
from audiofile import AudioFile
from latency_measurement import LatencyMeasurement


if __name__ == '__main__':

  files = get_files()

  s1 = AudioFile(files.signal)
  s2 = AudioFile(files.response)

  save_plot_buf(s1.buf, './s1.png')
  save_plot_buf(s2.buf, './s2.png')

  msr = LatencyMeasurement(s1.buf, s2.buf, s1.fs)
  msr.get_latency()

