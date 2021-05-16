import unittest

from docx.opc.exceptions import PackageNotFoundError

from transcription_loader import open_docx_transcription, open_txt_transcription

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testpathtodocx = 'D:\\preparator_voices\\test_files\\test.docx'
        self.failedtestpathtodocx = 'D:\\preparator_voices\\test_files\\test1.docx'
        self.testpathtotxt = 'D:\\preparator_voices\\test_files\\test.txt'
        self.failedtestpathtotxt = 'D:\\preparator_voices\\test_files\\test1.txt'

    def test_docx_document_not_exist(self):
        self.assertRaises(FileNotFoundError, open_docx_transcription, self.failedtestpathtodocx)

    def test_docx_document_exists(self):
        self.assertListEqual(['To jest przykładowy tekst'], open_docx_transcription(self.testpathtodocx))

    def test_txt_document_not_exist(self):
        self.assertRaises(FileNotFoundError, open_txt_transcription, self.failedtestpathtotxt)

    def test_txt_document_exists(self):
        self.assertListEqual(['Nie prowadzimy psychoterapii\n', 'no Twój kuzyn stanowisko dostał umlaüt'],
                             open_txt_transcription(self.testpathtotxt))

if __name__ == '__main__':
    unittest.main()
