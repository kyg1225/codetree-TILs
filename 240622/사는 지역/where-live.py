class LivingPlace:
    def __init__(self, name, code, region):
        self.name = name
        self.code = code
        self.region = region

n = int(input())
living_place = []
for _ in range(n):
    u_name, u_code, u_region = tuple(input().split())
    living_place.append(LivingPlace(u_name, u_code, u_region))

maxi_idx = 0
for i in range(n):
    if living_place[maxi_idx].name < living_place[i].name:
        maxi_idx = i

print(f'name {living_place[maxi_idx].name}')
print(f'addr {living_place[maxi_idx].code}')
print(f'city {living_place[maxi_idx].region}')