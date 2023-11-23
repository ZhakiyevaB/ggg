import json
# СОздала класс с студентами
class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    def display(self):
        print("Name : ", self.name)
        print("RollNo : ", self.rollno)
        print("Marks1 : ", self.m1)
        print("Marks2 : ", self.m2)
# создала класс чтобы управлять данными и студентах
class StudentsManager:
    def __init__(self, file_path='students_data.json'):
        self.file_path = file_path
        self.students_list = []

    def accept_student(self, name, rollno, marks1, marks2):
        student = Student(name, rollno, marks1, marks2)
        self.students_list.append(student)

    def display_students(self):
        print("\nList of Students\n")
        for student in self.students_list:
            student.display()

    def search_student(self, rollno):
        for i, student in enumerate(self.students_list):
            if student.rollno == rollno:
                return i
        return -1

    def delete_student(self, rollno):
        index = self.search_student(rollno)
        if index != -1:
            del self.students_list[index]

    def update_student(self, rollno, new_rollno):
        index = self.search_student(rollno)
        if index != -1:
            self.students_list[index].rollno = new_rollno
# данные о студентах находились в json 
    def save_to_json_file(self):
        students_data = []
        for student in self.students_list:
            students_data.append({
                'name': student.name,
                'rollno': student.rollno,
                'm1': student.m1,
                'm2': student.m2
            })

        with open(self.file_path, 'w') as file:
            json.dump(students_data, file, indent=2)

    def load_from_json_file(self):
        try:
            with open(self.file_path, 'r') as file:
                students_data = json.load(file)

            self.students_list = []
            for data in students_data:
                student = Student(data['name'], data['rollno'], data['m1'], data['m2'])
                self.students_list.append(student)

        except FileNotFoundError:
            print(f"File {self.file_path} not found.")
        except json.JSONDecodeError:
            print(f"Error JSON{self.file_path}.")

students_manager = StudentsManager()
# тут мой код уже выводит меню каие операции он должен сделать
print("\nOperations used, ")
print("\n1. Accept Student details\n2. Display Student Details\n3. Search Details of a Student\n4. Delete Details of Student\n5. Update Student Details\n6. Save to JSON File\n7. Load from JSON File\n8. Exit")
#  имена студентов и их иоценки
students_manager.accept_student("K", 3, 80, 80)
students_manager.accept_student("D", 2, 90, 90)
students_manager.accept_student("S", 1, 100, 100)
# тут показывается сам список со студентами 
print("\nList of Students\n")
students_manager.display_students()
# тут мы находим студентов, данные о которых мы ввели и вывели в список
print("\nStudent Found, ")
# тут обновленный список с данными о новых студентах
students_manager.update_student(3, 2)
print(len(students_manager.students_list))
print("List after updation")
# отоброжение в в виде списка обновленный вариант студентов 
students_manager.display_students()
# для того чтобы выше указанные данные сохранялись вводим сохранить в json
students_manager.save_to_json_file()
# тут заружается данные о студентах в файле json который у меня выходит в другом окне
students_manager.load_from_json_file()

# вроде как все