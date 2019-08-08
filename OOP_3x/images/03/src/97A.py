def get_lesson(self, student):
  assignment = self.student_graders[student]
  return assignment.lesson()

def check_assignment(self, student, code):
  assignment = self.student_graders[student]
  return assignment.check(code)    
