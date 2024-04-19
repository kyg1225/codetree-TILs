s = input()

ee_cnt, eb_cnt = 0, 0
for i in range(len(s)-1):
    if s[i]+s[i+1] == 'ee':
        ee_cnt += 1
    elif s[i]+s[i+1] == 'eb':
        eb_cnt += 1
        
print(ee_cnt, eb_cnt)