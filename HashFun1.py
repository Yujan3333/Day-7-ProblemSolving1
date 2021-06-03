def fun1(s):
    w=''
    for i in range(len(s)):
        if(ord(s[i])==ord('z')):
            w+=chr(ord('a'))
        else:
            w+=chr(ord(s[i])+1)
    return w

i=input("Enter a Word")
print(fun1(i))