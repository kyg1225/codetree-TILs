class BombUnlock:
    def __init__(self, unlock_code, line_color, specific_second):
        self.unlock_code = unlock_code
        self.line_color = line_color
        self.specific_second = specific_second

code, color, second = tuple(input().split())
bomb_unlock = BombUnlock(code, color, second)

print(f'code : {bomb_unlock.unlock_code}')
print(f'color : {bomb_unlock.line_color}')
print(f'second : {bomb_unlock.specific_second}')