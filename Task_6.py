#6
A = [6,1,9,2,3,4,8]
i = 0
me = 0 #предыдущий максимум
j = 0
ma = max(A)+1 #это просто максимум,мы его берём таким большим,чтобы  me был больши при первом сравнении с предыдущим максимум
while j <= (len(A)//2):#ищем "средний" по счёту максимум,тоесть как раз медиану
    me = ma
    ma = -1
    #print('-----')
    for i in range(len(A)):#максмум ищем по обычному алгоритму,а не ленивой функцией питона)

        if (A[i] > ma) and (me > A[i]):#нахожу максимум но не больший предыдущего максимума
            ma = A[i]
            #print(max)
    j += 1
print(me)
#ой в этой задаче я заыла ,что длина массива вводится,но без разницы же?