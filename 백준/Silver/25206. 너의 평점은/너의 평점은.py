grades = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
    }
total_score = 0
total_under = 0
for _ in range(20):
    data = input().split()
    credit = float(data[1])
    grade_str = data[2]

    if data[2] == 'P':
        continue

    else:
        grade = grades.get(grade_str)
        total_score += credit * grade
        total_under += credit

if total_score == 0:
    answer = 0
    print(f'{answer:.6f}')
else:
    answer = "{:.6f}".format(total_score / total_under)
    print(answer)
        