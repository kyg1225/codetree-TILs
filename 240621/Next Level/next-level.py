class NextLevel:
    def __init__(self, user_id='codetree', user_level='10'):
        self.user_id = user_id
        self.user_level = user_level

next_lv1 = NextLevel()
print(f'user {next_lv1.user_id} lv {next_lv1.user_level}')

u_id, u_lv = tuple(input().split())
next_lv2 = NextLevel(u_id, u_lv)
print(f'user {next_lv2.user_id} lv {next_lv2.user_level}')