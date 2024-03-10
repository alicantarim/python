x = 5 

result = 5 < x < 10
hak = 5
devam = 'e'

# and 

result = (x > 5) and (x < 10)  
#True, True => True
#True, False => False
result = (x > 5) and (x < 10) 
result = (hak > 0 ) and (devam == 'e')

# or

result = (x > 0) or (x % 2 == 0)
# True, False => True    Eşitliğin bir tarafı True olması yeterli
# False, False => False
# True, True => True  

# not

result = not(x > 0)  #False gelir.

# x, 5-10 arasında olan bir çift sayı mı?

result = ((x>5) and (x<10)) and (x%2==0)

print(result)
