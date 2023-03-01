from itertools import product
s = "информатика"
sog = 'нфрмтк'
count = 0
for i1 in s:
    for i2 in sog:
        for i3 in s:
            for i4 in sog:
                for i5 in s:
                    for i6 in sog:
                        for i7 in s:
                            for i8 in sog:
                                for i9 in s:
                                    for i10 in sog:
                                        res = i1 + i2 + i3 + i4 + i5 + i6 + i7 + i8 + i9 + i10 
                                        for i in res:
                                            pr = 1
                                            if res.count(i) == 1:
                                                pr = 1
                                            else:
                                                pr = 0
                                            if pr == 1:
                                                count += 1
print(count)