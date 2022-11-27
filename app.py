# name = input('Your name: \n')
# f_name = 'name.txt'
# file = open(f_name,'w')
# file.write(name)
# file.close()

# file = open(f_name,'r')
# res = file.read()
# print("\nRead file file: \n",res)

block = [1,2,3.6,0.3]

print(block)

block.remove(1)
print(block)
block.append(10)
print(block)

block.reverse()
print(block)