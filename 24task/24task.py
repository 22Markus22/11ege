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

def N17563_reg():
    with open("txts/24_17563.txt") as f:
        s = f.read().strip()

    number = r'[7-9][07-9]*'
    pattern = rf'({number}[*-])+{number}'
    matches = [match.group() for match in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N17563_replace():
    with open("txts/24_17563.txt") as f:
        s = f.read().strip()
    s = s.replace('-', '*')
    s = s.replace('**', '  ')
    for i in '89':
        s = s.replace(i, '7')
    s = s.replace('*0', '  ')
    while ' 0' in s:s = s.replace(' 0', '  ')
    ls = s.split()
    lens = []
    for i in ls:
        lens.append(len(i))
    print(max(lens))

def N16388():
    with open("txts/24_1_1.txt") as f:
        s = f.read().strip()
    pattern = r'(KLMN)+(KLM)?(KL)?(K)?'
    matches = [match.group() for match in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N17685():
    with open("txts/24_2_1.txt") as f:
        s = f.read().strip()
    number = r'(0|[1-9][0-9]*)'
    pattern = rf'{number}([*+]{number})+'
    matches = [m.group() for m in finditer(pattern, s)]
    ln = 0
    for i in matches:
        if eval(i) == 0 and len(i)>ln:
            ln = len(i)
    print(ln)

def N17641():
    with open("txts/24_3_1.txt") as f:
        s = f.read().strip()
    number = r'(0|[1-9][0-9]*)'
    pattern = rf'{number}([*+]{number})+'
    matches = [m.group() for m in finditer(pattern, s)]
    ln = 0
    for i in matches:
        if eval(i) == 0 and len(i)>ln:
            ln = len(i)
    print(ln)

N17641()