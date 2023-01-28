import os
folder_name = 'Text files'
catalog = sorted(os.listdir(folder_name))


def concatenate_files(catalog):
    d_text = {}   # создание словаря "{кол-во строк файла: имя файла}"
    for text in catalog:
        text_path = os.path.join(os.getcwd(), folder_name, text)
        with open(text_path, 'r', encoding='utf8') as t:
            d_text |= {len(t.readlines()): text}
    sorted_d_text = dict(sorted(d_text.items(), key=lambda x: x[0]))  # сортировка словаря по возрастанию ключа

    with open('res.txt', 'w', encoding='utf8') as res:  # запись в файл 'res.txt' служебной информации
        for len_t, name in sorted_d_text.items():
            name_path = os.path.join(os.getcwd(), folder_name, name)
            res.writelines(f'{name}\n{str(len_t)}\n')
            with open(name_path, 'r', encoding='utf8') as file:  # запись в файл 'res.txt' информации из файлов
                res.writelines(file)
                res.writelines('\n')


concatenate_files(catalog)
