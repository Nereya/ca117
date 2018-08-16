'''
def sum_num(n):
   if n == 0:
      return 0
   else:
      return n + sum_num(n - 1) 

print(sum_num(0))



def factorial(n):
   if n == 0 or n == 1: 
      return 1
   else:
      return n * factorial(n - 1)

print(factorial(0)) 


def r_print(a,b):
   if a != b: 
      print(a)       
      return r_print(a + 1,b)

print(r_print(4,10))


def sum_to(a,b):
   if a == b:
      return 0
   else:
      return a + sum_to(a + 1,b)

print(sum_to(4,7))


def is_palindrome(s):
   if len(s) < 2:
      return True
   if s[0] != s[-1]:
      return False
   return is_palindrome(s[1:-1])
      
print(is_palindrome('abba'))   


def maximum(lst):
   if len(lst) == 1:
      return lst[0]
   else:
      m = maximum(lst[1:])
      if m > lst[0]:
         return m
      else:
         return lst[0]


def main():
   lst = [1,2,6,4,1,10,30]
   print(maximum(lst))
if __name__ =='__main__':
   main()


def is_palindrome(word):
   if len(word) < 2: 
      return True
   if word[0] != word[-1]:
      return False
   return is_palindrome(word[1:-1])

print(is_palindrome('ab'))


def sum_to(lst,k):
   i = 0
   while i < len(lst):
      j = i + 1
      while j < len(lst):
         if lst[i] + lst[j] == k:
            print(lst[i],lst[j])
         j = j + 1
      i = i + 1


print(sum_to([60,6,10,8,5],15))


def sum_to(lst,k):
   
   new_lst = [n for n in lst if n < k]
   return new_lst

'''

def sum_to(a,n):
   i = 0
   j = n-1
   while(i < j):
      if (a[i] + a[j] == target) return (i, j)
      else if (a[i] + a[j] <  target) i += 1
      else if (a[i] + a[j] >  target) j -= 1
  


print(sum_to([60,6,10,8,5],15))
