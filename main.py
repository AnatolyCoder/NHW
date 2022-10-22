class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
               f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {",".join(self.finished_courses)}'

    def average_grades(self):
        sum_grades = 0
        number_grades = 0
        for grade in self.grades.values():
            number_grades += len(grade)
            sum_grades += sum(grade)
        return round(sum_grades / number_grades, 1)

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lect(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def compare_students(self, student):
        if student.average_grades() > self.average_grades():
            return 1
        elif student.average_grades() < self.average_grades():
            return -1
        else:
            return 0

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.average_grades()}'

    def average_grades(self):
        sum_grades = 0
        number_grades = 0
        for grade in self.grades.values():
            number_grades += len(grade)
            sum_grades += sum(grade)
        return round(sum_grades / number_grades,1)

    def compare_lecturers(self, lecturer):
        if lecturer.average_grades() > self.average_grades():
            return 1
        elif lecturer.average_grades() < self.average_grades():
            return -1
        else:
            return 0

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
#объявлем стдента №1
best_student = Student('Best', 'Student', 'best_student_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['C++']
best_student.grades['Git'] = [10, 10, 10, 10, 10]
best_student.grades['Python'] = [10, 10]

#объявлем стдента №2
bad_student = Student('Bad', 'Student', 'bad_student_gender')
bad_student.courses_in_progress += ['Python']
bad_student.grades['Git'] = [5, 4, 3, 2, 1]
bad_student.grades['Python'] = [5, 4]

#объявлем ревьювера
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

#объявлем лектора №1
bad_lecturer = Lecturer('Bad', 'Lecturer')
bad_lecturer.grades['Git'] = [5, 4, 3]
bad_lecturer.grades['Python'] = [5, 4]

#объявлем лектора №2
cool_lecturer = Lecturer('Cool', 'Lecturer')
cool_lecturer.grades['Git'] = [10, 10, 10]
cool_lecturer.grades['Python'] = [10, 10]
cool_lecturer.courses_attached += ['Python']

#выставляем оценки студентам за домашнее задлание
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(bad_student, 'Python', 5)
cool_reviewer.rate_hw(bad_student, 'Python', 5)

#выставляем оценки лекторам за лекции
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 10)
best_student.rate_lect(cool_lecturer, 'Python', 10)

#выводим информацию
print(best_student)
print()
print(bad_student)
print()
print(cool_reviewer)
print()
print(cool_lecturer)
print()
print(bad_lecturer)
print()

#сравниваем между собой лекторов
if cool_lecturer.compare_lecturers(bad_lecturer) == 1:
    print(f'{cool_lecturer.name} {cool_lecturer.surname} < {bad_lecturer.name} {bad_lecturer.surname}')
elif cool_lecturer.compare_lecturers(bad_lecturer) == 0:
    print(f'{cool_lecturer.name} {cool_lecturer.surname} = {bad_lecturer.name} {bad_lecturer.surname}')
elif cool_lecturer.compare_lecturers(bad_lecturer) == -1:
    print(f'{cool_lecturer.name} {cool_lecturer.surname} > {bad_lecturer.name} {bad_lecturer.surname}')

#сравниваем между собой студентов
if best_student.compare_students(bad_student) == 1:
    print(f'{best_student.name} {best_student.surname} < {bad_student.name} {bad_student.surname}')
elif best_student.compare_students(bad_student) == 0:
    print(f'{best_student.name} {best_student.surname} = {bad_student.name} {bad_student.surname}')
elif best_student.compare_students(bad_student) == -1:
    print(f'{best_student.name} {best_student.surname} > {bad_student.name} {bad_student.surname}')

all_students = [best_student, bad_student]
all_lecturers = [cool_lecturer, bad_lecturer]

def average_grades_all_students(list_all_students, course):
    list_all_grades = []
    for student in list_all_students:
        for key, value in student.grades.items():
            if key == course:
                list_all_grades += value
    return f'Средняя оценка за домашние задания всех студентов в рамках курса {course}: {round(sum(list_all_grades)/len(list_all_grades),1)}'

def average_grades_all_lecturers(list_all_lecturers, course):
    list_all_grades = []
    for lecturer in list_all_lecturers:
        for key, value in lecturer.grades.items():
            if key == course:
                list_all_grades += value
    return f'Средняя оценка за лекции всех лекторов в рамках курса {course}: {round(sum(list_all_grades)/len(list_all_grades),1)}'

print(average_grades_all_students(all_students,'Python'))
print(average_grades_all_lecturers(all_lecturers, 'Python'))