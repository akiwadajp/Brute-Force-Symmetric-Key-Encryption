#this model won't load if typed in lower case or letters that cannot shift 14 letters within the 'alpha' range
alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

str_in = input("Enter message, like HELLO: ")

n = len(str_in)
str_out = ""

for i in range(n):
   c = str_in[i]
   loc = alpha.find(c)
   print(i, c, loc) 
   newloc = loc + 14
   str_out += alpha[newloc]
   print(newloc, str_out)

print("Ciphertext:", str_out)
