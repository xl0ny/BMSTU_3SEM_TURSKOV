from operator import itemgetter


class StudentGroup:
    """Студенческая группа"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class Course:
    """Учебный курс"""

    def __init__(self, id, title, avg_grade, group_id):
        self.id = id
        self.title = title
        self.avg_grade = avg_grade
        self.group_id = group_id


class GroupCourse:
    """
    'Группы на курсе' для реализации 
    связи многие-ко-многим
    """

    def __init__(self, group_id, course_id):
        self.group_id = group_id
        self.course_id = course_id


# Студенческие группы
groups = [
    StudentGroup(1, 'Группа ИТ-101'),
    StudentGroup(2, 'Группа Матем-201'),
    StudentGroup(3, 'Группа Физ-301'),
    StudentGroup(4, 'Армейская Группа СВО-243'),
]

# Учебные курсы
courses = [
    Course(1, 'Программирование', 85, 1),
    Course(2, 'Математический анализ', 90, 2),
    Course(3, 'Физика', 75, 3),
    Course(4, 'История', 80, 4),
    Course(5, 'Изучение языков', 88, 2),
    Course(6, 'Философия', 93, 3),
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
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(c.title, c.avg_grade, g.name)
                   for g in groups
                   for c in courses
                   if c.group_id == g.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(g.name, gc.group_id, gc.course_id)
                         for g in groups
                         for gc in groups_courses
                         if g.id == gc.group_id]

    many_to_many = [(c.title, c.avg_grade, group_name)
                    for group_name, group_id, course_id in many_to_many_temp
                    for c in courses if c.id == course_id]

    print('Запрос Д1')
    res_d1 = [(title, group_name) for title, avg_grade, group_name in one_to_many if title.endswith("ов")]
    print(res_d1)

    print('\nЗапрос Д2')
    res_d2_unsorted = []
    for g in groups:
        g_courses = list(filter(lambda i: i[2] == g.name, one_to_many))
        if len(g_courses) > 0:
            g_grades = [avg_grade for _, avg_grade, _ in g_courses]
            g_avg_grade = sum(g_grades) / len(g_grades)
            res_d2_unsorted.append((g.name, g_avg_grade))

    res_d2 = sorted(res_d2_unsorted, key=itemgetter(1), reverse=True)
    print(res_d2)

    print('\nЗапрос Д3')
    res_d3 = {}
    for g in groups:
        if g.name.startswith("А"):
            g_courses = list(filter(lambda i: i[2] == g.name, many_to_many))
            g_courses_titles = [x for x, _, _ in g_courses]
            res_d3[g.name] = g_courses_titles

    print(res_d3)


if __name__ == '__main__':
    main()