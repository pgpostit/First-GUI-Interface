import PySimpleGUI as psg

class TelaPython:
    def __init__(self):
        psg.change_look_and_feel('DarkBlue')
        #Layout
        layout = [
            [psg.Text('Nome',size=(5,0)),psg.Input(size=(15,0),key='nome')],
            [psg.Text('Idade',size=(5,0)),psg.Input(size=(15,0),key='idade')],
            [psg.Text('Provedores de e-mail: ')],
            [psg.Checkbox('Gmail',key='gmail'),psg.Checkbox('Outlook',key='outlook'),psg.Checkbox('Yahoo',key='yahoo')],
            [psg.Text('Aceita cartão: ')],
            [psg.Radio('Sim','cartões',key='AceitaCartão'),psg.Radio('Não','cartões',key='NãoAceitaCartão')],
            [psg.Slider(range(0,255),default_value=0,orientation='h',size=(15,20),key='SliderVelocidade')],
            [psg.Button('Enviar dados')],
            [psg.Output(size=(30,20))]
        ]
        #Janela
        self.janela = psg.Window("Dados do Usuário").layout(layout)
        #Extrair os dados da tela

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartão = self.values['AceitaCartão']
            não_aceita_cartão = self.values['NãoAceitaCartão']
            velocidadescript = self.values['SliderVelocidade']
            print(f'Nome: {nome}')
            print(f'Idade: {idade}')
            print(f'Aceita Gmail? {aceita_gmail}')
            print(f'Aceita Outlook? {aceita_outlook}')
            print(f'Aceita Yahoo? {aceita_yahoo}')
            print(f'Aceita Cartão? {aceita_cartão}')
            print(f'Não Aceita Cartão? {não_aceita_cartão}')
            print(f'Velocidade Script: {velocidadescript}')


tela = TelaPython()
tela.Iniciar()