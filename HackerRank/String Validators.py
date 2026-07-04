if __name__ == '__main__':
    s = input()
    a=b=c=d=e=False
    for ch in s:
        for ch in s:
            if ch.isalnum():
                a = True
            if ch.isalpha():
                b = True
            if ch.isdigit():
                c = True
            if ch.islower():
                d = True
            if ch.isupper():
                e = True

print(a)
print(b)
print(c)
print(d)
print(e)
