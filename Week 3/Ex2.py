def my_reverse(ls):
    reverse = []
    for num in range(len(ls)):
        reverse.insert(num, ls[len(ls)-1-num])
    return reverse
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_reverse(a_list))

#ls.reverse()
#reverse=ls[::-1]
#list(reversed(ls))
       
