import pytest
from dict_curs import dict_curs
from teacher_names import teacher_names
from unique_names import unique_names

def test_unique_names():
    result = unique_names()
    expected = 'Уникальные имена преподавателей: Адилет, Азамат, Александр, Алексей, Алена, Анатолий, Анна, Антон, Вадим, Валерий, Владимир, Денис, Дмитрий, Евгений, Елена, Иван, Илья, Кирилл, Константин, Максим, Михаил, Никита, Николай, Олег, Павел, Ринат, Роман, Сергей, Татьяна, Тимур, Филипп, Эдгар, Юрий'
    assert result == expected
def test_dict_curs():
    result = dict_curs()
    expected = ('Самый короткий курс(ы): Python-разработчик с нуля - 12 месяца(ев)\n'
    'Самый длинный курс(ы): Fullstack-разработчик на Python, Frontend-разработчик с нуля - 20 месяца(ев)')
    assert result == expected
def test_teacher_names():
    result = teacher_names()
    expected = ' Александр: 10 раз(а), Евгений: 5 раз(а), Максим: 4 раз(а)'
    assert result == expected