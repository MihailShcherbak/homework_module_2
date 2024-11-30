my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
ind = 0
# print(len(my_list))
while ind <= len(my_list):
     if my_list[ind] > 0:
         print(my_list[ind])
         ind = ind + 1
         continue
     elif my_list[ind] == 0:
         ind = ind + 1
         continue
     else:
         break