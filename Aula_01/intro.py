# print("Bom dia Picas")
# print("Digite um numero: ")
# input()


print('''
    \033[32m

                                                    
.------..------..------..------..------..------.
|P.--. ||Y.--. ||T.--. ||H.--. ||O.--. ||N.--. |
| :/\: || (\/) || :/\: || :/\: || :/\: || :(): |
| (__) || :\/: || (__) || (__) || :\/: || ()() |
| '--'P|| '--'Y|| '--'T|| '--'H|| '--'O|| '--'N|
`------'`------'`------'`------'`------'`------' 
      
                         $$$$$$                         
               $$$  $$ $$$                        
               $    ##   $$§§                     
               ####        $§§§                   
                $$$$$$   $  $§§§                  
                  §§§$$   $ $§§§§                 
                 §§§§§$   $ $§§§§§                
                 §§§§§$   $$$§§§§§                
                 §§§§$$ $   $§§§§§                
                §§§§§§$  $ $$§§§§§                
                §§§§§$$   $$§§§§§§                
               §§§§§§$  $ $$§§§§§                 
               §§§§$$   $ $§§§§§                  
               §§§$$   $ $$§§§§                   
                §$$    $ $§§§§                    
                 $    $ $$§§                      
                $$   $  $$                        
               $$      $$                         
               $      $$ $                        
              $$     $$ $$$      $$$$$$$$$$$      
              $      $   $$$$$$$$           $     
       $$$$$ $$   $ $$    $$$$$$    $$$      $    
   $$$$    $$$$ $ $ $$$$$$$$    $$$$$$$$$$$  $    
  $$    $    $$   $ $$      $$$$          $$$$$   
 $     $      $ $   $$ $$$$$            $     $$$ 
$      $$$$$$$$    $ $$$                 $$     $$
$      $$     $ $    $$          $$$$$$$$$$      $
$$       $$$$ $$ $$ $ $$     $$$$$$       $      $
 $$            $$    $ $$$$$$$          $$       $
   $$           $     $  $$$       $$$$$$       $$
    $$$$$     $$$        $$$$$$$$$           $$   
       $$$$$$$$$$ $$$                        $$$  
                    $$$$                  $$$$    
                        $$$$$$$$$$$$$$$$$$$       

    \033[0;0m
\n''')

print("Bem vindo ao sitema piranha \n")

# valor = input("Digite um numero: ")

nome = 'Tijolison Argamassa NasCimento'
idade = 18
endereco = 'Rua dos Cria'
numero = '1'
telefone = '4002-8922'

# print('\nCaro Sr. ' + nome + ' de idade ' + idade + ' residente de ' + endereco + ', ' + numero + ' e telefone ' + telefone)
print('\nCaro Sr. \033[32m{}\033[0;0m de idade \033[32m{}\033[0;0m residente da \033[32m{}\033[0;0m, nº \033[32m{}\033[0;0m e telefone \033[32m{}\033[0;0m\n'
      .format(nome, idade, endereco, numero, telefone))

if idade > 17:
    print('Você é maior de \033[32m18\033[0;0m')
elif idade < 10:
    print('Você é menor de \033[32m10\033[0;0m')
else:
    print('Você NÃO é MAIOR de \033[32m18\033[0;0m e nem MENOR de \033[32m10\033[0;0m')

vogal = ['a', 'e', 'i', 'o', 'u']

if 'i' in vogal:
    print('É \033[32mVOGAL\033[0;0m\n')
else:
    print('NÃO É \033[32mVOGAL\033[0;0m\n')

for i in range(1, 6):
    print(str(i) + ': \033[32mPalmeiras\033[0;0m não tem mundial')

print('\n')

for letra in 'Santos na serie B':
    if letra in vogal:
        print('\033[32m' + letra + '\033[0;0m')
    else:
        print(letra)
