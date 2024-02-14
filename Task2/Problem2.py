scores = set()
student_scores = []
for _ in range(int(input())):
    student_name = input()
    score = float(input())
    scores.add(score)
    student_scores.append([student_name, score])
student_scores.sort(key=lambda student: (student[1], student[0]))
scores = list(scores)
scores.sort()
for student in student_scores:
    if scores[1] == student[1]:
        print(student[0])
