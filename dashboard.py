from kivy.core.window import Window
from kivy.lang import Builder
from kivy.modules import cursor
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import SlideTransition
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
import sqlite3

from borrowerlanding import BorrowerLanding
from lender_landing import LenderLanding
import anvil
KV = """


<DashScreen>:
    canvas.before:
        Color:
            rgba:  1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source: "LOGO.png"
        pos_hint: {'center_x': 0.5, 'center_y': 0.97}
        size_hint: None, None
        size: "100dp", "100dp"

    Label:
        text: 'An RBI registered NBFC '
        font_size:dp(13)

        pos_hint: {'center_x': 0.5, 'center_y': 0.92}
        color:1/255, 26/255, 51/255, 1
        underline:"True"

    Image:
        source: "dashboardlogo.jpg"
        pos_hint: {'center_x': 0.5, 'center_y': 0.69}
        size_hint: None, None
        size: "200dp", "250dp"

    Label:
        id:username
        pos_hint: {'center_x': 0.5, 'center_y': 0.41}
        color: 1/255, 26/255, 51/255, 1
        bold:"True"
        font_size:dp(23)

    Label:
        text: 'Start your journey with us,'
        font_size:dp(20)
        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
        color: 0, 0, 0, 1


    MDRaisedButton:
        text: 'Continue as Borrower'
        on_release: root.go_to_borrower_landing()

        size_hint: (None, None)
        padding:dp(10)
        height: dp(100)  # Fixed height
        pos_hint: {'center_x': 0.5, 'center_y': 0.25}
        theme_text_color: "Custom"
        text_color:1,1,1,1
        md_bg_color:0.043, 0.145, 0.278, 1   
        font_name: "Roboto-Bold"
        font_size:dp(15)

    MDRaisedButton:
        text: 'Continue as Lender'
        on_release: root.go_to_lender_landing()
        size_hint: (None,None)
        font_name: "Roboto-Bold"
        border_radius: [1, 1, 1, 1]
        height: dp(120)  # Fixed height
        pos_hint: {'center_x': 0.5, 'center_y': 0.15}
        theme_text_color: "Custom"
        text_color: 1,1,1,1
        md_bg_color:0.043, 0.145, 0.278, 1      

        font_size:dp(15)
"""


class DashScreen(Screen):
    Builder.load_string(KV)

    def get_email(self):
        data = anvil.server.call('another_method')
        return data

    def profile(self):
        return anvil.server.call('profile')
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.on_pre_enter()

    def load_user_data(self):
        pass

    def on_pre_enter(self):
        # Connect to the SQLite database
        profile = self.profile()
        log_email = self.get_email()

        email_user = []
        name_list = []
        for i in profile:
            email_user.append(i['email_user'])
            name_list.append(i['full_name'])

        # Check if 'logged' is in the status list
        if log_email in email_user:
            log_index = email_user.index(log_email)
            self.ids.username.text = name_list[log_index]
        else:
            # Handle the case when 'logged' is not in the status list
            self.ids.username.text = "User Not Logged In"

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
        self.manager.current = 'DashScreen'

    def switch_screen(self, screen_name):
        print(f"Switching to screen: {screen_name}")

        # Get the screen manager
        sm = self.manager

        sm.transition = SlideTransition(direction='left')
        sm.current = screen_name

    def go_to_lender_landing(self):
        # Get the screen manager
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = LenderLanding(name='LenderLanding')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'LenderLanding'

    def go_to_borrower_landing(self):
        # Get the screen manager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = BorrowerLanding(name='BorrowerLanding')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'BorrowerLanding'
