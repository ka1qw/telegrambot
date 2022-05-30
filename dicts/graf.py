graf = {
    'Лаб. физики океана': ['05'],
    '06': ['05'],
    '05': ['Лаб. физики океана', '06', '07'],
    '07': ['05', '08'],
    '08': ['07', 'Левая лестница цоколь'],
    'Левая лестница цоколь': ['Левая лестница 1 этаж', 'Левая лестница 2 этаж', 'Левая лестница 3 этаж', '08'],
    'Левая лестница 1 этаж': ['Левая лестница цоколь', 'Левая лестница 2 этаж', 'Левая лестница 3 этаж', '109'],
    '109': ['Левая лестница 1 этаж', 'Кафедра ВТИ'],
    'Кафедра ВТИ': ['109', '108'],
    '108': ['Кафедра ВТИ', '105'],
    '105': ['108', 'Лестница 1 этаж', 'Арка'],
    'Лестница 1 этаж': ['105', 'Арка', 'Вестибюль', '115', '104', 'Лестница 2 этаж', 'Лестница 3 этаж'],
    'Вестибюль': ['Гардероб', 'Лестница 1 этаж'],
    'Гардероб': ['Вестибюль'],
    '115': ['Лестница 1 этаж'],
    '104': ['Лестница 1 этаж', '102'],
    '102': ['Столовая', '104', 'Правая лестница 1 этаж'],
    'Столовая': ['102'],
    'Правая лестница 1 этаж': ['101', 'Правая лестница цоколь', 'Правая лестница 2 этаж', 'Правая лестница 3 этаж'],
    '101': ['Правая лестница 1 этаж'],
    'Правая лестница цоколь': ['18а', '025','Правая лестница 1 этаж', 'Правая лестница 2 этаж', 'Правая лестница 3 этаж'],
    '18а': ['Правая лестница цоколь'],
    '025': ['Правая лестница цоколь', '024'],
    '024': ['023', '025'],
    '023': ['024'],
    'Арка': ['105', 'Лестница 1 этаж', 'Кафедра океанологии'],
    'Кафедра океанологии': ['Арка', 'Проход'],
    'Проход': ['Кафедра океанологии', '117', '116', 'Задняя лестница 1 этаж'],
    '117': ['Проход'],
    '116': ['Проход'],
    'Задняя лестница 1 этаж': ['Внутренний двор', 'Задняя лестница 2 этаж', 'Задняя лестница 3 этаж'],
    'Внутренний двор': ['Задняя лестница 1 этаж', 'Центральный вход', 'Левый вход'],
    'Левый вход': ['Внутренний двор', 'Дверь по левой стене'],
    'Дверь по левой стене': ['Проход 2', 'Левый вход'],
    'Проход 2': ['Кафедра ВМиИ', 'Дверь по левой стене'],
    'Кафедра ВМиИ': ['Проход 2', '14 квартира'],
    '14 квартира': ['Кафедра ВМиИ'],
    'Центральный вход': ['Внутренний двор', 'Библиотека', 'Архив'],
    'Архив': ['Центральный вход'],
    'Библиотека': ['Центральный вход'],
    'Задняя лестница 2 этаж': ['Задняя лестница 1 этаж', 'Задняя лестница 3 этаж', 'Внутренний двор', 'Дирекция ИИСиГТ',
                               '406а'],
    'Дирекция ИИСиГТ': ['Задняя лестница 2 этаж', '406а'],
    '406а': ['Дирекция ИИСиГТ', '406б', 'Задняя лестница 2 этаж'],
    '406б': ['406а'],
    'Задняя лестница 3 этаж': ['Задняя лестница 1 этаж', 'Задняя лестница 2 этаж', 'Внутренний двор', 'Кафедра ПИ',
                               '317а'],
    'Кафедра ПИ': ['Задняя лестница 3 этаж', '317а'],
    '317а': ['Задняя лестница 3 этаж', 'Кафедра ПИ', '317б'],
    '317б': ['317а', 'Кафедра ИТиСБ'],
    'Кафедра ИТиСБ': ['317б'],
    'Левая лестница 2 этаж': ['Левая лестница 1 этаж', 'Левая лестница цоколь', 'Левая лестница 3 этаж',
                              'Кабинет геологии', '212'],
    'Кабинет геологии': ['Левая лестница 2 этаж', 'Кафедра МИС', '212'],
    '212': ['Кабинет геологии', '210', 'Левая лестница 2 этаж'],
    'Кафедра МИС': ['Кабинет геологии', '210'],
    '210': ['Кафедра МИС', '212', '209а'],
    '209а': ['210', '209', '208'],
    '209': ['209а'],
    '208': ['209', '207'],
    '207': ['208', '206'],
    '206': ['207', '205', 'Лестница 2 этаж', 'Проход 3'],
    'Лестница 2 этаж': ['Лестница 1 этаж', 'Лестница 3 этаж', '206', 'Проход 3', '205'],
    'Проход 3': ['206', 'Лестница 2 этаж', '213', '205'],
    '213': ['Проход 3'],
    '205': ['Проход 3', '206', 'Лестница 2 этаж', '204'],
    '204': ['205', '203'],
    '203': ['204', '202'],
    '202': ['203', 'Правая лестница 2 этаж'],
    'Правая лестница 2 этаж': ['Правая лестница цоколь', 'Правая лестница 1 этаж', 'Правая лестница 3 этаж', '202',
                               '201', 'Проход 4'],
    '201': ['Правая лестница 2 этаж'],
    'Проход 4': ['Правая лестница 2 этаж', 'Кафедра физики', 'Лаборатория физики'],
    'Кафедра физики': ['Проход 4'],
    'Лаборатория физики': ['Проход 4'],
    'Левая лестница 3 этаж': ['Левая лестница 1 этаж', 'Левая лестница цоколь', 'Левая лестница 2 этаж', '312', '311'],
    '312': ['Дирекция ИГиО', '311', 'Левая лестница 2 этаж'],
    '311': ['312', '310', 'Левая лестница 2 этаж'],
    'Дирекция ИГиО': ['312', '310', '308'],
    '310': ['311', 'Дирекция ИГиО', '308'],
    '308': ['Дирекция ИГиО', '310', '307'],
    '307': ['308', 'Лестница 3 этаж', '305'],
    'Лестница 3 этаж': ['Лестница 1 этаж', 'Лестница 2 этаж', '307', '305'],
    '305': ['Лестница 3 этаж', '307', '304'],
    '304': ['305', '303'],
    '303': ['304', '302а'],
    '302а': ['303', '302', 'Правая лестница 3 этаж'],
    '302': ['302а'],
    'Правая лестница 3 этаж': ['Правая лестница цоколь', 'Правая лестница 1 этаж', 'Правая лестница 2 этаж', '301',
                               '302а', 'Проход 4'],
    '301': ['Правая лестница 3 этаж', 'Проход 5'],
    'Проход 5': ['Правая лестница 3 этаж', '301', '322', 'Лаборатория КУПЗ'],
    'Лаборатория КУПЗ': ['Кафедра КУПЗ', 'Проход 5'],
    '322': ['325', 'Проход 5'],
    '325': ['322'],
    'Кафедра КУПЗ': ['Лаборатория КУПЗ']
}