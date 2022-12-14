#!/opt/venv/bin/python
import numpy as np
from calc_latency_signal_response import calculate_latency_from_files

base_dir = '/workspace'
app_path = f'{base_dir}/src/main.py'
audiofiles_path = f'{base_dir}/audiofiles'
loopback_path = f'{audiofiles_path}/loopback/120522'
loopback_path_141222 = f'{audiofiles_path}/loopback/141222'
linein_lq_path = f'{audiofiles_path}/linein-lq'

loopback_signal = f'{loopback_path}/signal.wav'
loopback_responses=(
    f'{loopback_path}/loopback1.wav',
    f'{loopback_path}/loopback2.wav',
    f'{loopback_path}/loopback3.wav',
    f'{loopback_path}/loopback4.wav',
    f'{loopback_path}/loopback5.wav'
)

loopback_responses_141222=(
    f'{loopback_path_141222}/loopback141222_1900_1.wav',
    f'{loopback_path_141222}/loopback141222_1900_2.wav',
    f'{loopback_path_141222}/loopback141222_1900_3.wav',
    f'{loopback_path_141222}/loopback141222_1900_4.wav',
    f'{loopback_path_141222}/loopback141222_1900_5.wav'
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

linein_lq_21327=(
    f'{linein_lq_path}/lin-lq-2.13.27-base-1.wav',
    f'{linein_lq_path}/lin-lq-2.13.27-base-2.wav',
    f'{linein_lq_path}/lin-lq-2.13.27-base-3.wav',
    f'{linein_lq_path}/lin-lq-2.13.27-base-4.wav',
    f'{linein_lq_path}/lin-lq-2.13.27-base-5.wav'
)

linein_lq_21327_jbuf=(
    f'{linein_lq_path}/linein_lq_21327_jbuf_1.wav',
    f'{linein_lq_path}/linein_lq_21327_jbuf_2.wav',
    f'{linein_lq_path}/linein_lq_21327_jbuf_3.wav',
    f'{linein_lq_path}/linein_lq_21327_jbuf_4.wav',
    f'{linein_lq_path}/linein_lq_21327_jbuf_5.wav'
)

def latency_stats(signal_path, responses_path_list):

    latencies = np.zeros(len(responses_path_list))

    for i, response_file in enumerate(responses_path_list):
        latencies[i] = calculate_latency_from_files(signal_path, response_file, True)
        # print(f'latency[{i}] [ms] = {latencies[i]}')

    latency_avg = np.average(latencies)
    latency_std = np.std(latencies)

    return latency_avg, latency_std


def show_results(message, signal, responses, offset=0):
    print(f'\nCalculating latency: {message}')
    avg, std = latency_stats(signal, responses)
    print(f'Average latency : {(avg - offset):.2f} +/- {(std):.2}')    
    return avg


show_results('Initial loopback latency', loopback_signal, loopback_responses)
show_results('Initial compensated loopback latency', loopback_signal, loopback_compensated)
show_results('LineIn to 4W latency[6 playback buffers]', loopback_signal, linein_lq_6b)
show_results('LineIn to 4W latency[2 playback buffers]', loopback_signal, linein_lq_2b)
loopback_141222 = show_results('Loopback latency[12.14.22 19:30 ARG]', loopback_signal, loopback_responses_141222)
show_results('LineIn to 4W latency[2.13.27 Baseline]', loopback_signal, linein_lq_21327, loopback_141222)
show_results('LineIn to 4W latency[2.13.27 Jitter Buffer reduced]', loopback_signal, linein_lq_21327_jbuf, loopback_141222)