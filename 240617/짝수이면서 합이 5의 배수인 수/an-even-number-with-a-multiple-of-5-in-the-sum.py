def is_jjack(n):
    addition = n//10 + n%10
    if n%2 == 0 and addition%5 == 0:
        return 'Yes'
    else:
        return 'No'

n = int(input())
print(is_jjack(n))