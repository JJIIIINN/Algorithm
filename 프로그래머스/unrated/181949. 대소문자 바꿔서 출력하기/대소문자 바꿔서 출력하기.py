str = input()
a = ''
for i in str:
    if(ord(i) >= 97):
        a = a + chr(ord(i) - 32)
    else:
        a = a + chr(ord(i) + 32)
print(a)
