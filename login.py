import sqlite3

from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton, MDFlatButton

import anvil.server
from dashboard import DashScreen

anvil.server.connect("server_BQ6Z7GHPS3ZH5TPKQJBHTYJI-ZVMP6VAENIF2GORT")

KV = """
<WindowManager>:
    LoginScreen:

<LoginScreen>:
    MDFloatLayout:
        md_bg_color:1,1,1,1
        Image:
            source: "LOGO.png"
            pos_hint: {'center_x': 0.5, 'center_y': 0.93}
            size_hint: None, None
            size: "100dp", "100dp"
    
        MDLabel:
            id: label1
            text: 'Welcome Back!'
            font_size:dp(23)
            
            halign: 'center'
            font_name:"Roboto-Bold"
            underline:"True"
            pos_hint: {'center_x': 0.5, 'center_y': 0.81}
        MDLabel:
         
            text: 'Login to continue'
            color:6/255, 143/255, 236/255, 1
            font_size:dp(16)
            halign: 'center'
          
            pos_hint: {'center_x': 0.5, 'center_y': 0.77}
        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.8, None
            height: "80dp"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            canvas.before:
                Color:
                    rgba: 1,1,1,1
                Line:
                    rectangle: self.x, self.y, self.width, self.height
            MDTextField:
                id: email      
                hint_text: "Email"
                helper_text_mode: "on_focus"
                icon_right: "account"
                font_name: "Roboto-Bold"
                pos_hint: {'center_x': 0.5, 'center_y': 0.57}
            MDTextField:
                id: password
                hint_text: "Password"
                helper_text: "Enter your password"
                helper_text_mode: "on_focus"
                icon_right: "lock"
                password: not password_visibility.active
                size_hint_y: None
                height: "30dp"
                width: dp(200)
                pos_hint: {'center_x': 0.5, 'center_y': 0.46}
                on_text_validate: app.validate_password()
        BoxLayout:
            orientation: 'horizontal'
            size_hint_y: None
            height: "29dp"
            spacing:dp(5)
            pos_hint: {'center_x': 0.6, 'center_y': 0.4}
            MDCheckbox:
                id: password_visibility
                size_hint: None, None
                size: "30dp", "30dp"
                active: False
                on_active: root.on_checkbox_active(self, self.active)

            MDLabel:
                text: "Show Password"
                font_size:dp(14)
                size: "30dp", "30dp"
                theme_text_color: "Secondary"
                halign: "left"
                valign: "center"      
        GridLayout:
            cols: 2
            spacing:dp(20)
            padding:dp(20)
            pos_hint: {'center_x': 0.5, 'center_y': 0.32}
            size_hint: 1, None
            height: "50dp"
            MDRaisedButton:
                text: "Back"
                on_release: app.root.current ='MainScreen'
                md_bg_color: 0.031, 0.463, 0.91, 1
                theme_text_color: 'Custom'
                text_color: 1, 1, 1, 1
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
            MDRaisedButton:
                text: "Login"
                on_release: root.go_to_dashboard()
                md_bg_color: 0.031, 0.463, 0.91, 1
                pos_hint: {'right': 1, 'y': 0.5}
                size_hint: 1, None
                height: "50dp"
                font_name: "Roboto-Bold"
        MDLabel:
            id: error_text
            text: ""

    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        width: "190dp"
        height: "35dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.2}

        MDLabel:
            text: "Don't have an account?"
            font_size:dp(14)
            theme_text_color: 'Secondary'
            halign: 'center'
            valign: 'center'

        MDFlatButton:
            text: "Sign Up"
            font_size:dp(18)
        
            theme_text_color: 'Custom'
            text_color: 6/255, 143/255, 236/255, 1
            on_release: root.go_to_signup()


"""


class LoginScreen(Screen):
    Builder.load_string(KV)

    def on_checkbox_active(self, checkbox, value):
        # Handle checkbox state change
        # Update password visibility based on the checkbox state
        if hasattr(self, 'login_screen'):
            self.login_screen.ids.password.password = not value
            print(value)

    def go_to_dashboard(self):
        # Get the entered email and password
        entered_email = self.ids.email.text
        entered_password = self.ids.password.text

        if not entered_email or "@" not in entered_email or "." not in entered_email:
            self.show_error_dialog("Invalid email address")
            return

        if not entered_password:
            self.show_error_dialog("Please enter password")
            return

        conn = sqlite3.connect("fin_user_profile.db")
        cursor = conn.cursor()

        cursor.execute('''
            SELECT * FROM fin_users
            WHERE email = ?
        ''', (entered_email,))

        user_data = cursor.fetchone()
        data = self.login_data()
        email_list = []
        password_list = []
        a = 0
        for i in data:
            a += 1
            email_list.append(i['email'])
            password_list.append(i['password_hash'])

        if user_data:

            if user_data[4] == entered_password:  # Fix index to 4 for the password field

                users = cursor.execute('''SELECT * FROM fin_users''')
                id_list = []
                for i in users:
                    id_list.append(i[0])

                for i in id_list:
                    if i == user_data[0]:

                        cursor.execute('''
                                        UPDATE fin_users SET customer_status = 'logged'
                                        WHERE user_id = ?
                                    ''', (user_data[0],))
                        conn.commit()
                    else:
                        cursor.execute('''
                                        UPDATE fin_users SET customer_status = ''
                                        WHERE user_id = ?
                                    ''', (i,))
                        conn.commit()

                sm = self.manager
                lender_screen = DashScreen(name='DashScreen')
                sm.add_widget(lender_screen)
                sm.transition.direction = 'left'  # Set the transition direction explicitly
                sm.current = 'DashScreen'
                conn.close()

            else:

                self.show_error_dialog("Incorrect password")
        elif entered_email in email_list:
            for i in range(a):
                print(i, email_list[i], password_list[i])
                if email_list[i] == entered_email and password_list[i] == entered_password:
                    self.manager.current = 'DashScreen'
            print(email_list, password_list, a)
        else:

            self.show_error_dialog("Invalid credentials")

    def show_error_dialog(self, message):

        dialog = MDDialog(
            text=message,
            size_hint=(0.8, 0.3),
            buttons=[
                MDFlatButton(
                    text="OK",
                    on_release=lambda *args: dialog.dismiss()
                )
            ]
        )
        dialog.open()

    def go_to_signup(self):
        from signup import SignupScreen
        sm = self.manager
        lender_screen = SignupScreen(name='SignupScreen')
        sm.add_widget(lender_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'SignupScreen'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):

        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'MainScreen'

    def login_data(self):
        return anvil.server.call('login_data')


class MyScreenManager(ScreenManager):
    pass
