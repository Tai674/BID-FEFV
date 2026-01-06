
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class Home(BoxLayout):
    pass

class ColossusAdmin(App):
    def build(self):
        Window.size = (360, 640)
        root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        root.add_widget(Label(text='Colossus Admin', font_size='24sp'))
        root.add_widget(Label(text='App gerado via GitHub Actions', font_size='16sp'))
        return root

if __name__ == '__main__':
    ColossusAdmin().run()
