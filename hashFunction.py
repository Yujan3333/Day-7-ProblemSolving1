#Task input='abcdz'
#hash output='bcdefa' using ord()   and change to chr()

st='abcdez'
output=''
print(ord('z'))
for i in range(len(st)):  # we can also use for i in st ,, and i shows abcgefz
    
    if(ord(st[i])==ord('z')):
        output+=chr(ord('a'))
    else:
        output+=chr(ord(st[i])+1)
print(output)
