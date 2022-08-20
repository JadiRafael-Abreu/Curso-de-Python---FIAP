from funcoes import *


usuarios = {}

while True :
   opcao =  menu()

   if opcao == 0 :
        break
   elif opcao == 1 :
        cadastrar(usuarios)
   """elif opcao == 2 :
        editar(usuarios)
   elif opcao == 3 :
        remover(usuarios)
   elif opcao == 4 :
        listar(usuarios)"""        