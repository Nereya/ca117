def cal_average(lst):
   n = len(lst)
   total = (sum(lst))
   average = (total/n)
   new_lst = [num for num in lst if num > average]
   return new_lst

print(cal_average([1,1,1,1,1,2,5]))


