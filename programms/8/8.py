answer = 0
not_use = ['16', '61', '36', '63', '56', '65', '76', '67']
 
for i1 in '1234567':
   for i2 in '01234567':
       for i3 in '01234567':
           for i4 in '01234567':
               for i5 in '01234567':

                       numb = i1 + i2 + i3 + i4 + i5 
 
                       if numb.count('6') == 1 and sum([int(x in numb) for x in not_use]) == 0:
                           answer += 1
 
print(answer)