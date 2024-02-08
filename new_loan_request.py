from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager, SlideTransition
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.slider import MDSlider
from kivymd.uix.label import MDLabel
import sqlite3

user_helpers2 = """
<WindowManager>:
    NewloanScreen:
    NewloanScreen1:
    NewloanScreen2:
    
<NewloanScreen>:

    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: [10, 0]
        spacing: 15
        orientation: 'vertical'
        radius: [10,]
        MDGridLayout:
            cols: 2
            spacing: dp(10)
            padding: dp(10)
            MDLabel:
                text: "Credit Limit" 
                font_size: 36
            MDLabel:
                id: credit_limit
                text: "" 
        MDGridLayout:
            cols: 1
            spacing: dp(10)
            BoxLayout:
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                elevation: 2
                padding: [40, 0]
                spacing: 25
                orientation: 'horizontal'

                MDLabel:
                    size_hint: 1, None
                    width: dp(300)
                    text: "Product Group"
                    bold: True

                Spinner:
                    id: group_id
                    text: "Select Group"
                    width: dp(300)
                    multiline: False
                    size_hint: 1, None
                    background_color: 1, 1 ,1, 0 
                    color: 0, 0, 0, 1
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        MDGridLayout:
            cols: 1
            spacing: dp(10)
            BoxLayout:
                pos_hint: {'center_x':0.5, 'center_y':0.5}
                elevation: 2
                padding: [40, 0]
                spacing: 25
                orientation: 'horizontal'

                MDLabel:
                    size_hint: 1, None
                    width: dp(300)
                    text: "Product Categories"
                    bold: True

                Spinner:
                    id: group_id
                    text: "Select Categories"
                    width: dp(300)
                    multiline: False
                    size_hint: 1, None
                    background_color: 1, 1 ,1, 0 
                    color: 0, 0, 0, 1
                    canvas.before:
                        Color:
                            rgba: 0, 0, 0, 1  
                        Line:
                            width: 0.7
                            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
        MDGridLayout:
            cols: 2
            spacing: 30
            padding: [20, 0]
            size_hint: 1, 1
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDRaisedButton:
                text: "NEXT"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: root.go_to_newloan_screen1()
                size_hint: 1, None                    


        MDLabel:
            text:""

<NewloanScreen1>:

    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: [40, 0]
        spacing: 25
        orientation: 'vertical'
        radius: [10,]

        MDLabel:
            text: "New Loan Request"
            halign: "center"
            bold: True
        Widget:
            size_hint_y: None
            height: 5

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    points: self.x, self.y, self.x + self.width, self.y

        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Loan ID"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDLabel:
                    id: loan id
                    text: ""

        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Loan Amount"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDTextField:
                    id: text_input1
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Interest Amount (%)"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDLabel:
                    id: text_input2
                    text: ""

        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Processing Fee"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDLabel:
                    id: text_input3
                    text: ""


        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Loan Period (Months)"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDTextField:
                    id: text_input5
                    size_hint: None, None
                    size_hint_x: 0.91
                    multiline: False
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    line_color_normal: [1, 1, 1, 1]  
                    line_color_focus: [1, 1, 1, 1]
                    font_name: "Roboto-Bold"
        MDLabel:
            text: "EMI Amount"
            bold: True
            halign: "left"
        MDBoxLayout:
            orientation: "horizontal"

            MDGridLayout:
                cols: 2
                spacing: 10

                CheckBox:
                    size_hint: (None, None)
                    width: 50
                    bold: True
                    color: (195/255,110/255,108/255,1)

                MDLabel:
                    text: "One Time"
                    multiline: False
            MDGridLayout:
                cols: 2
                spacing: 10

                CheckBox:
                    size_hint: (None, None)
                    width: 50
                    bold: True
                    color: (195/255,110/255,108/255,1)

                MDLabel:
                    text: "Monthly"
                    multiline: False
            MDGridLayout:
                cols: 2
                spacing: 10

                CheckBox:
                    size_hint: (None, None)
                    width: 50
                    bold: True
                    color: (195/255,110/255,108/255,1)

                MDLabel:
                    text: " Three Months"
                    multiline: False
            MDGridLayout:
                cols: 2
                spacing: 10

                CheckBox:
                    size_hint: (None, None)
                    width: 50
                    bold: True
                    color: (195/255,110/255,108/255,1)

                MDLabel:
                    text: " Six Months"
                    multiline: False
        MDLabel:
            text: " "


        MDGridLayout:
            cols: 2
            spacing: 30
            padding: [20, 0]
            size_hint: 1, 1
            pos_hint: {'center_x': 0.48, 'center_y': 0.5}

            MDRaisedButton:
                text: "NEXT"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: root.go_to_newloan_screen2()
                size_hint: 1, None

<NewloanScreen2>:

    BoxLayout:
        pos_hint: {'center_x':0.5, 'center_y':0.5}
        elevation: 2
        padding: [40, 0]
        spacing: 25
        orientation: 'vertical'
        radius: [10,]

        MDLabel:
            text: "Loan Summary"
            halign: "center"
            bold: True
        Widget:
            size_hint_y: None
            height: 5

            canvas:
                Color:
                    rgba: 0, 0, 0, 1  
                Line:
                    points: self.x, self.y, self.x + self.width, self.y

        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Loan Amount"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDLabel:
                    id: loanamount
                    text: ""

        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Total interest amount"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1 
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDLabel:
                    id: interestamount
                    text: " "
        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Processing Fee Amount"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDLabel:
                    id: text_input2
                    text: ""

        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Monthly EMI"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  # Border line width

                MDLabel:
                    id: text_input3
                    text: ""


        MDGridLayout:
            cols: 2
            spacing: 60

            MDLabel:
                text: "Total Repayment Amount"

            MDFloatLayout:
                size_hint: None, None
                size: dp(200), dp(40)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                size_hint_x: 1
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1  
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [10, 10, 10, 10]

                    Color:
                        rgba: 0, 0, 0, 1  

                    Line:
                        rounded_rectangle: [self.x + 5, self.y + 0.9, self.width - 2, self.height - 0.5, 10, 10, 10, 10]
                        width: 1  

                MDLabel:
                    id: text_input4
                    text: " "

        MDLabel:
            text: " "


        MDGridLayout:
            cols: 3
            spacing: 30
            padding: [20, 0]
            size_hint: 1, 1
            pos_hint: {'center_x': 0.48, 'center_y': 0.5}
            MDRaisedButton:
                text: "BACK"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.current = "ForecloseDetails"
                size_hint: 1, None
            MDRaisedButton:
                text: "EDIT"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.current = "ForecloseDetails"
                size_hint: 1, None

            MDRaisedButton:
                text: "NEXT"
                md_bg_color: 0.031, 0.463, 0.91, 1
                on_release: app.root.current = "ForecloseDetails"
                size_hint: 1, None

"""


class NewloanScreen(Screen):
    Builder.load_string(user_helpers2)

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

    def current(self):
        self.manager.current = 'DashboardScreen'

    def go_to_newloan_screen1(self):
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = NewloanScreen1(name='NewloanScreen1')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'NewloanScreen1'


class NewloanScreen1(Screen):
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
        self.manager.current = 'NewloanScreen'

    def current(self):
        self.manager.current = 'NewloanScreen'

    def go_to_newloan_screen2(self):
        # Get the existing ScreenManager
        sm = self.manager

        # Create a new instance of the LoginScreen
        login_screen = NewloanScreen2(name='NewloanScreen2')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(login_screen)

        # Switch to the LoginScreen
        sm.current = 'NewloanScreen2'


class NewloanScreen2(Screen):
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
        self.manager.current = 'NewloanScreen1'

    def current(self):
        self.manager.current = 'NewloanScreen1'


class MyScreenManager(ScreenManager):
    pass
