class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        pass

    def __change_name__(self):
        print("My name is " + Bob.change_name)
    def __change_age__(self):
        print("my age is " + Bob.change_age)
    def __add_track__(self):
        print("my tracks are " + Bob.tracks)
    def __get_score__(self):
        print("My scores are " + Bob.score)

Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

