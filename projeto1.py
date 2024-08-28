from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class CinemaQuiz(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.index = 0
        self.score = 0

        self.questions = [
            {"question": "Oi, cinéfilo! \nDescobriremos se você é realmente fã de cinema e outros filmes :)", "options": ["INICIAR"], "correct": "INICIAR"},
            {"question": "Quando foi criado um dos primeiros filmes da história?", "options": ["1877", "1888", "1898","1903"], "correct": "1888", "justification": "O título da obra considerada um dos primeiros filmes da história do cinema é Roundhay Garden Scene. \nTrata-se de um curta-metragem realizado no Reino Unido no ano de 1888. A produção tem apenas dois segundos de duração e a autoria é do inventor francês Louis Le Prince. ", "image":"rdw.jpg"},
            {"question": "Quantas pessoas já negaram receber o Oscar?", "options": ["0", "2", "3", "5"], "correct": "3"},
            {"question": "Qual o filme mais bem avaliado do Quentin Tarantino?", "options": ["Cães de Aluguel", "Pulp Fiction", "Kill Bill", "Django Livre"], "correct": "Cães de Aluguel"},
            {"question": "Qual a cena eleita a mais tocante de todos os filmes já feitos?", "options": ["Morte da mãe do Bambi", "E.T. se despedindo do menino Elliot", "Morte do Mufasa em Rei Leão", "Cena da moeda e conversa entre Molly e seu falecido marido Sam em Ghost"], "correct": "E.T. se despedindo do menino Elliot"},
            {"question": "Qual a única atriz brasileira foi indicada ao Oscar?", "options": ["Juliana Paes", "Suzana Vieira", "Fernanda Montenegro", "Jade Picon"], "correct": "Fernanda Montenegro"},
            {"question": "Qual é a maior bilheteria da história?", "options": ["Vingadores: Ultimato", "Avatar", "Titanic", "Star Wars: O Despertar da Força"], "correct": "Avatar"},
            {"question": "Qual a maior bilheteria de 2024?", "options": ["Deadpool & Wolverine", "Duna: Parte 2", "Divertida Mente 2", "Meu Malvado Favorito 4"], "correct": "Divertida Mente 2"}
        ]
        self.layout = BoxLayout(orientation='vertical')

        # Adicionando a cor de fundo amarela
        with self.layout.canvas.before:
            Color(237, 227, 0, 1)  # Amarelo, RGBA
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        # Adicionando imagem icon
        self.image = Image(source='icon.png')
        self.layout.add_widget(self.image)

        self.question_label = Label(text=self.questions[self.index]["question"], color=(0,0,0,1))
        self.layout.add_widget(self.question_label)

        self.listabotoes = []
        self.adicionar_botões()

        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def adicionar_botões(self):
        for option in self.questions[self.index]["options"]:
            btn = Button(text=option, on_press=self.check_answer)
            self.listabotoes.append(btn)
            self.layout.add_widget(btn)

    def check_answer(self, instance):
        if self.index==0:
            self.next_question()
            return

        elif instance.text == self.questions[self.index]["correct"]:
            self.score += 1
            result = "Correto!"
        else:
            result = f"Errado! A resposta correta era: {self.questions[self.index]['correct']}"

        # Mostra um popup com o resultado e avança para a próxima pergunta
        result_popup = Popup(
            title='Resultado',
            content=Label(text=result),
            size_hint=(None, None), size=(400, 200),
            on_dismiss=self.next_question
        )
        result_popup.open()

    def next_question(self, *args):
        self.index += 1

        if self.index < len(self.questions):
            self.update_question()
        else:
            self.show_score()

    def update_question(self):
        self.question_label.text = self.questions[self.index]["question"]

        for btn in self.listabotoes:
            self.layout.remove_widget(btn)
        self.listabotoes.clear()

        self.adicionar_botões()

    def show_score(self):
        # Cria a mensagem inicial com a pontuação
        score_message = f'Sua pontuação: {self.score}/{(len(self.questions)-1)}\n\n'

        # Adiciona a mensagem dependendo da pontuação
        if self.score <= 3:
            message = 'Você não é um fã de cinema, sinto muito!'
        elif 4 <= self.score < 6:
            message = 'Você está no caminho para ser um fã de cinema!'
        else:
            message = 'Você definitivamente é um fã de cinema!'

        # Combina a mensagem de pontuação com a mensagem condicional
        full_message = score_message + message

        # Cria e exibe o Popup com a mensagem completa
        score_popup = Popup(
            title='Quiz Concluído',
            content=Label(text=full_message),
            size_hint=(None, None), size=(500, 200)
        )

        score_popup.open()

if __name__ == '__main__':
    CinemaQuiz().run()
