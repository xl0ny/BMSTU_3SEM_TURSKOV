from operator import itemgetter

class StudentGroup:
    # Студенческая группа
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Course:
    # Учебный курс
    def __init__(self, id, title, avg_grade, group_id):
        self.id = id
        self.title = title
        self.avg_grade = avg_grade
        self.group_id = group_id

class GroupCourse:
    # 'Группы на курсе' для реализации
    # связи многие-ко-многим
    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id

# Студенческие группы
groups = [
    StudentGroup(1, 'Группа ИТ-101'),
    StudentGroup(2, 'Армейская Группа СВО-243'),
    StudentGroup(3, 'Группа Физ-301'),
    StudentGroup(4, 'Группа Матем-201'),
    StudentGroup(5, 'Астрономическая Группа 504'),
    StudentGroup(6, 'Археологическая Группа А-102'),
]

# Учебные курсы
courses = [
    Course(1, 'Программирование', 85, 1),
    Course(2, 'Математический анализ', 90, 2),
    Course(3, 'Физика', 75, 3),
    Course(4, 'История', 80, 4),
    Course(5, 'Изучение языков', 88, 2),
    Course(6, 'Философия', 93, 3),
    Course(7, 'Экономический анализ', 87, 5),
    Course(8, 'Введение в биологию', 76, 6),
    Course(9, 'Эволюция', 84, 1),
    Course(10, 'Инвестирование', 92, 2),
    Course(11, 'Теория алгоритмов', 89, 3),
    Course(12, 'Статистика данных', 78, 4),
]

# Связи многие-ко-многим
groups_courses = [
    GroupCourse(1, 1),
    GroupCourse(2, 2),
    GroupCourse(3, 3),
    GroupCourse(4, 4),
    GroupCourse(2, 5),
    GroupCourse(3, 6),
    GroupCourse(4, 6),
    GroupCourse(3, 1),
    GroupCourse(5, 7),
    GroupCourse(6, 8),
    GroupCourse(1, 9),
    GroupCourse(2, 10),
    GroupCourse(3, 11),
    GroupCourse(4, 12),
    GroupCourse(5, 6),
    GroupCourse(6, 11),
]

def build_one_to_many(groups, courses):
    return [(c.title, c.avg_grade, g.name)
            for g in groups
            for c in courses
            if c.group_id == g.id]

def build_many_to_many(groups, courses, groups_courses):
    many_to_many_temp = [(g.name, gc.group_id, gc.course_id)
                         for g in groups
                         for gc in groups_courses
                         if g.id == gc.group_id]

    many_to_many = [(c.title, c.avg_grade, group_name)
                    for group_name, group_id, course_id in many_to_many_temp
                    for c in courses if c.id == course_id]
    return many_to_many

def query_d1(one_to_many):
    """Запрос Д1: все курсы, оканчивающиеся на 'ов'."""
    return [(title, group_name)
            for title, avg_grade, group_name in one_to_many
            if title.endswith("ов")]

def query_d2(one_to_many):
    """Запрос Д2: Средняя оценка курсов по каждой группе, отсортированные по убыванию."""
    res_d2_unsorted = []
    # Группы
    groups_names = set([g for _, _, g in one_to_many])
    for g in groups_names:
        g_courses = list(filter(lambda i: i[2] == g, one_to_many))
        if len(g_courses) > 0:
            g_grades = [avg_grade for _, avg_grade, _ in g_courses]
            g_avg_grade = sum(g_grades) / len(g_grades)
            res_d2_unsorted.append((g, g_avg_grade))
    res_d2 = sorted(res_d2_unsorted, key=itemgetter(1), reverse=True)
    return res_d2

def query_d3(groups, many_to_many):
    """Запрос Д3: Для всех групп, начинающихся с 'А', выдать список курсов."""
    res_d3 = {}
    for g in groups:
        if g.name.startswith("А"):
            g_courses = list(filter(lambda i: i[2] == g.name, many_to_many))
            g_courses_titles = [x for x, _, _ in g_courses]
            res_d3[g.name] = g_courses_titles
    return res_d3

def main():
    one_to_many = build_one_to_many(groups, courses)
    many_to_many = build_many_to_many(groups, courses, groups_courses)

    print('Запрос Д1')
    d1 = query_d1(one_to_many)
    for item in d1:
        print(f"{item[0]} - {item[1]}")

    print('\nЗапрос Д2')
    d2 = query_d2(one_to_many)
    for item in d2:
        print(f"{item[0]} - {item[1]}")

    print('\nЗапрос Д3')
    d3 = query_d3(groups, many_to_many)
    for g in d3:
        print(f"{g}: {', '.join(d3[g])}")

if __name__ == '__main__':
    main()