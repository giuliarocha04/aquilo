from Model import *
from Dao import *

class ControllerAdicionarTarefa():
    def __init__(self, tarefa):
        self.tarefa = tarefa
        S = 0
        while S == 0:
            try:
                excluir_convert = int(self.excluir)
                excluir_convert -= 1
                if self.tarefa == "":
                    print("Informe uma tarefa valida")

                else:
                    if DAO.AdicionarTarefa(self.tarefa) == True:
                        print("Tarefa Adicionada")

                    else:
                        print("Algum problema foi encontrado ao tentar adicionar a tarefa")
                        S == 1
                 
            except Exception as error:
                print(error.__class__.__name__)
                print("Certifique-se de não passar um valor vazio")
            
class ControllerExcluirTarefa():
    def __init__(self, excluir):
        self.excluir = excluir
        S = 0
        while S == 0:

            try:
                excluir_convert = int(self.excluir)
    
                excluir_convert -= 1

                if TODO.ExcluirTarefa(self.excluir) == True:
                    excluir_convert = int(self.excluir)
                    excluir_convert -= 1

                    print("Tarefa Excluida")

                else:
                    print("Algum problema foi encontrado ao tentar excluir a tarefa")
                    S == 1
            
            except Exception as error:
                print(error.__class__.__name__)
                print("Certifique-se se o item informado está lista, e que você utilizou o ID do item.")
            
            
class ControllerListarTarefas():
    def __init__(self):
        ControllerLista = TODO.ListarTarefas()
        S = 0
        while S == 0:
        
            try:
                excluir_convert = int(self.excluir)
                excluir_convert -= 1
                for tarefas in ControllerLista:
                    print(tarefas)

            except Exception as error:
                print(error.__class__.__name__)
                print("Certifique-se se o item informado está lista, e que você utilizou o ID do item.")



            #augusto mono#augusto mono
            #menos augusto no mundo
            #augusto mono#augusto mono
            #menos augusto no mundo
            #augusto mono#augusto mono
            #menos augusto no mundo
            #augusto mono#augusto mono
