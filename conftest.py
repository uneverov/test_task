import json
import os

import pdfplumber
import pytest


@pytest.fixture
def json_data():
    """
    Передаем данные для теста из json файла
    :return:
    """
    with open(rf'{os.getcwd()}/elements_for_checking.json', 'r') as f:
        elements = dict(json.load(f))
    return elements


@pytest.fixture
def pdf_data():
    """
    Передаем в теasdсasdasdт координаты всех слов в pdf файле
    :return:
    """
    with pdfplumber.open(rf'{os.getcwd()}/pdf_files/test_task.pdf') as pdf:
        words = pdf.pages[0].extract_words()
    return words
