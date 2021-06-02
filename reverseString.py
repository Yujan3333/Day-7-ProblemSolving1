string="My name is Abcd"
output="dcbA si eman yM"

naya_output="yM eman si dcbA"

def reverStringOneLiner(string):
    return string[::-1]

def whileloopReverseListConversion(string):
    m=len(string)-1
    newstringLists=[]
    while m>-1:
        newstringLists.append(string[m])
        m=m-1
    
    return ''.join([str(c) for c in newstringLists])

def whileLoopStringReverses(string):
    m=len(string)-1
    reversedString=""
    while m>-1:
        reversedString=reversedString+string[m]
        m=m-1
    return reversedString

print(reverStringOneLiner(string))
print(whileloopReverseListConversion(string))
print(whileLoopStringReverses(string))


