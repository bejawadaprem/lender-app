from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container

"""


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(20):
            item = OneLineListItem(text='Item ' + str(i))
            item.bind(on_release=self.on_item_click)  # Bind on_release event
            self.root.ids.container.add_widget(item)

    def on_item_click(self, instance):
        # Deselect all other items
        for item in self.root.ids.container.children:
            if isinstance(item, OneLineListItem):
                item.bg_color = (1, 1, 1, 1)  # Reset background color for all items

        # Change the background color of the clicked item
        instance.bg_color = (0.5, 0.5, 0.5, 1)  # Change color as desired


DemoApp().run()
