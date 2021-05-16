from docx import Document

def open_docx_transcription(path: str) -> list:
    """

    Opening docx file and save each one word of transcription to list.
    If document doesn't exist is thrown FileNotFoundException.

    Args:
        path (str): path to docx file

    Returns:
        transcription_list (list):  list of transcritptions' paragraphs

    """
    transcription_list = []

    try:
        transcript = Document(path)
    except:
        transcript = Document()

    for paragraph in transcript.paragraphs:
        transcription_list.append(paragraph.text)

    if len(transcription_list) == 0:
        raise FileNotFoundError("Document doesn't exist!")

    return transcription_list

def open_txt_transcription(path: str) -> list:
    """
    Opening txt file and save each one word of transcription to list.
    If document doesn't exist is thrown FileNotFoundException.

    Args:
        path (str): path to txt file

    Returns:
        transcription_list (list):  list of transcritptions' lines

    """
    transcription_list = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            transcription_list = file.readlines()
        file.close()
    except FileNotFoundError:
        print("File doesn't exist!")
        raise

    return transcription_list

def check_type_of_description(path: str):
    scenario = 0
    #if under try block
    return scenario

#TODO cleaning transcription list