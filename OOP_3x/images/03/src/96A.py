import uuid
# needs refactoring
class Grader:
    def __init__(self):
        self.student_graders = {}
        self.assignments_classes = {}

    def register(self, assignment_classes):
        if not issubclass(assignment_class, Assignment):
            raise RuntimeError(
                "Your class does not have the appropriate method(s)"
            )

        id = uuid.uuid4()
        self.assignment_classes[id] = assignment_class
        return id
