#!/opt/venv/bin/python
import numpy as np
from calc_latency_signal_response import calculate_latency_from_files

base_dir = '/workspace'
app_path = f'{base_dir}/src/main.py'
audiofiles_path = f'{base_dir}/audiofiles'
loopback_path = f'{audiofiles_path}/loopback/120522'
linein_lq_path = f'{audiofiles_path}/linein-lq'

loopback_signal = f'{loopback_path}/signal.wav'
loopback_responses=(
    f'{loopback_path}/loopback1.wav',
    f'{loopback_path}/loopback2.wav',
    f'{loopback_path}/loopback3.wav',
    f'{loopback_path}/loopback4.wav',
    f'{loopback_path}/loopback5.wav'
)

loopback_compensated=(
    f'{loopback_path}/loopback-comp1.wav',
    f'{loopback_path}/loopback-comp2.wav',
    f'{loopback_path}/loopback-comp3.wav',
    f'{loopback_path}/loopback-comp4.wav',
    f'{loopback_path}/loopback-comp5.wav'
)

linein_lq_6b=(
    f'{linein_lq_path}/linein-lq-1.wav',
    f'{linein_lq_path}/linein-lq-2.wav',
    f'{linein_lq_path}/linein-lq-3.wav',
    f'{linein_lq_path}/linein-lq-4.wav',
    f'{linein_lq_path}/linein-lq-5.wav'
)

linein_lq_2b=(
    f'{linein_lq_path}/linein-lq-2buf-1.wav',
    f'{linein_lq_path}/linein-lq-2buf-2.wav',
    f'{linein_lq_path}/linein-lq-2buf-3.wav',
    f'{linein_lq_path}/linein-lq-2buf-4.wav',
    f'{linein_lq_path}/linein-lq-2buf-5.wav'
)

def latency_stats(signal_path, responses_path_list):

    latencies = np.zeros(len(responses_path_list))

    for i, response_file in enumerate(responses_path_list):
        latencies[i] = calculate_latency_from_files(signal_path, response_file, True)
        # print(f'latency[{i}] [ms] = {latencies[i]}')

    latency_avg = np.average(latencies)
    latency_std = np.std(latencies)

    return latency_avg, latency_std

print('\nCalculating loopback latency')
loopback_avg, loopback_std = latency_stats(loopback_signal, loopback_responses)
print(f'Average latency : {loopback_avg:.2f} +/- {loopback_std:.2}')

print('\nCalculating compensated loopback latency')
loopback_c_avg, loopback_c_std = latency_stats(loopback_signal, loopback_compensated)
print(f'Average latency [compensated] : {loopback_c_avg:.2f} +/- {loopback_c_std:.2}')

print('\nCalculating LineIn to 4W latency[6 playback buffers]:')
linein_lq_6b_avg, linein_lq_6b_c_std = latency_stats(loopback_signal, linein_lq_6b)
print(f'LineIn - HS latency: {linein_lq_6b_avg:.2f} +/- {linein_lq_6b_c_std:.2}')

print('\nCalculating LineIn to 4W latency[2 playback buffers]:')
linein_lq_2b_avg, linein_lq_2b_c_std = latency_stats(loopback_signal, linein_lq_2b)
print(f'LineIn - HS latency: {linein_lq_2b_avg:.2f} +/- {linein_lq_2b_c_std:.2}')

