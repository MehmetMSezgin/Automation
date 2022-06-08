class student_class:

    def __init__(self, name, major, grade, is_on_programme):
        self.name = name
        self.major = major
        self.grade = grade
        self.is_on_programme = is_on_programme

    def yellow_card_KHO(self):
        if self.grade >= 3.5:
            print("Yellow card owner")
            return True
        else:
            print("No")
            return False