# def main(**kwargs):
#     print(kwargs)
#     for k, v in kwargs.items():
#         print(k, v)

# print(main(name='Olzhas', age='20', i=123, a=123.312, b={'name': 'marselle'}))


# def rec():
#     return rec()
# rec()

# def rec_num(number:int):
#     if number == 0:
#         return 1
#     return number * rec_num(number - 1)
# # print(rec_num(5))

# num = int(input("введите число:  "))
# factorial = rec_num(num)
# print("факториал числа", num, "равен", factorial)


def max_find_num(lists:list, n):
    if n == 0:
        return "куасынба"

    if n == 1:
        return lists[0]
    
    return max(lists[n - 1], max_find_num(lists,n - 1))

arr = [1,2,3,4,5,6]
n = len(arr)
print(max_find_num(arr, n))