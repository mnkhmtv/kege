s = '>' + 25*'1' + 17*'2' + 10*'3'
while '>1' in s or '>2' in s or '>3' in s:
    if '>1' in s:
        s = s.replace('>1', '22>3',1)
    if '>2' in s:
        s = s.replace('>2','2>',1)
    if '>3' in s:
        s = s.replace('>3', '11>2',1)

print(s.count('3')*3 + s.count('2')*2 + s.count('1')*1)