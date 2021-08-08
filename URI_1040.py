grades = list(map(float, input().split()))
grade_avg = (2.0 * grades[0] + 3.0 * grades[1] + 4.0 * grades[2] + 1.0 * grades[3])/10.0

print("Media: {:.1f}".format(grade_avg))
if grade_avg < 5.0:
    print("Aluno reprovado.")
elif grade_avg >= 7.0:
    print("Aluno aprovado.")
else:
    print("Aluno em exame.")
    grade_extra = float(input())
    print("Nota do exame: {:.1f}".format(grade_extra))
    grade_agv_new = (grade_avg + grade_extra)/2.0
    if grade_agv_new < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno aprovado.")
    print("Media final: {:.1f}".format(grade_agv_new))
