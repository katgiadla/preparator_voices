import unittest

from pydub import AudioSegment
import voice_spliter

class MyTestCase(unittest.TestCase):
    def test_get_AudioSegment_From_MP3(self):
        self.assertIsInstance(type(voice_spliter.check_file("D:\\preparator_voices\\test_files\\test_file_1.mp3")), AudioSegment)

if __name__ == '__main__':
    unittest.main()