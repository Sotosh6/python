# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

print("Введите через пробел сумму чисел и их произведение: ")
a, b = map(int, input().split())
res = []
for i in range(a + b):
    if i == (a * i - b)**0.5:
        res.append(i)
print("Задуманные числа X и Y: ")        
print(*res if len(res) == 2 else res + res)
