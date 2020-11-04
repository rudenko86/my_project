d = '2 + 3 * 3 - 4'
lst = d.split ()
def f(x):
    rez = 0
    sum_ = int(lst[0])
    for i in range(len(lst)):
        if lst[i] == "*":
            rez = int(lst[i-1]) * int(lst[i+1])
            lst[i-1] = rez
            del lst[i]
            del lst[i]
            break
    
    for i in range(len(lst)):
        if lst[i] == '+':
            sum_ =sum_ + int(lst[i+1])
        elif lst[i] == '-':
            sum_ =sum_ - int(lst[i+1])
    print(sum_)
   

f(lst)