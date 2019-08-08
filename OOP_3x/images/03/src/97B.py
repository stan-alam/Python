def assignment_summary(self, student):
  grader = self.student_graders[student]
  return f"""
  {student}'s attempts at {grader.assignment.__class__.__name__}:

  attempts: {grader.attempts}
  correct: {grader.correct_attempts}
  passed: {grader.correct_attempts > 0}
  """
