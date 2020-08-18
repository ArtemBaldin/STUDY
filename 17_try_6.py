 
"""
 Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов
 `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимай набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.
"""

class Subject:
    def __init__(self):
      #  self.name = name
        self.subj_list = set()
    
    def add_subj(self, name):
        self.subj_list.add(name)
        return self.subj_list
        
    def show_subj(self):
        text =""
        sort_list = sorted(list(self.subj_list))
        #почему не получается сделать через 
        # list(self.subj_list).sort()
        for index, subj in enumerate(sort_list):
            text += f"{index+1}) {subj}\n"
        return  text
         
    def index(self, name):
        return list(self.subj_list).index(name)
        
     

class Student:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        self.grades = {}
       # self.st_obj = self.st_object
     
    def _add_grades(self, subj, mark):
        self.grades.setdefault(subj, [mark])
        return self.grades
   
    def add_mark (self, subj, mark):
        try:
            mark = int(mark)
        except:
            print("Wrong value")
            return self.grades
        if self.grades.get(subj) is None:
           # print(f"Added to list:\n{subj}: {mark}")
            return self._add_grades(subj, mark)
        mark_list = self.grades[subj]
        mark_list.append(int(mark))
       # self.grades[subj] = mark_list
        return self.grades
        
    def check_grades(self):
        text = ""
        for string_var in self.grades:
            text += f"{string_var}\t : avr({round(sum(self.grades[string_var])/len(self.grades[string_var]),2)}) \tMarks:{self.grades[string_var]}\n"
        result =f"Student:{self.name}\n{'=' *13}\n{text}" 
        return  result  #self.grades
   
   # def st_object(self):
#        self.st_obj.setdefault(self.name ,self.grades)
#        return self.st_obj
 
       
        
class Group:
    def __init__ (self, name):
        self.name =name
      #  self.obj = obj
        self.st_list = set()
       # self.groups_list
        
    def group_upd(self, obj):
        self.st_list.add(obj)
        return self.st_list
        
    def show_st (self):
        st_list = list(self.st_list)
        print(f"\nGroup name: {self.name}\n{'-'*17}")
        print("List of students:\n")
        for index, st in enumerate(st_list):
            print(f"{index+1}) {st.name}\tage:{st.age}")
       
    def show_grades(self):
        st_list = list(self.st_list)
        print(f"\nGroup name: {self.name}\n{'-'*17}")
        print("List of students:\n")
        for index, st in enumerate(st_list):
            print(f"{st.check_grades()}")
        
       
        
             



# MAIN

subject = Subject()
subject.add_subj("English")
subject.add_subj("Math")
subject.add_subj("Biology")
subject.add_subj("Physics")
subject.add_subj("Math")

#print(subject.show_subj())
#print(subject.index("Math"))



st_1 = Student("Howard", 20)
st_2 = Student("Harry", 19)

#print("--->")
st_1.add_mark("Math", 9)
st_1.add_mark("Math", 11)
st_1.add_mark("Math", 12)
st_1.add_mark("Physics", 9)
st_2.add_mark("Math", 10)

#print("--->")
#print(st_1.check_grades())
#print(st_2.check_grades())
#print(st_2.check_grades()["Math"])

#Main
print("Class = Group\n")
group = Group("INTRO")
group.group_upd(st_1)
group.group_upd(st_2)
#print(group.st_list)
#group.show_st()

####

print("Menu:")
print("Select group:")
print(f"1) {group.name}")
selected_group = int(input("Input: "))
selected_group = group
print("Select variant:")
print("1) Show list of students")
print("2) Check grades")
select_var = int(input("Input: "))
if select_var == 1:
    selected_group.show_st()
if select_var == 2:
    selected_group.show_grades()

    