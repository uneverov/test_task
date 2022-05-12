import os
import pdfplumber as pdfplumber

pdf_path = rf'{os.getcwd()}/pdf_files/test_task.pdf'


def get_substring(content: str,
                  start: str,
                  end: str) -> str:
    """
    Получаем часть строки
    :param content:
    :param start:
    :param end:
    :return:
    """
    return (content[content.find(start) + len(start):content.
            rfind(end)].replace('\n', '').rstrip())


def test_check_pdf(pdf_data,
                   json_data):
    """
    Проверяет наличие элементов (слов-ключей) в pdf
    Не проверяет наличие штрихкодов
    """
    elements = json_data
    words = pdf_data
    for element in elements.values():
        assert element in words, ('Не все обязательные элементы'
                                  'присутсвуют на странице согласно структуре')


def get_dict_from_pdf(pdf_path: str) -> dict:
    """
    Читает текст с pdf и возвращает словарь со значениями
    :param pdf_path: путь до pdf файла
    """
    doc_content = {}
    with pdfplumber.open(pdf_path) as pdf:
        pdf_content = pdf.pages[0].extract_text().replace('\n', ' ')

    doc_content['DOC_NAME'] = get_substring(pdf_content,
                                            '',
                                            'PN:')
    doc_content['PN'] = get_substring(pdf_content,
                                      'PN: ',
                                      'SN:')
    doc_content['SN'] = get_substring(pdf_content,
                                      'SN:',
                                      'DESCRIPTION:')
    doc_content['DESCRIPTION'] = get_substring(pdf_content,
                                               'DESCRIPTION: ',
                                               'LOCATION:')
    doc_content['LOCATION'] = get_substring(pdf_content,
                                            'LOCATION: ',
                                            'CONDITION:')
    doc_content['CONDITION'] = get_substring(pdf_content,
                                             'CONDITION: ',
                                             'RECEIVER#:')
    doc_content['RECEIVER#'] = get_substring(pdf_content,
                                             'RECEIVER#: ',
                                             'UOM:')
    doc_content['UOM'] = get_substring(pdf_content,
                                       'UOM: ',
                                       'EXP DATE:')
    doc_content['EXP DATE'] = get_substring(pdf_content,
                                            'EXP DATE: ',
                                            'PO:')
    doc_content['PO'] = get_substring(pdf_content,
                                      'PO: ',
                                      'CERT SOURCE:')
    doc_content['CERT SOURCE'] = get_substring(pdf_content,
                                               'CERT SOURCE: ',
                                               'REC.DATE:')
    doc_content['REC.DATE'] = get_substring(pdf_content,
                                            'REC.DATE: ',
                                            'MFG:')
    doc_content['MFG'] = get_substring(pdf_content,
                                       'MFG: ',
                                       'BATCH# :')
    doc_content['BATCH#'] = get_substring(pdf_content,
                                          'BATCH# : ',
                                          'DOM:')
    doc_content['DOM'] = get_substring(pdf_content,
                                       'DOM: ',
                                       'REMARK:')
    doc_content['REMARK'] = get_substring(pdf_content,
                                          'REMARK: ',
                                          'LOT# :')
    doc_content['LOT#'] = get_substring(pdf_content,
                                        'LOT# : ',
                                        ' TAGGED BY:')
    doc_content['TAGGED BY'] = get_substring(pdf_content,
                                             'TAGGED BY: ',
                                             'NOTES:')
    doc_content['NOTES'] = get_substring(pdf_content,
                                         'NOTES: ',
                                         'Qty:')
    doc_content['Qty'] = get_substring(pdf_content,
                                       'Qty: ',
                                       '')
    return doc_content


files = os.listdir(rf'{os.getcwd()}/pdf_files')
for file in files:
    print(get_dict_from_pdf(rf'{os.getcwd()}/pdf_files/' + file))
