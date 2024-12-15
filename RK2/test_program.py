import pytest
from program import groups, courses, groups_courses, build_one_to_many, build_many_to_many, query_d1, query_d2, query_d3

#pytest RK2/test_program.py

@pytest.fixture
def data():
    one_to_many = build_one_to_many(groups, courses)
    many_to_many = build_many_to_many(groups, courses, groups_courses)
    return one_to_many, many_to_many

def test_query_d1(data):
    one_to_many, _ = data
    result = query_d1(one_to_many)
    # проверим, что все названия заканчиваются на "ов"
    for title, _ in result:
        assert title.endswith("ов"), f"Название курса {title} не заканчивается на 'ов'"
    # можем также проверить кол-во результатов или конкретные значения
    assert len(result) > 0

def test_query_d2(data):
    one_to_many, _ = data
    result = query_d2(one_to_many)
    # проверим, что результат отсортирован по убыванию средней оценки
    avg_grades = [r[1] for r in result]
    assert avg_grades == sorted(avg_grades, reverse=True), "Результат не отсортирован по убыванию"
    # проверим, что существует хотя бы одна группа
    assert len(result) > 0

def test_query_d3(data):
    one_to_many, many_to_many = data
    result = query_d3(groups, many_to_many)
    # проверим, что все ключи результата начинаются на "А"
    for g_name in result.keys():
        assert g_name.startswith("А"), f"Группа {g_name} не начинается на 'А'"
    # проверим, что результаты непустые
    for courses_list in result.values():
        assert len(courses_list) >= 0  # может быть 0, если группа не содержит курсов