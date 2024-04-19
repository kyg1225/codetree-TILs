s = ['apple', 'banana', 'grape', 'blueberry', 'orange']

char = input()

result = 0
for i in s:
    if i[2]==char or i[3]==char:
        print(i)
        result += 1

print(result)