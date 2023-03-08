import random 
from random import shuffle
test_seed = random.randint(0,100)
random.seed(test_seed)


#FizzBuzz es una pregunta de entrevista, segun la waifu angolchina
'''
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0 :
        print('FizzBuzz')
    elif number % 5 == 0:
        print('Buzz')
    elif number % 3 == 0:
        print('Fizz')
    else: 
        print(number) '''
########################################################################
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]   
abecedario = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 
          'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
          'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 
          'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
simbolos = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
num_num = input("Cuantos numeros debe tener tu contrasena? " )
num_let = input("Cuantas letras debe tener tu contrasena? " )
num_sim = input("Cuantos simbolos debe tener tu contrasena? " )
password = []
password_1 = []
for numeros in range (0, int(num_num)):
    index_1 = random.randint(0,8)
    password.append(numbers[index_1])
    
for letra in range(0, int(num_let)):
    index_2 = random.randint(0,52)
    password.append(abecedario[index_2])
    
for simbolo in range(0,int(num_sim)):
    index_3 = random.randint(0,11)
    password.append(simbolos[index_3])
    
random.shuffle(password)
password_1 = "".join(map(str, password))    

print(f'Sugerimos la contrasena: {password_1}')