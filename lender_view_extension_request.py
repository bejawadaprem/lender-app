import anvil.server
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.app import MDApp
from kivy.uix.label import Label
from kivy.uix.popup import Popup

anvil.server.connect('server_BQ6Z7GHPS3ZH5TPKQJBHTYJI-ZVMP6VAENIF2GORT')

lender_view_extension = """
<WindowManager>:
    NewExtension:
    ApprovedLoansE:
    RejectedLoansE:
    UnderProcessLoansE:
    ViewProfileE:

<NewExtension>
    BoxLayout:
        orientation: 'vertical'
        size_hint: 1, 1 
        pos_hint: {'center_x':0.5, 'center_y':0.5}

        MDTopAppBar:
            title: "View Extension Request"
            elevation: 2
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

        MDGridLayout:
            cols: 2
            padding: dp(15)
            spacing: dp(5)
            pos_hint: {'center_x': .5, 'center_y': .5}


            Button:
                text: "Approved Loans"
                background_color: 0.529, 0.807, 0.922, 0 
                color: 0, 0, 0, 1
                on_release: root.approved_loans()
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  # Border width
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "View All Loans"
                background_color: 0.529, 0.807, 0.922, 0
                on_release: root.all_loans()
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
            Button:
                text: "Rejected Loans"
                background_color: 0.529, 0.807, 0.922, 0
                on_release: root.rejected_loans()
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba: 0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)



            Button:
                text: "UnderProcess Loans"
                text_color: 0, 0, 0, 1
                on_release: root.under_process_loans()
                background_color: 0.529, 0.807, 0.922, 0
                color: 0, 0, 0, 1
                bold: True
                canvas.before:
                    Color:
                        rgba:0.529, 0.807, 0.922, 1 
                    Line:
                        width: 0.9  
                        rounded_rectangle: (self.x, self.y, self.width, self.height, 15)
"""

lender_view_extension += '''
<ApprovedLoansE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Approved Loans "
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]

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
                                rgba: 0, 0, 1, 1 
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]


                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                text: 'Loan ID'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True


                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True

                            MDLabel:
                                text: 'Loan Extension Status'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50) 
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
                                    width: dp(0.6)  
                                    points: self.x, self.y, self.x + self.width, self.y


'''

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: {id_label}
                                text: ''
                                size_hint_y: None
                                height: dp(50)

                            MDLabel:
                                id: {amount}
                                text: ''
                                size_hint_y: None
                                height: dp(50) 


                            MDLabel:
                                id: {status}
                                text: ''
                                size_hint_y: None
                                height: dp(50) 


                            MDIconButton:
                                id: {icon}
                                icon: 'arrow-right-thick'
                                size_hint_y: None
                                height: dp(50) 
                                on_release: root.icon_button_clicked({id_label}.text)
                                opacity: 0
'''

lender_view_extension += '''
<ViewAllLoansE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View All Loans "
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
                                rgba: 0, 0, 1, 1 
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]


                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                text: 'Loan ID'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True


                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True

                            MDLabel:
                                text: 'Loan Extension status'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50)
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
                                    width: dp(0.6)  
                                    points: self.x, self.y, self.x + self.width, self.y


'''

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: {id_label}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  

                            MDLabel:
                                id: {amount}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  


                            MDLabel:
                                id: {status}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  


                            MDIconButton:
                                id: {icon}
                                icon: 'arrow-right-thick'
                                size_hint_y: None
                                height: dp(50)  
                                on_release: root.icon_button_clicked({id_label}.text)
                                opacity: 0
'''
lender_view_extension += '''
<RejectedLoansE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Rejected Loans "
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]

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
                                rgba: 0, 0, 1, 1 
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]


                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                text: 'Loan ID'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True


                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True

                            MDLabel:
                                text: 'Loan Extension Status'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50)  
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
                                    width: dp(0.6) 
                                    points: self.x, self.y, self.x + self.width, self.y


'''

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: {id_label}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  

                            MDLabel:
                                id: {amount}
                                text: ''
                                size_hint_y: None
                                height: dp(50)  


                            MDLabel:
                                id: {status}
                                text: ''
                                size_hint_y: None
                                height: dp(50) 


                            MDIconButton:
                                id: {icon}
                                icon: 'arrow-right-thick'
                                size_hint_y: None
                                height: dp(50) 
                                on_release: root.icon_button_clicked({id_label}.text)
                                opacity: 0
'''
lender_view_extension += '''
<UnderProcessLoansE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Under Process Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]

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
                                rgba: 0, 0, 1, 1  
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]


                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                text: 'Loan ID'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True


                            MDLabel:
                                text: 'Loan Amount'
                                size_hint_y: None
                                height: dp(50) 
                                bold: True

                            MDLabel:
                                text: 'Loan Extension Status'
                                size_hint_y: None
                                height: dp(50)  
                                bold: True
                            MDLabel:
                                text: ''
                                size_hint_y: None
                                height: dp(50) 
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
                                    width: dp(0.6)  
                                    points: self.x, self.y, self.x + self.width, self.y


'''

a = 8

for i in range(a):
    id_label = f"label_{i}"
    amount = f"amount_{i}"
    status = f"status_{i}"
    icon = f"icon_{i}"
    lender_view_extension += f'''
                        GridLayout:
                            cols: 4
                            spacing: dp(20)
                            MDLabel:
                                id: {id_label}
                                text: ''
                                size_hint_y: None
                                height: dp(50) 

                            MDLabel:
                                id: {amount}
                                text: ''
                                size_hint_y: None
                                height: dp(50) 


                            MDLabel:
                                id: {status}
                                text: ''
                                size_hint_y: None
                                height: dp(50)


                            MDIconButton:
                                id: {icon}
                                icon: 'arrow-right-thick'
                                size_hint_y: None
                                height: dp(50)  
                                on_release: root.icon_button_clicked({id_label}.text)
                                opacity: 0

'''
lender_view_extension += f'''
<ViewProfileE>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
        ScrollView:

            MDBoxLayout:
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    id: box1
                    orientation: 'vertical'
                    size_hint_y: None
                    MDLabel:
                        text: "Loan Extension details"
                        halign: "center"
                        bold: True
                MDBoxLayout:
                    orientation: 'vertical'
                    size_hint_y: None
                    height: self.minimum_height
                    padding: dp(20)

                    BoxLayout:
                        id: box1
                        orientation: 'vertical'
                        size_hint_y: None
                        height: dp(900)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1 
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loanid
                                text: ""
                            MDLabel:
                                text: "Borrower Name" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: name
                                text: "" 
                            MDLabel:
                                text: "Loan Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: amount
                                text: "" 
                            MDLabel:
                                text: "Extension Fee(%)" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: extension
                                text: "" 
                            MDLabel:
                                text: "Extension Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: extension_amount
                                text: "" 
                            MDLabel:
                                text: "Total Paid Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: total_amount
                                text: "" 
                            MDLabel:
                                text: "Remaining Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: remaining_amount
                                text: "" 
                            MDLabel:
                                text: "Reason For Extension" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: reason
                                text: "" 
                            MDLabel:
                                text: "New EMI" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: interest
                                text: "" 

                            MDRaisedButton:
                                text: "Reject"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                text_color: 0, 0, 0, 1
                                on_release: root.reject_request()
                                font_name: "Roboto-Bold.ttf"
                                size_hint: 1, None

                            MDRaisedButton:
                                text: "Accept"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                on_release: root.accept_request()
                                theme_text_color: 'Primary'
                                font_name: "Roboto-Bold.ttf"
                                text_color: 0, 0, 0, 1
                                size_hint: 1, None
'''
Builder.load_string(lender_view_extension)


class NewExtension(Screen):
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
        self.manager.current = 'borrower_dashboard'

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'LenderDashboard'

    def approved_loans(self):
        sm = self.manager
        borrower_screen = ApprovedLoansE(name='ApprovedLoansE')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'ApprovedLoansE'

    def rejected_loans(self):
        sm = self.manager
        borrower_screen = ApprovedLoansE(name='RejectedLoansE')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'RejectedLoansE'

    def under_process_loans(self):
        sm = self.manager
        borrower_screen = ApprovedLoansE(name='UnderProcessLoansE')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'UnderProcessLoansE'

    def all_loans(self):
        sm = self.manager
        borrower_screen = ApprovedLoansE(name='ViewProfileE')
        sm.add_widget(borrower_screen)
        sm.transition.direction = 'left'  # Set the transition direction explicitly
        sm.current = 'ViewProfileE'


class ApprovedLoansE(Screen):
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[i] == 'approved':
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            id_label = f"label_{k}"
            amount = f"amount_{k}"
            status = f"status_{k}"
            icon = f"icon_{k}"  # Fix the variable name here

            label_1 = self.ids[id_label]
            label_1.text = loan_id[i]
            label_2 = self.ids[amount]
            label_2.text = str(loan_amount[i])
            label_3 = self.ids[status]
            label_3.text = loan_status[i]
            icon = self.ids[icon]  # Fix the variable name here
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def go_back(self):
        screen_manager = NewExtension()
        screen_manager.add_widget(NewExtension(name='NewExtension'))

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileE'
        self.manager.get_screen('ViewProfileE').initialize_with_value(value, data)


class ViewAllLoansE(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0

        # Separate lists for different loan statuses
        approved_loans = []
        rejected_loans = []
        underprocess_loans = []

        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

            # Categorize loans based on status
            if i['status'] == 'approved':
                approved_loans.append(s - 1)
            elif i['status'] == 'rejected':
                rejected_loans.append(s - 1)
            elif i['status'] == 'under process':
                underprocess_loans.append(s - 1)

        # Iterate over approved loans
        k = -1
        for i in approved_loans:
            k += 1
            self.populate_loan_data(i, k, loan_id, loan_amount, loan_status)

        # Iterate over rejected loans
        for i in rejected_loans:
            k += 1
            self.populate_loan_data(i, k, loan_id, loan_amount, loan_status)

        # Iterate over under process loans
        for i in underprocess_loans:
            k += 1
            self.populate_loan_data(i, k, loan_id, loan_amount, loan_status)

        # Iterate over new loans

    def populate_loan_data(self, i, k, loan_id, loan_amount, loan_status):
        id_label = f"label_{k}"
        amount = f"amount_{k}"
        status = f"status_{k}"
        icon = f"icon_{k}"  # Fix the variable name here

        label_1 = self.ids[id_label]
        label_1.text = loan_id[i]
        label_2 = self.ids[amount]
        label_2.text = str(loan_amount[i])
        label_3 = self.ids[status]
        label_3.text = loan_status[i]
        icon = self.ids[icon]  # Fix the variable name here
        icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 30
        self.ids.box1.height = h

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileE'
        self.manager.get_screen('ViewProfileE').initialize_with_value(value, data)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):
        screen_manager = NewExtension()
        screen_manager.add_widget(NewExtension(name='NewExtension'))

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')


class RejectedLoansE(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[i] == 'rejected':
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            id_label = f"label_{k}"
            amount = f"amount_{k}"
            status = f"status_{k}"
            icon = f"icon_{k}"  # Fix the variable name here

            label_1 = self.ids[id_label]
            label_1.text = loan_id[i]
            label_2 = self.ids[amount]
            label_2.text = str(loan_amount[i])
            label_3 = self.ids[status]
            label_3.text = loan_status[i]
            icon = self.ids[icon]  # Fix the variable name here
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def icon_button_clicked(self, value):
        data = self.get_table_data()  # Fetch data here
        self.manager.current = 'ViewProfileE'
        self.manager.get_screen('ViewProfileE').initialize_with_value(value, data)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):
        screen_manager = NewExtension()
        screen_manager.add_widget(NewExtension(name='NewExtension'))

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')

    def icon_button_clicked(self, value):
        data = self.get_table_data()
        self.manager.current = 'ViewProfileE'
        self.manager.get_screen('ViewProfileE').initialize_with_value(value, data)


class UnderProcessLoansE(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        customer_id = []
        loan_id = []
        loan_amount = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_full_name'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            loan_status.append(i['status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[i] == 'under process':
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            id_label = f"label_{k}"
            amount = f"amount_{k}"
            status = f"status_{k}"
            icon = f"icon_{k}"  # Fix the variable name here

            label_1 = self.ids[id_label]
            label_1.text = loan_id[i]
            label_2 = self.ids[amount]
            label_2.text = str(loan_amount[i])
            label_3 = self.ids[status]
            label_3.text = loan_status[i]
            icon = self.ids[icon]  # Fix the variable name here
            icon.opacity = 1

        h = self.ids.box1.height

        for i in range(a + 1):
            h += 150
        self.ids.box1.height = h

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_extension_data')

    def icon_button_clicked(self, value):
        self.manager.current = 'ViewProfileE'
        self.manager.get_screen('ViewProfileE').initialize_with_value(value)

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):
        screen_manager = NewExtension()
        screen_manager.add_widget(NewExtension(name='NewExtension'))


class ViewProfileE(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        borrower_name = []
        loan_id = []
        loan_amount = []
        extension_fee = []
        extension_amount = []
        reason_for_extension = []
        remaining_amount = []
        new_emi = []

        for i in data:
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_amount.append(i['loan_amount'])
            extension_fee.append(i['extend_fee'])
            extension_amount.append(i['extension_amount'])
            reason_for_extension.append(i['reason'])
            remaining_amount.append(i['final_repayment_amount'])
            new_emi.append(i['new_emi'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loanid.text = str(loan_id[index])
            self.ids.name.text = str(borrower_name[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.extension.text = str(extension_fee[index])
            self.ids.extension_amount.text = str(extension_amount[index])
            self.ids.reason.text = str(reason_for_extension[index])
            self.ids.remaining_amount.text = str(remaining_amount[index])
            self.ids.interest.text = str(new_emi[index])

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_keyboard)
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_keyboard)
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def go_back(self):
        screen_manager = NewExtension()
        screen_manager.add_widget(NewExtension(name='NewExtension'))

    def accept_request(self):
        # Code to send the request to the borrower for accepting the loan extension
        # Replace the following line with your actual logic
        print("Request Accepted")
        # Optionally, you can display a message to the user or navigate to another screen
        self.show_acceptance_popup()

    def reject_request(self):
        # Code to reject the loan extension request
        # Replace the following line with your actual logic
        print("Request Rejected")
        # Optionally, you can display a pop-up message to the user
        self.show_rejection_popup()

    def show_acceptance_popup(self):
        # Code to show a popup message for acceptance
        popup = Popup(title='',
                      content=Label(text='Your loan extension request has been accepted.'),
                      size_hint=(None, None), size=(400, 200))
        popup.open()

    def show_rejection_popup(self):
        # Code to show a popup message for rejection
        popup = Popup(title='',
                      content=Label(text='Your loan extension request has been rejected.'),
                      size_hint=(None, None), size=(400, 200))
        popup.open()


class MyScreenManager(ScreenManager):
    pass
