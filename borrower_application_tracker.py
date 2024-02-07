from kivy import platform
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager
import sqlite3

application_tracker = """

<WindowManager>:
    ApplicationTrackerScreen:

<ApplicationTrackerScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

        MDTopAppBar:
            title: "Application Tracker"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.borrower_dashboard()]]

        BoxLayout:
            id: box
            orientation: 'vertical'
            padding: dp(30)
            spacing: dp(40)

            MDLabel:
                text: 'Application Received'
                font_size: dp(20)
                bold: True
                size_hint_y: None
                height: 50

            MDLabel:
                text: "Congratulations! Your first loan application with P2P has been received. Please wait while we process the loan. You can check the status here"
                size_hint_y: None
                height: 50


            MDGridLayout:
                cols: 2
                spacing: dp(20)  # Adjust spacing between icon and label

                MDIconButton:
                    id: icon1
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50

                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label1
                    text: "Application for #loanamount sent"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon2
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    size_hint_y: None
                    height: 50

                    text_color: 12/255, 105/255, 171/255, 1
                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label2
                    text: "Waiting for approval"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon3
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label3
                    text: "Loan is approved for #loanamount"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50

                MDIconButton:
                    id: icon4
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50
                    canvas:
                        Color:
                            rgba: 12/255, 105/255, 171/255, 1
                        Line:
                            width: 2
                            points: self.x + dp(24), self.y + dp(12) , self.x + dp(24), self.y - dp(34)


                MDLabel:
                    id: label4
                    text: "Loan is under disbursal process"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height: 50


                MDIconButton:
                    id: icon5
                    icon: "checkbox-blank-circle-outline"
                    theme_text_color: "Custom"
                    text_color: 12/255, 105/255, 171/255, 1
                    size_hint_y: None
                    height: 50


                MDLabel:
                    id: label5
                    text: "Loan credited to a/c xxxxxxxxxxx"
                    theme_text_color: "Custom"
                    text_color: 86/255, 94/255, 97/255, 1
                    size_hint_y: None
                    height:dp(50)


"""
class ApplicationTrackerScreen(Screen):

    Builder.load_string(application_tracker)
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def go_back(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def borrower_dashboard(self):
        self.manager.current = 'DashboardScreen'

class WindowManager(ScreenManager):
    pass