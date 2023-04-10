
class Funcionario:
    def registra_hoas(self, horas):
        print('Horas registradas')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')


class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')


class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def buscar_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas no fórum.')


class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

jose = Junior()
jose.buscar_perguntas_sem_resposta()

lucas = Pleno()
lucas.buscar_perguntas_sem_resposta()
lucas.busca_cursos_mes()
lucas.mostrar_tarefas()