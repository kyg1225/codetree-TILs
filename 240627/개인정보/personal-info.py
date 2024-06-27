personal=[] 
for i in range(5):
    name, height, kg = tuple(input().split())
    personal.append((name, int(height), int(kg)))

personal.sort(key=lambda x:x[0])
print('name')
for p in personal:
    print(p[0], p[1], p[2])

personal.sort(key=lambda x:x[1])
print('height')
for p in personal:
    print(p[0], p[1], p[2])