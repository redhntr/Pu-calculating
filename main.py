from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
#from kivy.uix.button import Button
from kivy.core.window import Window

# глобальные настройки окна
Window.size = (300, 600)
Window.clearcolor = (255/255, 190/255, 152/255, 1)
Window.title = "Расчет Объема на колесо"

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.wheel = Label(text='Диаметр колеса')
        self.form = Label(text='Диаметр формы')
        self.height = Label(text='Высота колеса (с подложкой)')
        self.density = Label(text='Плотность преполимера 1.15/1.3')
        self.procent = Label(text='% отвердителя')
        self.volume = Label(text='Общий объем')
        self.volumePP = Label(text='Объем Преполимера')

        self.input_wheel = TextInput(hint_text='Введите значение (мм)', multiline=False)
        self.input_wheel.bind(text=self.on_text)

        self.input_form = TextInput(hint_text='Введите значение (мм)', multiline=False)
        self.input_form.bind(text=self.on_text)

        self.input_height = TextInput(hint_text='Введите значение (мм)', multiline=False)
        self.input_height.bind(text=self.on_text)

        self.input_density = TextInput(hint_text='Введите значение', multiline=False)
        self.input_density.bind(text=self.on_text)

        self.input_procent = TextInput(hint_text='Введите значение (%)', multiline=False)
        self.input_procent.bind(text=self.on_text)

    def on_text(self, *args):
        input_wheel = self.input_wheel.text.replace(",", ".")
        input_form = self.input_form.text.replace(",", ".")
        input_height = self.input_height.text.replace(",", ".")
        input_density = self.input_density.text.replace(",", ".")
        input_procent = self.input_procent.text.replace(",", ".")
        volume = self.volume.text


        some_list = [input_wheel, input_form, input_height, input_density, input_procent]
        try:
            all([i.isnumeric() for i in some_list])
            volume_result = round(((3.14 * float(input_form) ** 2 * float(input_height)) / 4000000 - (3.14 * float(input_wheel) ** 2 * float(input_height))/4000000) * float(input_density), 3)

            self.volume.text = 'Общий объем: ' + str(volume_result)
            self.volumePP.text = 'Объем Преполимера: ' + str(round(volume_result * 100 / (float(input_procent) + 100), 3))


        except:
            self.volume.text = ''
            self.volumePP.text = 'Введите число'


    def build(self):

        box = BoxLayout(orientation='vertical')
        box.add_widget(self.wheel)
        box.add_widget(self.input_wheel)
        box.add_widget(self.form)
        box.add_widget(self.input_form)
        box.add_widget(self.height)
        box.add_widget(self.input_height)
        box.add_widget(self.density)
        box.add_widget(self.input_density)
        box.add_widget(self.procent)
        box.add_widget(self.input_procent)
        box.add_widget(self.volume)
        box.add_widget(self.volumePP)

        return box


if __name__ == "__main__":
    MyApp().run()
