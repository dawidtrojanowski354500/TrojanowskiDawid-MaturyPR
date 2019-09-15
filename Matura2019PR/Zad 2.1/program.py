# (C)Dawid Trojanowski
def pisz(s,n,k):
    if len(s) == n:
        return s
    else:
        i = (k-1)
        return (s+int(i),n,k)