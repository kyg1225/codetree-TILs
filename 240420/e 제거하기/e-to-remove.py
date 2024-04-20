s = input()
result=list(s)
result.remove(result[s.find('e')])
print(''.join(result))