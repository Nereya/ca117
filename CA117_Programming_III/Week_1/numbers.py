def sum_to_k(lst, k):
   i = 0
   while i < len(lst):
      j = 1
      while j < len(lst):
         if lst[i] + lst[j] == k:
            return(lst[i], lst[j])
         
         j = j + 1
      i += 1

def main():

   lst = [60, 6, 10, 8, 5]
   k = 5
   print(sum_to_k(lst,k))

if __name__ == '__main__':
   main()
