import unittest
from text_preparotion.transcription_loader import *

class TestTranscritpionLoader(unittest.TestCase):
    def setUp(self) -> None:
        self.test_path_to_docx = 'D:\\preparator_voices\\test_files\\test.docx'
        self.test_failed_path_to_docx = 'D:\\preparator_voices\\test_files\\test1.docx'
        self.test_path_to_txt = 'D:\\preparator_voices\\test_files\\test.txt'
        self.test_failed_path_to_txt = 'D:\\preparator_voices\\test_files\\test1.txt'
        self.test_empty_transcription = []
        self.test_one_line_transcription_with_special_chars = ['Witaj, bo przemądrzali stali się głupcami\n']
        self.test_one_line_transcription_without_special_chars = ['Witaj raju pragnących zbawienia']
        self.test_two_lines_transcription = ['Policjanci nie przebywają z politykami na codzień', 'Szyby, skrobiemy']

    def test_docx_document_not_exist(self):
        self.assertRaises(FileNotFoundError, open_docx_transcription, self.test_failed_path_to_docx)

    def test_docx_document_exists(self):
        self.assertListEqual(['To jest przykładowy tekst'], open_docx_transcription(self.test_path_to_docx))

    def test_txt_document_not_exist(self):
        self.assertRaises(FileNotFoundError, open_txt_transcription, self.test_failed_path_to_txt)

    def test_txt_document_exists(self):
        self.assertListEqual(['Nie prowadzimy psychoterapii\n', 'no Twój kuzyn stanowisko dostał umlaüt'],
                             open_txt_transcription(self.test_path_to_txt))

    def test_split_transcriptions_lines_list_empty_list(self):
        self.assertRaises(EmptyListError.EmptyListError, split_lines_to_words, [])

    def test_split_transcription_lines_one_line_without_special_chars(self):
        self.assertListEqual(['Witaj', 'raju', 'pragnących', 'zbawienia'],
                             split_lines_to_words(self.test_one_line_transcription_without_special_chars))

    def test_split_transcription_lines_one_line_with_special_chars(self):
        self.assertListEqual(['Witaj,', 'bo', 'przemądrzali', 'stali', 'się', 'głupcami\n'],
                             split_lines_to_words(self.test_one_line_transcription_with_special_chars))

    def test_split_transcription_lines_more_lines(self):
        self.assertListEqual(['Policjanci', 'nie', 'przebywają', 'z', 'politykami', 'na', 'codzień', 'Szyby,', 'skrobiemy'],
                             split_lines_to_words(self.test_two_lines_transcription))

    def test_cleaning_more_whitespace(self):
        self.assertListEqual(['Witaj', 'bo', 'przemądrzali', 'stali', 'się', 'głupcami'],
                             cleaning_transcription_list(['Witaj,', 'bo', 'przemądrzali', 'stali', 'się', 'głupcami\n']))

if __name__ == '__main__':
    unittest.main()
