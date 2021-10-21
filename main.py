# используется для сортировки
from operator import itemgetter


class Student:
    """Школьник"""

    def __init__(self, id, fio, bal, st_id):
        self.id = id
        self.fio = fio
        self.bal = bal      #Оценка по информатике
        self.st_id = st_id


class Class:
    """Класс"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class StCl:
    """
    'Учащиеся класса' для реализации
    связи многие-ко-многим
    """

    def __init__(self, st_id, class_id):
        self.class_id = class_id
        self.st_id = st_id


# Классы
clas = [
    Class(1, 'физико-математичский'),
    Class(2, 'химико-биологический'),
    Class(3, 'социально-экономический'),
    Class(4, 'информационно-технологический'),

]

# Школьники
students = [
    Student(1, 'Артамонов', 2, 1),
    Student(2, 'Петров', 3, 2),
    Student(3, 'Иваненко', 4, 3),
    Student(4, 'Иванов', 3, 3),
    Student(5, 'Иванин', 2, 3),
    Student(6, 'Балабанов', 5, 4),
]

st_cl = [
    StCl(1, 1),
    StCl(2, 2),
    StCl(3, 3),
    StCl(4, 3),
    StCl(5, 3),
    StCl(6, 4),

    StCl(3, 2),
    StCl(4, 1),
    StCl(5, 4),
    StCl(6, 3),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(s.fio, s.bal, c.name)
                   for c in clas
                   for s in students
                   if s.st_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.name, cs.class_id, cs.st_id)
                         for c in clas
                         for cs in st_cl
                         if c.id == cs.class_id]

    many_to_many = [(s.fio, s.bal, class_name)
                    for class_name, class_id, st_id in many_to_many_temp
                    for s in students if s.id == st_id]

    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(0))
    print(res_11)

    print('\nЗадание Б2')
    res_12_unsorted = []
    # Перебираем все классы
    for c in clas:
        # Список учеников класса
        c_student = list(filter(lambda i: i[2] == c.name, one_to_many))
        # Если класс не пустой
        if len(c_student) > 0:
            res_12_unsorted.append((c.name, len(c_student)))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\nЗадание Б3')
    res_13 = {}
    # Перебираем все отделы
    for s in students:
        if s.fio.endswith("ов"):
            c_students = list(filter(lambda i: i[0] == s.fio, many_to_many))
            c_students_names = [x[2] for x in c_students]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[s.fio] = c_students_names

    print(res_13)


if __name__ == '__main__':
    main()

