class Human:
    def __init__(self, first_name, last_name, age, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Gender: {self.gender}"

class Student(Human):
    def __init__(self, first_name, last_name, age, gender, record_book):
        super().__init__(first_name, last_name, age, gender)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        try:
            if len(self.group) >= 10:
                raise ValueError("Невозможно добавить более 10 студентов в группу.")
            self.group.add(student)
            print(f"Студент {student.last_name} успешно добавлен в группу.")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\n{all_students}'

# Тестирование
gr = Group('PD1')

# Добавляем студентов
st1 = Student('Name1', 'Lastname1', 21, 'Male', 'AN101')
gr.add_student(st1)
for i in range(2, 11):
    st = Student(f'Name{i}', f'Lastname{i}', 20 + i, 'Male', f'AN{100+i}')
    gr.add_student(st)

print(gr)
print(f"Количество студентов в группе: {len(gr.group)}")

# Проверяем, что студент с фамилией 'Lastname1' находится в группе
found_student = gr.find_student('Lastname1')
assert found_student is not None, 'Test1: Student Lastname1 not found'
assert str(found_student) == str(st1), 'Test1: Incorrect student data'

assert gr.find_student('NonExistent') is None, 'Test2'
assert isinstance(gr.find_student('Lastname2'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Lastname3')
print(gr)
print(f"Количество студентов в группе после удаления: {len(gr.group)}")

# Пытаемся добавить 11-го студента
st11 = Student('Extra', 'Student', 31, 'Female', 'AN111')
gr.add_student(st11)

print(f"Итоговое количество студентов в группе: {len(gr.group)}")