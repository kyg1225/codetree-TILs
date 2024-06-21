class CodeName:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

code_names = []
for _ in range(5):
    code, sc = tuple(input().split())
    code_names.append(CodeName(code, int(sc)))

mini = 0
for i in range(5):
    if code_names[mini].score > code_names[i].score:
        mini = i

print(code_names[mini].code_name, code_names[mini].score)