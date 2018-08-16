def rprint(a,b):
   if a != b:
      print a
      a = a + 1
      return rprint(a,b)

print(rprint(4,10))
