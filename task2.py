# Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат. ¬ - Отрицание ⋁-логическое"Или" ⋀-логическое"И"
x = True
y = True
z = True
left = not (x or y or z)
right = not x and not y and not z
print(left)
print(right)
print(left == right)
