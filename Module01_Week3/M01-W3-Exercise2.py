from abc import abstractmethod, ABC

# Initial the abstract People class for later use: Student, Teacher, Doctor


class People:
    def __init__(self, name, yob):
        # Use the protected  type for parent class
        self._name = name
        self._yob = yob

    @abstractmethod
    def describe(self):
        pass

# Child class below - Inherit from People class


class Student(People):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        # Use the private type for the child class
        self.__grade = grade

    def describe(self):
        print(
            f'{Student.__name__}, Name: {self._name}, YOB: {self._yob}, Grade: {self.__grade}')


class Teacher(People):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        # Use the private type for the child class
        self.__subject = subject

    def describe(self):
        print(
            f'{Teacher.__name__}, Name: {self._name}, YOB: {self._yob}, Subject: {self.__subject}')


class Doctor(People):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        # Use the private type for the child class
        self.__specialist = specialist

    def describe(self):
        print(
            f'{Doctor.__name__}, Name: {self._name}, YOB: {self._yob}, Specialist: {self.__specialist}')


class Ward:
    def __init__(self, name):
        self.__name = name
        # List of people in the ward
        self.__people = []

    def add_people(self, person):
        self.__people.append(person)

    def describe(self):
        print(f'Ward, {self.__name}')
        for person in self.__people:
            person.describe()

    def count_doctor(self):
        count = 0
        for person in self.__people:
            if isinstance(person, Doctor) == True:
                count = count + 1
        return count

    def sort_age(self):
        self.__people.sort(key=lambda x: x._yob, reverse=True)
        return self.__people

    def compute_average(self):
        age_teacher = []
        for person in self.__people:
            # Check if person belong to class Teacher?
            if isinstance(person, Teacher) == True:
                # Store into list
                age_teacher.append(person._yob)
        # Round at the 2nd digit
        result = round(sum(age_teacher)/len(age_teacher), 2)
        return result


# MAIN PROGRAM
if __name__ == '__main__':
    # 2a
    student1 = Student(name="studentA", yob=2010, grade="7")
    student1.describe()
    teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
    teacher1.describe()
    doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
    doctor1.describe()
    # 2b
    print()
    teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
    doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
    ward1 = Ward(name='Ward1')
    ward1.add_people(student1)
    ward1.add_people(teacher1)
    ward1.add_people(teacher2)
    ward1.add_people(doctor1)
    ward1.add_people(doctor2)
    ward1.describe()
    # 2c
    print(f"\nNumber of doctors: {ward1.count_doctor()}")
    # 2d
    print("\nAfter sorting Age of Ward1 people")
    ward1.sort_age()
    ward1.describe()
    # 2e
    print(f"\nAverage year of birth (teachers): { ward1.compute_average()}")
