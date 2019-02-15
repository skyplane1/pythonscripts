str1 = (input('enter the terms with a space you want in the list'))

def count(string):

    list1 = string.split()
    even = 0
    odd = 0
    for i in list1:
        num = int(i)
        if num % 2 == 0:
            even += 1
        else:
            odd += 1
    print('the no. of even no is', even ,'the no of odd no is ', odd)



count (str1)

