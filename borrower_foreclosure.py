from kivymd.app import MDApp
from kivymd.uix.list import *
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from datetime import datetime

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

import anvil.server

anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

loan_forecloseB = '''
<WindowManager>:
    LoansDetailsB:
    ViewProfileScreenFB:
    ForecloseDetails:

<LoansDetailsB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Open Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container

<ViewProfileScreenFB>
    MDBoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]

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
                        text: "View Loan details"
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
                        height: dp(850)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: loan
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Loan Amount:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Borrower Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Tenure(Months):" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: tenure
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Interest Rate:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: interest
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Credit limit:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: limit
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Total Payment Made:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: total_payment
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: dp(10)
                            padding: dp(10)
                            MDLabel:
                                text: "Foreclosure Type:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: closer_type
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                        MDGridLayout:
                            cols: 2
                            spacing: 10

                            CheckBox:
                                size_hint: (None, None)
                                width: 50
                                bold: True
                                color: (195/255,110/255,108/255,1)

                            MDLabel:
                                text: "I Agree Terms and Conditions"
                                multiline: False


                        MDGridLayout:
                            cols: 2
                            spacing: 30
                            padding: 20
                            size_hint: 1, 1
                            pos_hint: {'center_x': 0.48, 'center_y': 0.5}

                            MDRaisedButton:
                                text: "BACK"
                                md_bg_color: 0.031, 0.463, 0.91, 1
                                on_release: root.on_back()
                                text_color: 1, 1, 1, 1
                                size_hint: 1, None


                            MDRaisedButton:
                                id: foreclose_button
                                text: "FORECLOSE"
                                md_bg_color: 0.031, 0.463, 0.91, 1
                                on_release: root.on_back_button_press()
                                size_hint: 1, None


<ForecloseDetails>
    BoxLayout:
        orientation: 'vertical'
        padding: dp(10)  
        spacing: dp(20) 
        ScrollView:
            do_scroll_x: False
            BoxLayout:
                orientation: "vertical"
                padding: dp(10) 
                spacing: dp(25)   
                size_hint_y: None
                height: self.minimum_height
                BoxLayout:
                    orientation: "vertical"
                    padding: dp(10) 
                    spacing: dp(25) 

                    MDLabel:
                        text: "Loan Foreclosure For LoanA/C:"
                        bold: True
                    MDLabel:
                        id: loan_id_label1
                        bold:True

                MDLabel:
                    text: "Loan Foreclosure Payment Details :"

                Widget:
                    size_hint_y: None
                    height: dp(2)  
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y
                MDLabel:
                    text: "Amount paid"
                    bold: True

                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(33)  

                    MDLabel:
                        text: "Total amount Paid "
                        bold: True

                    MDLabel:
                        id: totalamount
                        text: ""

                    MDLabel:
                        text: "Monthly installment"

                    MDLabel:
                        id: monthly_installment
                        text: ""

                    MDLabel:
                        text: "Interest Amount"

                    MDLabel:
                        id: interes_tamount
                        text: ""

                    MDLabel:
                        text: "Monthly EMI"

                    MDLabel:
                        id: monthly_emi
                        text: ""
                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: "Loan Closure Amount"
                    bold: True
                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(52)

                    MDLabel:
                        text: "Over Outstanding Amount"
                        bold: True

                    MDLabel:
                        id: overall_amount
                        text: ""
                    MDLabel:
                        text: "Overall Interest Amount "

                    MDLabel:
                        id: overall_interest_amount
                        text: ""

                    MDLabel:
                        text: "Total Amount"

                    MDLabel:
                        id: total_amount
                        text: ""

                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 1 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                MDLabel:
                    text: "Loan Closure Amount"
                    bold: True

                GridLayout:
                    cols: 2
                    size_hint_y: None
                    padding: dp(10)
                    spacing: dp(45)

                    MDLabel:
                        text: "Outstanding Amount"
                        bold: True

                    MDLabel:
                        id: outstanding_amount
                        text: ""

                    MDLabel:
                        text: "Foreclosure Fee "

                    MDLabel:
                        id: foreclosure_fee
                        text: ""

                    MDLabel:
                        text: "Foreclosure Amount"

                    MDLabel:
                        id: foreclosure_amount
                        text: ""

                Widget:
                    size_hint_y: None
                    canvas:
                        Color:
                            rgba: 0, 0, 0, 0 
                        Line:
                            points: self.x, self.y, self.x + self.width, self.y

                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: None

                    MDLabel:
                        text: 'Reason for Foreclosure '
                        valign: 'top'
                        bold: True

                    MDTextField:
                        hint_text: 'Enter text here'

                BoxLayout:
                    orientation: "horizontal"
                    size_hint_y: None
                    spacing: dp(10)

                    CheckBox:
                        size_hint: None, None
                        width: dp(30) 
                        color: (195/255, 110/255, 108/255, 1)

                    MDLabel:
                        text: "I Agree Terms and Conditions"
                        multiline: False  

                MDLabel:
                    text: ""

                MDGridLayout:
                    cols: 2
                    spacing: dp(10)
                    padding: dp(5)
                    size_hint: 1, None

                    MDRaisedButton:
                        text: "CANCEL"
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        theme_text_color: 'Custom'
                        on_release: app.root.current = 'ViewProfileScreenFB'
                        text_color: 1, 1, 1, 1
                        size_hint: 1, None

                    MDRaisedButton:
                        text: "SUBMIT"
                        id : submit
                        md_bg_color: 0.031, 0.463, 0.91, 1
                        on_release: root.add_data( outstanding_amount, foreclosure_fee, foreclosure_amount,requested_on, status)
                        size_hint: 1, None

'''
Builder.load_string(loan_forecloseB)
date = datetime.today()
print(date)


class LoansDetailsB(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = self.get_table_data()
        customer_id = []
        loan_id = []
        borrower_name = []
        loan_status = []
        s = 0
        for i in data:
            s += 1
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_full_name'])
            loan_status.append(i['loan_updated_status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'disbursed':
                index_list.append(c)

        b = 1
        k = -1
        for i in index_list:
            b += 1
            k += 1
            item = ThreeLineAvatarIconListItem(

                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Loan ID : {loan_id[i]}",
                secondary_text=f"Borrower Name: {borrower_name[i]}",
                tertiary_text=f"Status: {loan_status[i]}",
            )
            item.bind(on_release=self.icon_button_clicked)  # Corrected the binding
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == value:
                loan_status = loan['loan_updated_status']
                break

        if loan_status == 'disbursed':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            disbursed = ViewProfileScreenFB(name='ViewProfileScreenFB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(disbursed)

            # Switch to the LoginScreen
            sm.current = 'ViewProfileScreenFB'
            self.manager.get_screen('ViewProfileScreenFB').initialize_with_value(value, data)

        else:
            # Handle other loan statuses or show an error message
            pass

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def go_back(self):
        self.manager.current = 'DashboardScreen'


class ViewProfileScreenFB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # on_release: root.foreclose_details(loan.text)

    def initialize_with_value(self, value, data):
        loan_id = []
        loan_amount = []
        name = []
        tenure = []
        interest = []
        credit = []
        payment_made = []
        foreclose_type = []

        for i in data:
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            name.append(i['borrower_full_name'])
            tenure.append(i['tenure'])
            interest.append(i['interest_rate'])
            credit.append(i['credit_limit'])
            payment_made.append(i['total_payments_made'])
            foreclose_type.append(i['foreclosure_type'])
        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan.text = str(loan_id[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.name.text = str(name[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.interest.text = str(interest[index])
            self.ids.limit.text = str(credit[index])
            self.ids.total_payment.text = str(payment_made[index])
            self.ids.closer_type.text = str(foreclose_type[index])

            if int(tenure[index]) >= 12:
                self.ids.foreclose_button.disabled = False

            else:
                self.show_popup("Tenure Warning", "Your tenure needs to be more than 12 months")
                self.ids.foreclose_button.disabled = True

    def show_popup(self, title, content):
        popup = Popup(title=title, content=Label(text=content), size_hint=(None, None), size=(400, 200))
        popup.open()

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

    def on_back_button_press(self):
        self.manager.current = 'LoansDetailsB'

    def on_keyboard(self, window, key, *args):
        if key == 27:  # Key code for the 'Escape' key
            # Keyboard is closed, move the screen down
            self.screen_manager.y = 0
        return True

    def on_start(self):
        Window.softinput_mode = "below_target"

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')

    def foreclose_details(self, value):
        data = self.get_table_data()

        sm = self.manager
        # Create a new instance of the LoginScreen
        profile = ForecloseDetails(name='ForecloseDetails')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ForecloseDetails'
        self.manager.get_screen('ForecloseDetails').initialize_with_value(value, data)


class ForecloseDetails(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        loan_id = []
        outstading_amount = []
        forecloser_fee = []
        forecloser_amount = []
        request_on = []

        for i in data:
            loan_id.append(i['loan_id'])
            outstading_amount.append(i['outstanding_amount'])
            forecloser_fee.append(i['foreclose_fee'])
            forecloser_amount.append(i['foreclose_amount'])
            request_on.append(i['requested_on'])

            requested_on_value = None

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id_label1.text = str(loan_id[index])
            self.ids.outstanding_amount.text = str(outstading_amount[index])
            self.ids.foreclosure_fee.text = str(forecloser_fee[index])
            self.ids.foreclosure_amount.text = str(forecloser_amount[index])

            requested_on_value = date
        self.add_data(
            loan_id=self.ids.loan_id_label1.text,
            outstanding_amount=int(self.ids.outstanding_amount.text),
            foreclose_fee=int(self.ids.foreclosure_fee.text),
            foreclose_amount=int(self.ids.foreclosure_amount.text),
            requested_on=requested_on_value,
            status='under process'
        )

    def add_data(self, loan_id, outstanding_amount, foreclose_fee, foreclose_amount, requested_on, status):
        # Ensure 'YOUR_ANVIL_UPLINK_KEY' is replaced with your actual Anvil Uplink key
        anvil.server.call('get_foreclose_data', loan_id, outstanding_amount, foreclose_fee, foreclose_amount,
                          requested_on, status)


class MyScreenManager(ScreenManager):
    pass


