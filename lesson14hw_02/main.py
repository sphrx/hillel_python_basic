from student import Student
from group import Group

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
assert gr.find_student('Jobs2') is None

gr.delete_student('Taylor')
print(gr)  # Only one student

# Попытка добавить больше 10 студентов
for i in range(10):
    gr.add_student(Student('Male', 20, f'Student{i}', f'Lastname{i}', f'AN{i}'))

# Это должно вывести сообщение об ошибке
gr.add_student(Student('Female', 22, 'Extra', 'Student', 'AN999'))

print(f"Итоговое количество студентов в группе: {len(gr.group)}")