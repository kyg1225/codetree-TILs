class Info:
    def __init__ (self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

n = int(input())
infos = []
for i in range(n):
    n, h, w = map(str, input().split())
    infos.append(Info(n, h, w))

infos.sort(key=lambda x: x.height)

for info in infos:
    print(info.name, info.height, info.weight)