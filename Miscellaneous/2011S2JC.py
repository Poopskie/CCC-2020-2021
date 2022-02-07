n = int(input())

student = []
answers = []
end = 0

for i in range(n):
    student.append(i)

for i in range(n):
    answers.append(i)

for i in range(len(answers)):
    if answers[i]==student[i]:
        end += 1

print(end)