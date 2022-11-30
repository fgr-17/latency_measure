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
    
    echo "signal file: ${signal_file}"

    for file in "${responses_list[@]}"
    do
        echo "response file ${file}"
        options=(-s "${signal_file}" -r "${file}")
        echo "${options[@]}"
        ${APP_PATH} "${options[@]}"

    done
}

analize_audio_list $loopback_signal "${loopback_responses[@]}"