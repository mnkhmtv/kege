s = open('/home/diana/ЕГЭ/вариант 25013090/24 (9).txt').readline()

a = s.split('XYZ')

lens = []
for i in a:
    lens.append(len(i))

print(max(lens) + 4)
 # + 4, т.к. включаем подстроки 'YZ' в начале и 'XY' в конце
