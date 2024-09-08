from kivy.app import App # Importa a classe App para aplicação no Kivy
from kivy.uix.boxlayout import BoxLayout # Organiza widgets e cria interfaces
from kivy.uix.button import Button # Cria botões na interface 
from kivy.uix.label import Label # Exibe texto 
from kivy.uix.popup import Popup # Apresenta janelas Pop-Up na tela
from kivy.uix.image import Image # Adciona imagens
from kivy.graphics import Color, Rectangle # Cor aos gráficos e uso de retângulos na tela
from random import shuffle # Aleatoriza algo

class CinemaQuiz(App): 
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
#Cinema Quiz faz uso do import App e tudo o que for gerado depois vai estar relacionado com isto
#**kwargs generaliza os argumentos, quando você não sabe quais serão usados
    
    def build(self): #build faz parte da classe App do kivy, framework chama build quando é iniciado
        self.index = 0
        self.pontucao = 0
        #atributos index e pontuação zerados para serem modificados durante o desenrolar do quiz

        self.primeiraquestao = [{"questao": "Oi, cinéfilo! \nDescobriremos se você é realmente fã de cinema e outros filmes :)", "opcoes": ["INICIAR"], "correta": "INICIAR"}]
        outrasquestoes = [
            {"questao": "Quando foi criado um dos primeiros filmes da história?", "opcoes": ["1877", "1888", "1898", "1903"], "correta": "1888"},
            {"questao": "Quantas pessoas já negaram receber o Oscar?", "opcoes": ["0", "2", "3", "5"], "correta": "3"},
            {"questao": "Qual o filme mais bem avaliado do Quentin Tarantino?", "opcoes": ["Cães de Aluguel", "Pulp Fiction", "Kill Bill", "Django Livre"], "correta": "Cães de Aluguel"},
            {"questao": "Qual a cena eleita a mais tocante de todos os filmes já feitos?", "opcoes": ["Morte da mãe do Bambi", "E.T. se despedindo do menino Elliot", "Morte do Mufasa em Rei Leão", "Cena da moeda e conversa entre Molly e seu falecido marido Sam em Ghost"], "correta": "E.T. se despedindo do menino Elliot"},
            {"questao": "Qual a única atriz brasileira foi indicada ao Oscar?", "opcoes": ["Juliana Paes", "Suzana Vieira", "Fernanda Montenegro", "Jade Picon"], "correta": "Fernanda Montenegro"},
            {"questao": "Qual é a maior bilheteira da história?", "opcoes": ["Vingadores: Ultimato", "Avatar", "Titanic", "Star Wars: O Despertar da Força"], "correta": "Avatar"},
            {"questao": "Qual a maior bilheteira de 2024?", "opcoes": ["Deadpool & Wolverine", "Duna: Parte 2", "Divertida Mente 2", "Meu Malvado Favorito 4"], "correta": "Divertida Mente 2"},
            {"questao": "Em qual filme a famosa frase \"Eu sou o rei do mundo!\" foi dita?", "opcoes": ["Titanic", "O Grande Gatsby", "King Kong", "Gladiador"], "correta": "Titanic"},
            {"questao": "Quem foi o criador do estúdio de animação Pixar?", "opcoes": ["Walt Disney", "John Lasseter", "Steve Jobs", "George Lucas"], "correta": "Steve Jobs"},
            {"questao": "Qual filme detém o recorde de maior orçamento já gasto em sua produção?", "opcoes": ["Avatar", "Piratas do Caribe: Navegando em Águas Misteriosas", "Vingadores: Ultimato", "Liga da Justiça"], "correta": "Piratas do Caribe: Navegando em Águas Misteriosas"}
        ]
        #atribuito self.primeira questão e outras questões, em que faz uso de uma lista de dicionario com os termos questao, opcoes e correta
        shuffle(outrasquestoes) #embaralhamento das questoes
        self.questoes = self.primeiraquestao + outrasquestoes #combinação da lista de perguntas para facilitar na contagem da pontuação

        self.layout = BoxLayout(orientation='vertical')  #cria um layout para os widgets verticalmente

        # Adicionando a cor de fundo amarela
        with self.layout.canvas.before: #define o que tem que aparecer na parte de trás da tela "BEFORE CANVAS"
            Color(237, 227, 0, 1)  # Amarelo, RGBA
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)
            #Rectangle=forma do layout usado | size define que esse tamanho vai ser igual ao BoxLayout | pos indica que a posiçao vai ser a mesma que a BoxLayout
        self.layout.bind(size=self._update_rect, pos=self._update_rect)
            #bind atualiza dinamicamente a interface gráfica do Kivy | _update_rect atualiza o layout para não haver falhas

        # Adicionando imagem icon
        self.image = Image(source='icon.png')
        self.layout.add_widget(self.image)

        self.questao_label = Label(text=self.questoes[self.index]["questao"], color=(0,0,0,1))
        self.layout.add_widget(self.questao_label)
        #self.questao_label cria atributo para veicular o Label, que é responsável por apresentar texto na tela 
        #self.index aponta para a pergunta atual 
        #["questao"] aponta para a questão dentro do dicionario

        self.listabotoes = [] #inicializa uma lista para armazenar botões
        self.adicionar_botões() #chama um método para criar e adicionar botões à lista e ao layout

        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        #altera de fato o valor do que foi feito acima com o bind

    def adicionar_botões(self):
        for opcao in self.questoes[self.index]["opcoes"]:
            btn = Button(text=opcao, on_press=self.conferir_resposta) #on_press dá permissão para conferir a resposta
            self.listabotoes.append(btn) #adiciona os botões a lista de botoes
            self.layout.add_widget(btn)
        #metodo que cria os botoes e mostra oq tem que ser feito em cada um deles ,

    def conferir_resposta(self, instance): #atualiza a pontuação
        if self.index == 0:
            self.proxima_questao()
            return 
            #como a "primeira pergunta" é a introdução do quiz, pulammos para não afetar a pontuação total

        elif instance.text == self.questoes[self.index]["correta"]: #instance.text é a resposta selecionada pelo usuário
            self.pontucao += 1
            resultado = "Mandou bem, acertou!"
        else:
            resultado = f"Errou! A resposta correta era: {self.questoes[self.index]['correta']}"

        # Mostra um popup com o resultado e avança para a próxima pergunta
        resultado_popup = Popup(
            title='Resultado',
            content=Label(text=resultado),
            size_hint=(None, None), size=(400, 200), #hint atribui formato fixo ao popup e não altera e o size tbm fez  isso
            on_dismiss=self.proxima_questao #quando o popup fechar, vai pra próxima questao
        )
        resultado_popup.open()

    def proxima_questao(self, *args):
        self.index += 1 #move o usuária entre os indices das questoes

        if self.index < len(self.questoes):
            self.mudar_questao() 
        else:
            self.mostrar_pontuacao()
        #mensura a quantidade de questoes para aplicar as funçoes corretamente 

    def mudar_questao(self):
        self.questao_label.text = self.questoes[self.index]["questao"] #busca o indice, altera a questao e aplica a variavel

        for btn in self.listabotoes:
            self.layout.remove_widget(btn) #remove os botoes para aplicar outros
        self.listabotoes.clear() #limopa a lista dos botoes para não haver duplicados

        self.adicionar_botões() #adiciona os novos botoes

    def mostrar_pontuacao(self):
        # cria a mensagem inicial com a pontuação
        score_message = f'Sua pontuação: {self.pontucao}/{(len(self.questoes) - 1)}\n\n'

        # addiciona a mensagem dependendo da pontuação
        if self.pontucao <= 3:
            message = 'Você não é um fã de cinema, sinto muito!'
        elif 4 <= self.pontucao < 7:
            message = 'Você está no caminho para ser um fã de cinema!'
        else:
            message = 'Você definitivamente é um fã de cinema!'

        # combina a mensagem de pontuação com a mensagem condicional
        full_message = score_message + message

        # cria e exibe o Popup com a mensagem completa
        pontuacao_popup = Popup(
            title='Quiz Concluído',
            content=Label(text=full_message),
            size_hint=(None, None), size=(500, 200)
        )

        pontuacao_popup.open()

if __name__ == '__main__':
    CinemaQuiz().run() #execução do quiz

