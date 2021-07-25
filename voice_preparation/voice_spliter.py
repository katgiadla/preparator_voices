import sys
import json
from math import ceil
import vosk
from librosa import load
import numpy as np
import pandas as pd
import os

def extract_words(JSON_content) -> list:
    result = []
    json_resources = json.loads(JSON_content)
    if 'result' in json_resources:
        result = json_resources['result']
    else:
        pass
    return result

def transcribe_words(recognizer, bytes) -> list:
    result = []

    chunk_size = 4000

    for no_chunk in range(ceil(len(bytes)/chunk_size)):
        start = no_chunk * chunk_size
        end = min(len(bytes), (no_chunk + 1) * chunk_size)
        data = bytes[start:end]

        if recognizer.AcceptWaveform(data):
            words = extract_words(recognizer.Result())
            result += words
    result += extract_words(recognizer.FinalResult())

    return result

def create_csv_file_with_times():

    try:
        audio_path = sys.argv[1]
        csv_path = sys.argv[2]
    except IndexError:
        print("Try again! You don't attach name of input or output file!")

    vosk.SetLogLevel(-1)

    model_path = 'vosk-model-small-de-0.15'
    sample_rate = 44100

    audio, sr = load(path=audio_path, sr=sample_rate)

    int16 = np.int16(audio * 32768).tobytes()

    if not os.path.exists(path=model_path):
        raise ValueError("Could not find VOSK model!")

    model = vosk.Model(model_path=model_path)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)

    res = transcribe_words(recognizer, int16)
    df = pd.DataFrame.from_records(res)
    # df = df.sort_values('start')

    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
    create_csv_file_with_times()