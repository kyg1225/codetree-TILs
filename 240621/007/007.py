class Secret:
    def __init__(self, code, place, times):
        self.code = code
        self.place = place
        self.times = times

s1, s2, s3 = map(str, input().split())

secret = Secret(s1, s2, s3)
print('secret code :', secret.code)
print('meeting point :', secret.place)
print('time :', secret.times)