class MaxStudentsReachedError(Exception):
    """Exception raised when attempting to add more than 10 students to a group."""
    pass


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
        if len(self.group) >= 10:
            raise MaxStudentsReachedError("It is not possible to add more than 10 students to a group.")
        self.group.add(student)

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

# Добавляем 10 студентов
for i in range(1, 11):
    st = Student(f'Name{i}', f'Lastname{i}', 20 + i, 'Male', f'AN{100 + i}')
    gr.add_student(st)

print(gr)
print(f"Number of students in the group: {len(gr.group)}")

# Пытаемся добавить 11-го студента
st11 = Student('Extra', 'Student', 31, 'Female', 'AN111')

try:
    gr.add_student(st11)
except MaxStudentsReachedError as e:
    print(f"Ошибка: {e}")

print(f"The number of students in the group after the addition attempt: {len(gr.group)}")

# Проверка остальной функциональности
assert str(gr.find_student('Lastname1')) == str(gr.group.pop()), 'Test1'
assert gr.find_student('NonExistent') is None, 'Test2'
assert isinstance(gr.find_student('Lastname2'), Student) is True, 'The search method must return an instance of'

gr.delete_student('Lastname3')
print(gr)
print(f"The number of students in the group after removal: {len(gr.group)}")
