for i in range(0,10000):
    s = i*'2' + i*'1' + i*'3'
    while '21' in s or '31' in s or '32' in s:
        if '21' in s:
            s = s.replace('21','12',1)
        if '31' in s:
            s = s.replace('31','13',1)
        if '32' in s:
            s = s.replace('32','23',1)
            
    if len(s)>=50:
        if s[49] == '2':
            print(i*3)
            input()
