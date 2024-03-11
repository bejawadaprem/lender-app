from kivymd.app import MDApp
from kivymd.uix.list import *
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivy.utils import platform
from kivy.clock import mainthread
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.spinner import MDSpinner
from kivy.uix.modalview import ModalView
from kivy.clock import Clock
from kivy.animation import Animation
from kivymd.uix.label import MDLabel

if platform == 'android':
    from kivy.uix.button import Button
    from kivy.uix.modalview import ModalView
    from kivy.clock import Clock
    from android import api_version, mActivity
    from android.permissions import (
        request_permissions, check_permission, Permission)

import anvil.server

anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

kv = '''
<WindowManager>:
    DashboardScreenVLB:
    OpenLoanVLB:
    UnderProcessLoanVLB:
    RejectedLoanVLB:
    ViewLoansScreenVLB:



<DashboardScreenVLB>:
    MDFloatLayout:
        md_bg_color:1,1,1,1
        size_hint: 1, 1 

        MDTopAppBar:
            title: "Borrower View Loan"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            title_align: 'left'
            pos_hint: {'center_x': 0.5, 'center_y': 0.96}
            md_bg_color: 0.043, 0.145, 0.278, 1
            
        MDGridLayout:
            cols: 2
            spacing: dp(15)
            size_hint_y: None
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            height: self.minimum_height
            width: self.minimum_width
            size_hint_x: None

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.go_to_open_loans()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Open Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.go_to_under_loans()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "UnderProcess Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1 
                on_release: root.go_to_reject_loans()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Rejected Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}

            MDFlatButton:
                size_hint: None, None

                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                md_bg_color: 0.043, 0.145, 0.278, 1 

                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)
                on_release: root.go_to_app_tracker()
                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "Closed Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}


            MDFlatButton:
                size_hint: None, None
                md_bg_color: 0.043, 0.145, 0.278, 1
                on_release: root.go_to_foreclose_loans()
                size_hint_y: None
                height: dp(60)
                size_hint_x: None
                width: dp(110)

                BoxLayout:
                    orientation: 'horizontal'
                    spacing:dp(10)
                    MDLabel:
                        text: "ForeClose Loans"
                        font_size:dp(14)
                        bold:True
                        theme_text_color: 'Custom'
                        halign: "center"
                        text_color:1,1,1,1

<OpenLoanVLB>
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
<UnderProcessLoanVLB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "UnderProcess Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container1
<RejectedLoanVLB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Rejected Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container2
<ClosedLoanVLB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Close Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container3
<ForeCloseLoanVLB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Foreclose Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            title_align: 'left'
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container4

<ViewLoansScreenVLB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

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
                        height: dp(400)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
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
                                id: user1
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDLabel:
                                text: "Loan Amount:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Interest Rate:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: rate
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan Tenure:" 
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
                            MDLabel:
                                text: "Date Of Apply:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: date
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDLabel:
                                text: "Loan Updated Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: updated_status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

<ViewLoansScreenVLBB>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Profile"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
            md_bg_color: 0.043, 0.145, 0.278, 1

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
                        height: dp(400)

                        padding: [10, 0,0,0]
                        canvas.before:
                            Color:
                                rgba: 0, 0, 0, 1  # Blue color for the box
                            Line:
                                rectangle: self.pos[0], self.pos[1], self.size[0], self.size[1]

                        GridLayout:
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
                                id: user1
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Borrower Name:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: borrower_name
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"

                            MDLabel:
                                text: "Loan Amount:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Interest Rate:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: rate
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"


                            MDLabel:
                                text: "Loan Updated Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: updated_status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
'''
Builder.load_string(kv)


class DashboardScreenVLB(Screen):
    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=5)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def go_to_open_loans(self):
        modal_view = ModalView(size_hint=(None, None), size=(500, 200), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="25sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_go_to_open_loans(modal_view), 2)

    def performance_go_to_open_loans(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = OpenLoanVLB(name='OpenLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'OpenLoanVLB'

    def go_to_under_loans(self):
        modal_view = ModalView(size_hint=(None, None), size=(500, 200), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="25sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_go_to_under_loans(modal_view), 2)

    def performance_go_to_under_loans(self, modal_view):
        # Perform the actual action here (e.g., fetching loan requests)
        # For demonstration purposes, let's simulate a delay of 2 seconds
        # Replace this with your actual logic

        # Dismiss the modal view once the action is complete
        modal_view.dismiss()

        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = UnderProcessLoanVLB(name='UnderProcessLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'UnderProcessLoanVLB'

    def go_to_reject_loans(self):
        modal_view = ModalView(size_hint=(None, None), size=(500, 200), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="25sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_go_to_reject_loans(modal_view), 2)

    def performance_go_to_reject_loans(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = RejectedLoanVLB(name='RejectedLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'RejectedLoanVLB'

    def go_to_app_tracker(self):
        modal_view = ModalView(size_hint=(None, None), size=(500, 200), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="25sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_go_to_app_tracker(modal_view), 2)

    def performance_go_to_app_tracker(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ClosedLoanVLB(name='ClosedLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ClosedLoanVLB'

    def go_to_foreclose_loans(self):
        modal_view = ModalView(size_hint=(None, None), size=(500, 200), background_color=[0, 0, 0, 0])

        # Create MDLabel with white text color, increased font size, and bold text
        loading_label = MDLabel(text="Loading...", halign="center", valign="bottom",
                                theme_text_color="Custom", text_color=[1, 1, 1, 1],
                                font_size="25sp", bold=True)

        # Set initial y-position off-screen
        loading_label.y = -loading_label.height

        modal_view.add_widget(loading_label)
        modal_view.open()

        # Perform the animation
        self.animate_loading_text(loading_label, modal_view.height)

        # Perform the actual action (e.g., fetching loan requests)
        # You can replace the sleep with your actual logic
        Clock.schedule_once(lambda dt: self.performance_go_to_foreclose_loans(modal_view), 2)

    def performance_go_to_foreclose_loans(self, modal_view):
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ForeCloseLoanVLB(name='ForeCloseLoanVLB')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ForeCloseLoanVLB'

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):
        if key == 27:
            self.go_back()
            return True
        return False

    def on_back_button_press(self):
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'DashboardScreen'

    def logout(self):
        self.manager.current = 'MainScreen'


class ViewLoansScreenVLBB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        loan_amount = []
        interest_rate = []
        borrower_name = []
        date_of_apply = []
        status = []
        for i in data:
            # customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            borrower_name.append(i['borrower_name'])
            interest_rate.append(i['interest_rate'])
            # date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['status'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.user1.text = str(loan_id[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.borrower_name.text = str(borrower_name[index])
            self.ids.rate.text = str(interest_rate[index])
            # self.ids.date.text = str(date_of_apply[index])
            self.ids.updated_status.text = str(status[index])

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

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenVLB'


class ViewLoansScreenVLB(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        loan_amount = []
        interest_rate = []
        tenure = []
        date_of_apply = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            loan_amount.append(i['loan_amount'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            date_of_apply.append(i['borrower_loan_created_timestamp'])
            status.append(i['loan_updated_status'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.user1.text = str(loan_id[index])
            self.ids.amount.text = str(loan_amount[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.rate.text = str(interest_rate[index])
            self.ids.date.text = str(date_of_apply[index])
            self.ids.updated_status.text = str(status[index])

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

    def show_snackbar(self, text):
        Snackbar(text=text, pos_hint={'top': 1}, md_bg_color=[1, 0, 0, 1]).open()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

    def go_back(self):
        # Navigate to the previous screen with a slide transition
        self.manager.transition = SlideTransition(direction='right')
        self.manager.current = 'ViewLoansRequest'

    def on_back_button_press(self):
        self.manager.current = 'DashboardScreenVLB'


class OpenLoanVLB(Screen):
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
            disbursed = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(disbursed)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLB'
            self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(value, data)

        else:
            # Handle other loan statuses or show an error message
            pass

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
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')


class UnderProcessLoanVLB(Screen):

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
            if loan_status[c] == 'under process':
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
            item.bind(on_release=self.icon_button_clicked)
            self.ids.container1.add_widget(item)

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

        if loan_status == 'under process':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            under_process = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(under_process)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLB'
            self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(value, data)

        else:
            # Handle other loan statuses or show an error message
            pass

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
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')


class RejectedLoanVLB(Screen):
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
            if loan_status[c] == 'rejected':
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
            item.bind(on_release=self.icon_button_clicked)
            self.ids.container2.add_widget(item)

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

        if loan_status == 'rejected':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            rejected = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(rejected)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLB'
            self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(value, data)

        else:
            # Handle other loan statuses or show an error message
            pass

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
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')


class ClosedLoanVLB(Screen):
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
            if loan_status[c] == 'closed':
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
            self.ids.container3.add_widget(item)

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

        if loan_status == 'closed':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            disbursed = ViewLoansScreenVLB(name='ViewLoansScreenVLB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(disbursed)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLB'
            self.manager.get_screen('ViewLoansScreenVLB').initialize_with_value(value, data)

        else:
            # Handle other loan statuses or show an error message
            pass

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
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container3.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')


class ForeCloseLoanVLB(Screen):
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
            # customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            borrower_name.append(i['borrower_name'])
            loan_status.append(i['status'])

        c = -1
        index_list = []
        for i in range(s):
            c += 1
            if loan_status[c] == 'approved':
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
            self.ids.container4.add_widget(item)

    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()  # Fetch data here
        loan_status = None
        for loan in data:
            if loan['loan_id'] == value:
                loan_status = loan['status']
                break

        if loan_status == 'approved':
            # Open the screen for approved loans

            sm = self.manager

            # Create a new instance of the LoginScreen
            disbursed = ViewLoansScreenVLBB(name='ViewLoansScreenVLBB')

            # Add the LoginScreen to the existing ScreenManager
            sm.add_widget(disbursed)

            # Switch to the LoginScreen
            sm.current = 'ViewLoansScreenVLBB'
            self.manager.get_screen('ViewLoansScreenVLBB').initialize_with_value(value, data)

        else:
            # Handle other loan statuses or show an error message
            pass

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
        self.manager.current = 'DashboardScreenVLB'

    def refresh(self):
        self.ids.container4.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('foreclosure_data')


class MyScreenManager(ScreenManager):
    pass