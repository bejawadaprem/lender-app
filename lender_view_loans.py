
import anvil.server
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition,ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition

view_loans ='''
<WindowManager>:
    ViewLoansScreen:
    ALlLoansScreen:
<ViewLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1  # Make the size stretchable

        MDTopAppBar:
            title: "View Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            size_hint: 1, 1  # Make the size stretchable

            Button:
                text: "Open Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                


            Button:
                text: "Closed Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                
            Button:
                text: "Approved Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                

            Button:
                text: "Rejected Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                

            Button:
                text: "All Loans"
                size_hint_y: None
                background_color: 1, 1 ,1, 0 
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 1  # Border color (black in this example)
                    Line:
                        width: 0.4  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
                on_release: root.all_loanscreen()

<ALlLoansScreen> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        ScrollView:

            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height


                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: 0

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 1, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]


                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                text: 'Loan ID'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True


                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True

                            MDLabel:
                                text: 'Loan Status'
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed
                                size_hint_x: None
                                width: dp(20)
                                bold: True
                        Widget:
                            size_hint_y: None
                            height: dp(2) 
                            canvas:
                                Color:
                                    rgba: 0, 0, 1, 1
                                Line:
                                    width: dp(0.6)  # Set the width of the line to make it bold
                                    points: self.x, self.y, self.x + self.width, self.y

'''

a = 50

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon{i}"
    view_loans += f'''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: {id_label}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed

                            MDLabel:
                                id: {amount}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed


                            MDLabel:
                                id: {status}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed


                            MDIconButton:
                                id: {icon}
                                icon: 'arrow-right-thick'
                                opacity: 0
                                size_hint_y: None
                                height: dp(50)  # Adjust the height as needed

    '''

Builder.load_string(view_loans)
conn = sqlite3.connect('fin_user_profile.db')
cursor = conn.cursor()
class ALlLoansScreen(Screen):
    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        cursor.execute('select * from fin_users')
        rows = cursor.fetchall()
        row_id_list = []
        status = []
        for row in rows:
            row_id_list.append(row[0])
            status.append(row[-1])
        if 'logged' in status:
            log_index = status.index('logged')
        else:
            # Handle the case where 'logged' is not in the list (choose an appropriate default index)
            log_index = 0  # Or any other suitable default value depending on your requirements

        data = self.get_table_data()

        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []

        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['loan_updated_status'])

        c = -1
        index_list = []
        for id in customer_id:
            c += 1
            if row_id_list and 0 <= log_index < len(row_id_list) and id == row_id_list[log_index]:
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            id_label = f"label_{k}"
            amount = f"amount_{k}"
            status = f"status_{k}"
            icon = f"icon{k}"

            label_1 = self.ids[id_label]
            label_1.text = loan_id[i]
            label_2 = self.ids[amount]
            label_2.text = str(loan_amount[i])
            label_3 = self.ids[status]
            label_3.text = loan_status[i]
            icon = self.ids[icon]
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def on_back_button_press(self):

        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ViewLoansScreen(name=' ViewLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = ' ViewLoansScreen'

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')


class ViewLoansScreen(Screen):
    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        # Handle the back button event
        if key == 27:  # 27 is the keycode for the hardware back button on Android
            self.go_back()
            return True  # Consume the event, preventing further handling
        return False  # Continue handling the event

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'
    def on_back_button_press(self):
        self.manager.current = 'LenderDashboard'
    def all_loanscreen (self):
        #self.manager.current = 'ViewProfileScreen'
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen =  ALlLoansScreen(name=' ALlLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = ' ALlLoansScreen'
class MyScreenManager(ScreenManager):
    pass
