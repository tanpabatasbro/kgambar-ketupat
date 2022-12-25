print('''PROGRAM KETUPAT BINTANG
      ''')
print(20*"=")

a = int(input("masukkan lebar belah ketupat : "))

for i in range(a):
  print(' ' * (a-i),end='')
  print('* ' * (i+1))
   
for i in range(1,a):
  print(' ' * (i+1),end='')
  print('* ' * (a-i))
