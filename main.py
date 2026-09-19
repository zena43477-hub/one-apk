from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Calc(BoxLayout):
    def __init__(self, **kw):
        super().__init__(orientation="vertical", padding=20, spacing=15, **kw)
        self.a = TextInput(hint_text="Введите первое число", multiline=False,
                           input_filter="float", font_size=32)
        self.b = TextInput(hint_text="Введите второе число", multiline=False,
                           input_filter="float", font_size=32)
        self.add_widget(self.a)
        self.add_widget(self.b)

        row = BoxLayout(spacing=10)
        for op in ["+", "-", "*", "/"]:
            btn = Button(text=op, font_size=40)
            btn.bind(on_release=lambda w, o=op: self.calc(o))
            row.add_widget(btn)
        self.add_widget(row)

        self.out = Label(text="Результат:", font_size=32)
        self.add_widget(self.out)

    def calc(self, op):
        try:
            a = float(self.a.text)
            b = float(self.b.text)
        except ValueError:
            self.out.text = "Введите оба числа"
            return
        if op == "+":
            result = a + b
        elif op == "-":
            result = a - b
        elif op == "*":
            result = a * b
        elif op == "/":
            result = "Деление на ноль" if b == 0 else a / b
        else:
            result = "Неизвестная операция"
        self.out.text = f"Результат: {result}"


class CalcApp(App):
    def build(self):
        return Calc()


CalcApp().run()
