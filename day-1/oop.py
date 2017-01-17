# An OOP model that grades exam results

class ExamResults():

    def __init__(self, name, marks_scored):
        self.name = name
        self.marks_scored = marks_scored


    def grade_awarded(self):

        if self.marks_scored >= 70:
            return self.name + " | Grade : A"
        elif self.marks_scored < 40:
            return self.name + " | Grade : E"
        elif self.marks_scored < 50:
            return self.name + " | Grade : D"
        elif self.marks_scored < 60:
            return self.name + " | Grade : C"
        elif self.marks_scored < 70:
            return self.name + " | Grade : B"


    def proceed_status(self):

        if self.marks_scored >= 40:
            return "Pass. Proceed to next class"
        elif self.marks_scored < 40:
            return "Fail. Repeat."


bob = ExamResults("Bob", 60)

print(bob.grade_awarded())
print(bob.proceed_status())

