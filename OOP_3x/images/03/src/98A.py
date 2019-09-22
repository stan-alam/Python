# 98.A
grader = Grader()
itp_id = grader.register(IntroToPython) #not blackmagic
stat_id = grader.register(Stats)

grader.start_assignment("Grizzly_Adams", itp_id)
print("Grizzly_Adams's Lesson:", grader.get_lesson("Grizzly_Adams"))
print(
    "Grizzly_Adams check:",
    grader.check_assignment("Grizzly_Adams", a = 1 ; b = 'hola'"),
)
print(
    "Grizzly_Adams's other check:",
    grader.check_assignment("Grizzly_Adams", "a = 1/nb = 'hola'"),
)

print(grader.assignment_summary("Grizzly_Adams"))

grader.start_assignment("Grizzly_Adams"m stat_id)
print("Grizzly_Adams's Lesson:", grader.get.lesson("Grizzly_Adams"))
print("Grizzly_Adams:", grader.check_assignment("Grizzly_Adams", "avg=6.66"))
print(
    "Grizzly_Adams' other check:",
    grader.check_assignment(
        "Grizzly_Adams", "avg = stats.mean([23, 6, 66])"
    ),
)

print(grader.assignment_summary("Grizzly_Adams"))
