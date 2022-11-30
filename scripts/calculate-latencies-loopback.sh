#!/bin/bash

BASE_DIR="/workspace"
APP_PATH="${BASE_DIR}/src/main.py"
AUDIOFILES_PATH="${BASE_DIR}/audiofiles"
loopback_signal="${AUDIOFILES_PATH}/loopback/loopback-s.wav"

loopback_responses=(
    "$AUDIOFILES_PATH/loopback/loopback-r1.wav"
    "$AUDIOFILES_PATH/loopback/loopback-r2.wav"
    "$AUDIOFILES_PATH/loopback/loopback-r3.wav"
    "$AUDIOFILES_PATH/loopback/loopback-r4.wav"
    "$AUDIOFILES_PATH/loopback/loopback-r5.wav"
)

analize_audio_list() {

    signal_file="$1"
    shift
    responses_list=("$@")
    
    latency_sum=0
    echo "signal file: ${signal_file}"

    for file in "${responses_list[@]}"
    do
        # echo "response file ${file}"
        # echo "${options[@]}"
        options=(-s "${signal_file}" -r "${file}" -S)
        latency=$(${APP_PATH} "${options[@]}" 2>/dev/null)
        latency_sum=`expr $latency_sum + $latency`
        echo "latency: $latency"
        echo "acc: $latency_sum"

    done
}

analize_audio_list $loopback_signal "${loopback_responses[@]}"