from pydub import AudioSegment
from pydub.silence import split_on_silence

def check_file(path: str) -> AudioSegment:
    ext = path.split(".")[1]
    return {
        "wav": lambda path: AudioSegment.from_wav(path),
        "mp3": lambda path: AudioSegment.from_mp3(path)}.get(ext)(path)


def split_voice(path: str):
    record = check_file()

