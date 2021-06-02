def reverse(s):
    w=s.split()
    w.reverse()
    return "".join(str(w))

st="My name is Yujan"
print(reverse(st))
