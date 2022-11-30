#!/opt/venv/bin/python

from common import get_files, save_plot_buf
from audiofile import AudioFile
from latency_measurement import LatencyMeasurement

def calculate_latency_from_files(sgn_path, res_path, silent):
  s1 = AudioFile(sgn_path)
  s2 = AudioFile(res_path)
  msr = LatencyMeasurement(s1.buf, s2.buf, s1.fs, silent)
  return msr.get_latency()

if __name__ == '__main__':
  files, silent = get_files()
  calculate_latency_from_files(files.signal, files.response, True)

