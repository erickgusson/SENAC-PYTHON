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

''' 01 - Atividade
 - Solicitar um numero ao usuario
 - se o numero for menor ou igual a peça que o usuario digite navamente até receber um numero valido
 - deve percorre do 0 até o numero escolhido
 - no laço se o numero for PAR deve ficar em AZUL e se for IMPAR deve ficar em VERMELHO
'''

valor = input("Digite um numero maior que 0: \033[32m")
print('\033[0;0m')

while int(valor) <= 0:
    valor = input('digite um novo número que seja maior que zero: \033[32m')
    print('\033[0;0m')

for i in range(0, int(valor) + 1):
    if i % 2 == 0:
        print('\033[34m' + str(i) + '\033[0;0m')
    else:
        print('\033[31m' + str(i) + '\033[0;0m')