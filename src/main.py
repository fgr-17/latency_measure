#!/opt/venv/bin/python
import numpy as np
from calc_latency_signal_response import calculate_latency_from_files

base_dir = '/workspace'
app_path = f'{base_dir}/src/main.py'
audiofiles_path = f'{base_dir}/audiofiles'

loopback_signal = f'{audiofiles_path}/loopback/loopback-s.wav'
loopback_responses=(
    f'{audiofiles_path}/loopback/loopback-r1.wav',
    f'{audiofiles_path}/loopback/loopback-r2.wav',
    f'{audiofiles_path}/loopback/loopback-r3.wav',
    f'{audiofiles_path}/loopback/loopback-r4.wav',
    f'{audiofiles_path}/loopback/loopback-r5.wav'
)

latencies = np.zeros(len(loopback_responses))

print('Calculating latencies of loopbacks')
for i, response_file in enumerate(loopback_responses):
    latencies[i] = calculate_latency_from_files(loopback_signal, response_file, True)
    # print(f'latency[{i}] [ms] = {latencies[i]}')

latency_avg = np.average(latencies)
latency_std = np.std(latencies)

print(f'Average latency : {latency_avg:.2f} +/- {latency_std:.2}')



