from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from random import shuffle

class CinemaQuiz(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.index = 0
        self.pontucao = 0

        self.primeiraquestao = [{"questao": "Oi, cinéfilo! \nDescobriremos se você é realmente fã de cinema e outros filmes :)", "opcoes": ["INICIAR"], "correta": "INICIAR"}]
        outrasquestoes = [
            {"questao": "Quando foi criado um dos primeiros filmes da história?", "opcoes": ["1877", "1888", "1898","1903"], "correta": "1888"},
            {"questao": "Quantas pessoas já negaram receber o Oscar?", "opcoes": ["0", "2", "3", "5"], "correta": "3"},
            {"questao": "Qual o filme mais bem avaliado do Quentin Tarantino?", "opcoes": ["Cães de Aluguel", "Pulp Fiction", "Kill Bill", "Django Livre"], "correta": "Cães de Aluguel"},
            {"questao": "Qual a cena eleita a mais tocante de todos os filmes já feitos?", "opcoes": ["Morte da mãe do Bambi", "E.T. se despedindo do menino Elliot", "Morte do Mufasa em Rei Leão", "Cena da moeda e conversa entre Molly e seu falecido marido Sam em Ghost"], "correta": "E.T. se despedindo do menino Elliot"},
            {"questao": "Qual a única atriz brasileira foi indicada ao Oscar?", "opcoes": ["Juliana Paes", "Suzana Vieira", "Fernanda Montenegro", "Jade Picon"], "correta": "Fernanda Montenegro"},
            {"questao": "Qual é a maior bilheteria da história?", "opcoes": ["Vingadores: Ultimato", "Avatar", "Titanic", "Star Wars: O Despertar da Força"], "correta": "Avatar"},
            {"questao": "Qual a maior bilheteria de 2024?", "opcoes": ["Deadpool & Wolverine", "Duna: Parte 2", "Divertida Mente 2", "Meu Malvado Favorito 4"], "correta": "Divertida Mente 2"}
        ]
        shuffle(outrasquestoes)
        self.questoes= self.primeiraquestao + outrasquestoes

        self.layout = BoxLayout(orientation='vertical')



        # Adicionando a cor de fundo amarela
        with self.layout.canvas.before:
            Color(237, 227, 0, 1)  # Amarelo, RGBA
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Adicionando imagem icon
        self.image = Image(source='icon.png')
        self.layout.add_widget(self.image)

        self.questao_label = Label(text=self.questoes[self.index]["questao"], color=(0,0,0,1))
        self.layout.add_widget(self.questao_label)

        self.listabotoes = []
        self.adicionar_botões()

        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def adicionar_botões(self):
        for opcao in self.questoes[self.index]["opcoes"]:
            btn = Button(text=opcao, on_press=self.conferir_resposta()
            self.listabotoes.append(btn)
            self.layout.add_widget(btn)

    def conferir_resposta(self, instance):
        if self.index==0:
            self.proxima_questao()
            return

        elif instance.text == self.questoes[self.index]["correta"]:
            self.pontucao += 1
            result = "Correto!"
        else:
            result = f"Errado! A resposta correta era: {self.questoes[self.index]['correta']}"

        # Mostra um popup com o resultado e avança para a próxima pergunta
        result_popup = Popup(
            title='Resultado',
            content=Label(text=result),
            size_hint=(None, None), size=(400, 200),
            on_dismiss=self.proxima_questao
        )
        result_popup.open()

    def proxima_questao(self, *args):
        self.index += 1

        if self.index < len(self.questoes):
            self.mudar_questao()
        else:
            self.mostrar_pontuacao()

    def mudar_questao(self):
        self.questao_label.text = self.questoes[self.index]["questao"]

        for btn in self.listabotoes:
            self.layout.remove_widget(btn)
        self.listabotoes.clear()

        self.adicionar_botões()

    def mostrar_pontuacao(self):
        # Cria a mensagem inicial com a pontuação
        score_message = f'Sua pontuação: {self.pontuacao}/{(len(self.questoes)-1)}\n\n'

        # Adiciona a mensagem dependendo da pontuação
        if self.pontuacao <= 3:
            message = 'Você não é um fã de cinema, sinto muito!'
        elif 4 <= self.pontuacao < 6:
            message = 'Você está no caminho para ser um fã de cinema!'
        else:
            message = 'Você definitivamente é um fã de cinema!'

        # Combina a mensagem de pontuação com a mensagem condicional
        full_message = score_message + message

        # Cria e exibe o Popup com a mensagem completa
        pontuacao_popup = Popup(
            title='Quiz Concluído',
            content=Label(text=full_message),
            size_hint=(None, None), size=(500, 200)
        )

        pontuacao_popup.open()

if __name__ == '__main__':
    CinemaQuiz().run()
