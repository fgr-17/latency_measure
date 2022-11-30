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

loopback_compensated=(
    f'{audiofiles_path}/loopback/loopback-r-c1.wav',
    f'{audiofiles_path}/loopback/loopback-r-c2.wav',
    f'{audiofiles_path}/loopback/loopback-r-c3.wav'
)

def latency_stats(signal_path, responses_path_list):

    latencies = np.zeros(len(responses_path_list))

    for i, response_file in enumerate(responses_path_list):
        latencies[i] = calculate_latency_from_files(signal_path, response_file, True)
        # print(f'latency[{i}] [ms] = {latencies[i]}')

    latency_avg = np.average(latencies)
    latency_std = np.std(latencies)

    return latency_avg, latency_std

print('Calculating latencies of loopbacks')
loopback_avg, loopback_std = latency_stats(loopback_signal, loopback_responses)
print(f'Average latency : {loopback_avg:.2f} +/- {loopback_std:.2}')

loopback_c_avg, loopback_c_std = latency_stats(loopback_signal, loopback_compensated)
print(f'Average latency [compensated] : {loopback_c_avg:.2f} +/- {loopback_c_std:.2}')


