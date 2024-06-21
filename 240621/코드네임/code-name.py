class CodeName:
    def __init__(self, code_name, score):
        self.code_name = code_name
        self.score = score

code_names = []
for _ in range(5):
    code, sc = tuple(input().split())
    code_names.append(CodeName(code, int(sc)))

lowest = code_names[0].score
cd = code_names[0].code_name
for i in range(5):
    if lowest > code_names[i].score:
        lowest = code_names[i].score
        cd = code_names[i].code_name

print(cd, lowest)