import sys

def add(a):
   i = int(a[0])
   j = int(a[1])
   return 'i' + '+' + 'j' + '=' + i+j

def main():
   
   for line in sys.stdin:
      sum = add(line.split())
      print(sum)
      
if __name__ == '__main__':
   main()
