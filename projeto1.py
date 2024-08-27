from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle

class AnimeQuiz(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def build(self):
        self.index = 0
        self.score = 0

        self.questions = [
            {"question": "Saudações aos visitantes de Westeros! \nDescobriremos se você é realmente um fã de Game of Thrones :)", "options": ["DRACARYS"], "correct": "DRACARYS"},
            {"question": "Qual é a casa mais antiga de Westeros?", "options": ["Casa Lannister", "Casa Targaryen", "Casa Stark", "Casa Velaryon"], "correct": "Casa Targaryen"},
            {"question": "Quantas vezes a familia Stark aparece junta na série t", "options": ["Tóquio", "Nova York", "Londres"], "correct": "Tóquio"},
            {"question": "Qual o nome do renomado rei dos piratas em One Piece?", "options": ["Luffy", "Shanks", "Roger"], "correct": "Roger"},
            {"question": "Em Hunter x Hunter, qual o sobrenome da família do personagem Killua?", "options": ["Zoldick", "Silva", "D."], "correct": "Zoldick"},
            {"question": "Qual é o título em inglês do anime japonês conhecido como Shingeki no Kyojin?", "options": ["Fullmetal Alchemist", "Attack on Titan", "My Hero Academia"], "correct": "Attack on Titan"},
            {"question": "Quais são os números escritos nos bottons de Gon e Killua (respectivamente) no Exame Hunter?", "options": ["(105/87)", "(905/49)", "(405/99)"], "correct": "(405/99)"},
            {"question": "Qual o maior medo do Goku?", "options": ["Perder a Chichi (esposa)", "Agulha", "Bills (Deus da Destruição)"], "correct": "Agulha"}
        ]
        self.layout = BoxLayout(orientation='vertical')

        # Adicionando a cor de fundo vermelha
        with self.layout.canvas.before:
            Color(255, 255, 0, 1)  # Vermelho, RGBA
            self.rect = Rectangle(size=self.layout.size, pos=self.layout.pos)

        self.layout.bind(size=self._update_rect, pos=self._update_rect)

        self.image = Image(source='got.png')
        self.layout.add_widget(self.image)


        self.question_label = Label(text=self.questions[self.index]["question"], color=(0,0,0,1))
        self.layout.add_widget(self.question_label)

        self.listabotoes = []
        self.add_buttons()

        return self.layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def add_buttons(self):
        for option in self.questions[self.index]["options"]:
            btn = Button(text=option, on_press=self.check_answer)
            self.listabotoes.append(btn)
            self.layout.add_widget(btn)

    def check_answer(self, instance):
        if instance.text == self.questions[self.index]["correct"]:
            self.score += 1

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

        self.add_buttons()

    def show_score(self):
        # Cria a mensagem inicial com a pontuação
        score_message = f'Sua pontuação: {self.score}/{len(self.questions)}\n\n'

        # Adiciona a mensagem dependendo da pontuação
        if self.score <= 3:
            message = 'Poderia ser melhor, talvez você seja um bastardo!'
        elif 4 <= self.score < 6:
            message = 'Você poderia comandar uma casa de Westeros com todo esse conhecimento!'
        else:
            message = 'Você estaria sentado no Trono de Ferro com todo este poder!'

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
    AnimeQuiz().run()
