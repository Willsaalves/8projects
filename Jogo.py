
  
# Projeto 7 - Jogo de Aventura
# Um jogo de decisões onde eu terei que criar varios finais diferentes baseados nas respostas que forem dadas

# Eu quero chegar a finais diferentes na minha historia, de acordo com as respostas que eu passe para o programa

# Qual é o cenário : Eu estou numa guerra entre duas nações, e nós temos 2 lados: LadoA e LadoB. Somente o ladoA irá vencer, e o ladoB irá perder! então eu tenho que tomar as decisões corretas para chegar até a vitória, que somente o ladoA irá conseguir!
import PySimpleGUI as sg
class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = ' Você nasceu na nação do ar ou nação do fogo? '
        self.pergunta2 = '  Você é paciente ou impaciente?' 
        self.pergunta3 = '  Você prefere um bisao voador ou um dragão '
        self.finalHistoria1 ='  Você será o avatar'
        self.finalHistoria2 ='  Você será o Governador Ozai'
        self.finalHistoria3 ='  Você tem grandes chances de ganhar'
        self.finalHistoria4 ='  Você vai se sacrificar'

        
    def Iniciar(self):
        # Layout
        layout = [
            [sg.Output(size=(50,0))],
            [sg.Input(size=(25,0),key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')]
        ]
        # criar a janela
        self.janela = sg.Window('Jogo do Avatar!',layout=layout)
        while True:
            # ler os dados
            self.LerValores()
            # fazer algo com os dados
            if self.evento == 'Iniciar':
                print(self.pergunta1)
                self.LerValores()
                if self.valores['escolha'] == 'ar':
                    print(self.pergunta2)
                    self.LerValores()
                    if self.valores['escolha'] == 'paciente':
                        print(self.finalHistoria1)
                    if self.valores['escolha'] == 'impaciente':
                        print(self.finalHistoria2)
                if self.valores['escolha'] == 'fogo':
                    print(self.pergunta3)
                    self.LerValores()
                    if self.valores['escolha'] == 'bisao':
                        print(self.finalHistoria3)
                    if self.valores['escolha'] == 'tatico':
                        print(self.finalHistoria4)
        
    def LerValores(self):
        self.evento, self.valores = self.janela.Read()

jogo = JogoDeAventura()
jogo.Iniciar()

