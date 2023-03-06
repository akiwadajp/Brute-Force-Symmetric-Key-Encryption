alpha =  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

str_in = input("Enter message, like HELLO: ")
shift = int(input("Shift value, like 14: "))

n = len(str_in)
str_out = ""

for i in range(n):
   c = str_in[i]
   loc = alpha.find(c)
   newloc = (loc + shift)%26
   str_out += alpha[newloc]

print("Ciphertext:", str_out)
