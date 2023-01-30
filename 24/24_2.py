# Текстовый файл содержит строки различной длины. Общий объём файла не превышает 1 Мбайт.
#  Строки содержат только заглавные буквы латинского алфавита (ABC…Z).

# В строках, содержащих менее 25 букв A, нужно определить и вывести максимальное
#  расстояние между одинаковыми буквами в одной строке.
s = open('/home/diana/ЕГЭ/24/24(2).txt').readline()
# a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# maxx = 0
# for st in s:
#     for i in a:
#         if st.count('A')<25 and (st.rfind(i) - st.find(i))>maxx:
        
#             maxx = st.rfind(i) - st.find(i)
# print(maxx)

maxx = 0
a = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for j in s:
    for i in a:
        if j.rfind(i) - j.find(i) > maxx and j.count("A") < 25:
            maxx = j.rfind(i) - j.find(i)
print(maxx)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        