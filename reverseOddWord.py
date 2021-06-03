def f(s):
    w=s.split()
    
    for i in w:
        if(w.index(i)%2 != 0):
            w[w.index(i)]= i[::-1]
    return ' '.join(w)

str=input("Enter your String")
print(f(str))