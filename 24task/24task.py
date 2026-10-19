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
    pattern = r'(LMN|MN|N)?(KLMN)+(KLM|KL|K)?'
    matches = [m.group() for m in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N17685_re():
    with open("txts/24_2_1.txt") as f:
        s = f.read().strip()
    number = r'(0|[1-9][0-9]*)'
    pattern = rf'{number}([*+]{number})*'
    matches = [m.group() for m in finditer(pattern, s)]
    ln = 0
    for i in matches:
        if eval(i) == 0 and len(i)>ln:
            ln = len(i)
    print(ln)


def N17685_correct_re():
    with open("txts/24_2_1.txt") as f:
            s = f.read().strip()
    number = r'(0|[1-9][0-9]*)'
    zero = rf'({number}\*)*0(\*{number})*'
    pattern = rf'{zero}(\+{zero})*'
    matches = [m.group() for m in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N17641_re():
    with open("txts/24_3_1.txt") as f:
        s = f.read().strip()
    number = r'(0|[1-9][0-9]*)'
    pattern = rf'{number}([*+]{number})*'
    matches = [m.group() for m in finditer(pattern, s)]
    ln = 0
    for i in matches:
        if eval(i) == 0 and len(i)>ln:
            ln = len(i)
    print(ln)

def N17641_correct_re():
    with open("txts/24_3_1.txt") as f:
            s = f.read().strip()
    number = r'(0|[1-9][0-9]*)'
    zero = rf'({number}\*)*0(\*{number})*'
    pattern = rf'{zero}(\+{zero})*'
    matches = [m.group() for m in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N17685_brute_force():
    with open("txts/24_17563.txt") as f:
        s = f.read().strip()
    number = r'(0|[1-9][0-9]*)'
    pattern = rf'({number}[+*])+{number}'
    matches = [match.group() for match in finditer(pattern, s)]
    answ = 0
    for match in matches:
        ln_mtch = len(match)
        if eval(match) == 0:
            answ = max(answ, len(match))
        elif len(match) > answ:
            for l in range(0, ln_mtch -1):
                for r in range(ln_mtch - 1, l, -1):
                    if match[r] in '+*' or match[l] == 0:
                        continue
                    new_match = match[l:r + 1]
                    if eval(new_match) == 0:
                        answ = max(answ, len(new_match))

def N7600():
    with open("txts/24_7600.txt") as f:
        s = f.read().strip()
    pattern = r'[^QRS]*([QRS][^QRS]+)*[QRS]?'
    matches = [m.group() for m in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N23381():
    with open("txts/24_23381.txt") as f:
        s = f.read().strip()
    pattern = r'[02468]([A-Z])\1*[02468]'
    matches = [m.group() for m in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N23206():
    #0SA 
    with open("txts/24_23206.txt") as f:
        s = f.read().strip()
    pattern = r'[02468][^02468S]*(S[^02468S]*){35}'
    matches = [m.group() for m in finditer(pattern, s)]
    print(len(max(matches, key=len)))

def N22356():
    with open("txts/24_22356.txt") as f:
        s = f.read().strip()
    pattern = r'[1-9AB][0-9AB]*[13579B]'
    matches = [m.group() for m in finditer(pattern, s)]
    ans = max(matches, key=lambda x: int(x,12))
    print(s.find(ans))

def N31160():
    with open("txts/24_31160.txt") as f:
        s = f.read().strip()
    pattern = r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'
    matches = [m.group() for m in finditer(pattern, s) if m.group()]
    mx = max(map(len, matches))
    longest = [x for x in matches if len(x) == mx]
    rnms = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1,
            'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
    ans = 10**10
    for num in longest:
        summ = 0
        flag = False
        for d1, d2 in zip(num, num[1:]):
            if flag:
                flag = False
                continue
            if d1 + d2 in rnms:
                summ += rnms[d1 + d2]
                flag = True
            else:
                summ += rnms[d1]
        if not flag:
            summ += rnms[num[-1]]
        ans = min(ans, summ)
    print(ans)

def N31160_while():
    with open("txts/24_31160.txt") as f:
        s = f.read().strip()

    numbers = {
        'M': 1000, 'D': 500, 'C': 100,
        'L': 50, 'X': 10, 'V': 5, 'I': 1,
        'CM': 900, 'CD': 400,
        'XC': 90, 'XL': 40,
        'IX': 9, 'IV': 4
    }

    len_data = len(s)

    l = r = 0
    last_number = 1000
    ans = []

    while r < len_data:

        if s[r:r + 2] in numbers and last_number > numbers[s[r:r + 2]]:
            last_number = numbers[s[r:r + 2]]
            r += 2

        elif s[r] in numbers and last_number >= numbers[s[r]]:

            if s[r] in "DLV" and s[l:r + 1].count(s[r]) == 0:
                last_number = numbers[s[r]]
                r += 1

            elif s[r] in "MCXI" and s[l:r + 1].count(s[r]) < 3:
                last_number = numbers[s[r]]
                r += 1

            else:
                ans.append(s[l:r])
                last_number = 1000
                l = r
                r += 1

        else:
            ans.append(s[l:r])
            last_number = 1000
            r += 1
            l = r

    if l < r:
        ans.append(s[l:r])

    max_len = len(max(ans, key=len))
    longest = [x for x in ans if len(x) == max_len]

    def roman_to_int(num):
        res = 0
        i = 0
        while i < len(num):
            if i + 1 < len(num) and num[i:i + 2] in numbers:
                res += numbers[num[i:i + 2]]
                i += 2
            else:
                res += numbers[num[i]]
                i += 1
        return res

    print(min(map(roman_to_int, longest)))

def N8840():
    with open('txts/24_8840.txt') as f:
        s = f.read().strip()
    word = r'[A-Z]+'
    pattern = rf'(?=({word}(\s+{word})*\.))'
    matches = [m.group(1) for m in finditer(pattern, s)]
    answ = 0

    for sentence in matches:
        ls = sentence[:-1].split()
        for l in range(len(ls) - 1, 0, -1):
            if len(ls[l]) > len(ls[l - 1]):
                break
        else:
            answ = max(answ, len(sentence))

    print(answ)

def N8840_t2():
    with open(r'txts\24_8840.txt') as file:
        data = file.readline()
    pattern = r'([A-Z]+ +)+[A-Z]+\.'
    matches = [match.group() for match in finditer(pattern, data)]
    ans = 0
    
    for match in matches:
        line = match[:-1].replace(' ', '*')
        line = sub(r'\*[A-Z]', '* Z', line)
        line = line.split()
        while line != sorted(line, key=lambda x: len(x.strip('*')), reverse=True):
            line = line[1:]
        ans = max(ans, len(''.join(line)) + 1)

    print(ans)

def N8837():
    with open('txts/24-371.txt') as f:
        s = f.read()

    pattern = r'[A-Z]([A-Z ]*[A-Z])?\.'
    matches = [match.group() for match in finditer(pattern, s)]
    ans = 0

    for match in matches:
        if not any(char in match for char in 'XYZ'):
            ans = max(ans, len(match))
        elif len(match) > ans:
            r = len(match) - 1
            while match[r] not in 'XYZ':
                r -= 1
            ans = max(ans, len(match[r+1:].lstrip()))
    print(ans)

def N8835():
    with open('txts/24-371.txt') as f:
        s = f.read()
    pattern = r'[^.]+\.'
    matches = [match.group() for match in finditer(pattern, s)]
    ans = 0

    for match in matches:
        cnt_M = match.count('M')

        if cnt_M == 112:
            ans = max(ans, len(match))

        elif cnt_M > 112 and len(match) > ans:
            r = len(match) - 1
            new_cnt_M = 0

            while new_cnt_M <= 1:
                if match[r] == 'M':
                    new_cnt_M += 1
                r -= 1
            ans = max(ans, len(match[r+2:]))
    print(ans)

def N4627():
    with open(r'C:\Users\Markus\Desktop\11ЕГЭ\11ege\24task\txts\24_4627.txt') as f:
           s = f.read()
    max_count = 0
    count = 0

    for i in range(0, len(s) - 2, 3):
        if s[i:i+3] in ('NPO', 'PNO'):
            count += 1
            max_count = max(max_count, count)
        else:
            count = 0

    print(max_count)

def N4627_rep():
    with open(r'C:\Users\Markus\Desktop\11ЕГЭ\11ege\24task\txts\24_4627.txt') as file:
        data = file.readline()

    for i in 'NPO', 'PNO':
        data = data.replace(i, '*')
    for i in 'NOP':
        data = data.replace(i, ' ')

    data = data.split()
    print(len(max(data, key=len)))

def N4602_rep():
    with open(r'C:\Users\Markus\Desktop\11ЕГЭ\11ege\24task\txts\24_4602.txt') as file:
        data = file.readline()

    for i in 'BA', 'BO', 'CA', 'CO', 'DA', 'DO':
        data = data.replace(i, '*')
    for i in 'ABCDO':
        data = data.replace(i, ' ')


    data = data.split()
    print(len(max(data, key=len)))


N4602_rep()
