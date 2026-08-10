from re import finditer

def N2942():
    with open("txts/24_2942.txt") as f:
        s = f.read().strip()

    mx = 0
    current = 0
    i = 0

    while i < len(s) - 1:
        if s[i] == "A" and s[i + 1] in "BC":
            current += 1
            i += 2
        else:
            mx = max(mx, current)
            current = 0
            i += 1

    mx = max(mx, current)
    print(mx)

def N2942_2():
    with open("txts/24_2942.txt") as f:
        s = f.read().strip()
    pattern = r'(A[BC])+'
    matches = [match.group() for match in finditer(pattern, s)]
    print(len(max(matches, key=len))/2)

def N4602():
    with open("txts/24_4602.txt") as f:
        s = f.read().strip()

    mx = 0
    current = 0
    i = 0

    while i < len(s) - 1:
        if s[i] in "BCD" and s[i + 1] in "AO":
            current += 1
            i += 2
        else:
            mx = max(mx, current)
            current = 0
            i += 1

    mx = max(mx, current)
    print(mx)

def N4602_2():
    with open("txts/24_4602.txt") as f:
        s = f.read().strip()
    pattern = r'([BCD][AO])+'
    matches = [match.group() for match in finditer(pattern, s)]
    print(len(max(matches, key=len))/2)

def N17563():
    with open("txts/24_17563.txt") as f:
        s = f.read().strip()

    number = r'[7-9][07-9]*'
    pattern = rf'({number}[*-])+{number}'
    matches = [match.group() for match in finditer(pattern, s)]
    print(len(max(matches, key=len)))

N17563()
