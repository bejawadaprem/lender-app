import anvil.server
from kivy.clock import Clock
from kivy.uix.modalview import ModalView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
import sqlite3
import anvil.server
from kivy.uix.screenmanager import Screen, SlideTransition
from kivymd.uix.list import *
from kivy.animation import Animation
from kivymd.uix.label import MDLabel
anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

view_loans = '''
<WindowManager>:
    ViewLoansScreen:
    ALlLoansScreen:
    OpenViewLoanScreen:
    ViewLoansProfileScreens:
    ViewLoansProfileScreens2:
    ViewApprovedLoansScreen:
    ViewRejectedLoansScreen:
    ViewUnderProcessLoansScreen:
    ViewClosedLoansScreen:
<ViewLoansScreen>
    MDTopAppBar:
        title: "View Loans"
        elevation: 3
        left_action_items: [['arrow-left', lambda x: root.on_back_button_press()]]
        pos_hint: {'top': 1}
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
            on_release: root.go_to_under_process_loans()
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
            on_release: root.go_to_rejected_loans()
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
            on_release: root.go_to_closed_loans()
            size_hint_y: None
            height: dp(60)
            size_hint_x: None
            width: dp(110)
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
            on_release: root.go_to_approved_loans()
            size_hint_y: None
            height: dp(60)
            size_hint_x: None
            width: dp(110)

            BoxLayout:
                orientation: 'horizontal'
                spacing:dp(10)
                MDLabel:
                    text: "Approved Loans"
                    font_size:dp(14)
                    bold:True
                    theme_text_color: 'Custom'
                    halign: "center"
                    text_color:1,1,1,1
        MDFlatButton:
            size_hint: None, None
            md_bg_color: 0.043, 0.145, 0.278, 1 

            size_hint_y: None
            height: dp(60)
            size_hint_x: None
            width: dp(110)
            on_release: root.all_loanscreen()
            BoxLayout:
                orientation: 'horizontal'
                spacing:dp(10)
                MDLabel:
                    text: "All Loans"
                    font_size:dp(14)
                    bold:True
                    theme_text_color: 'Custom'
                    halign: "center"
                    text_color:1,1,1,1

<OpenViewLoanScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Open Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
        
            MDList:
                id: container1

<ALlLoansScreen> 
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View All Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
        
            MDList:
                id: container2

<ViewApprovedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Approved Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
        
            MDList:
                id: container3

<ViewRejectedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Rejected Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
        
            MDList:
                id: container4

<ViewUnderProcessLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Under Process Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
        
            MDList:
                id: container5

<ViewClosedLoansScreen>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Closed Loans"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:
        
            MDList:
                id: container6
                
<ViewLoansProfileScreens>
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
                        text: "Borrower Full Loan details"
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
                        height: dp(650)

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
                                text: "User ID:" 
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
                                id: name
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
                                text: "Phone Number:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: number
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                
                            MDLabel:
                                text: "Credit Limit:" 
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
                            MDLabel:
                                text: "Loan Amount Applied:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount_applied
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
<ViewLoansProfileScreens2>
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
                        text: "Borrower Full Loan details"
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
                        height: dp(650)

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
                                text: "User ID:" 
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
                                id: name
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
                                text: "Phone Number:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: number
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                
                            MDLabel:
                                text: "Credit Limit:" 
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
                            MDLabel:
                                text: "Loan Amount Applied:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: amount_applied
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan ID:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: loan_id
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                            MDLabel:
                                text: "Loan Status:" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
                                bold: True
                            MDLabel:
                                id: status
                                text: "" 
                                size_hint_y:None
                                height:dp(50)
                                halign: "center"
    '''

Builder.load_string(view_loans)
conn = sqlite3.connect('fin_user_profile.db')
cursor = conn.cursor()


class ALlLoansScreen(Screen):
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
            self.ids.container2.add_widget(item)

    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens2(name='ViewLoansProfileScreens2')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens2'
        self.manager.get_screen('ViewLoansProfileScreens2').initialize_with_value(value, data)


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
        self.manager.current = 'ViewLoansScreen'


    def refresh(self):
        self.ids.container2.clear_widgets()
        self.__init__()


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

    def animate_loading_text(self, loading_label, modal_height):
        # Define the animation to move the label vertically
        anim = Animation(y=modal_height - loading_label.height, duration=1) + \
               Animation(y=0, duration=5)
        anim.bind(on_complete=lambda *args: self.animate_loading_text(loading_label,
                                                                      modal_height))  # Bind to the completion event to repeat the animation
        anim.start(loading_label)

    def all_loanscreen(self):
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
        Clock.schedule_once(lambda dt: self.performance_all_loanscreen(modal_view), 2)


    def performance_all_loanscreen(self,modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile_screen = ALlLoansScreen(name='ALlLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile_screen)

        # Switch to the LoginScreen
        sm.current = 'ALlLoansScreen'

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
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        open = OpenViewLoanScreen(name='OpenViewLoanScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(open)

        # Switch to the LoginScreen
        sm.current = 'OpenViewLoanScreen'

    def go_to_approved_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_approved_loans(modal_view), 2)

    def performance_go_to_approved_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        approved = ViewApprovedLoansScreen(name='ViewApprovedLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(approved)

        # Switch to the LoginScreen
        sm.current = 'ViewApprovedLoansScreen'



    def go_to_rejected_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_rejected_loans(modal_view), 2)


    def performance_go_to_rejected_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        rejected = ViewRejectedLoansScreen(name='ViewRejectedLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(rejected)

        # Switch to the LoginScreen
        sm.current = 'ViewRejectedLoansScreen'

    def go_to_under_process_loans(self):
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
        Clock.schedule_once(lambda dt: self.performance_go_to_under_process_loans(modal_view), 2)

    def performance_go_to_under_process_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        under_process = ViewUnderProcessLoansScreen(name='ViewUnderProcessLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(under_process)

        # Switch to the LoginScreen
        sm.current = 'ViewUnderProcessLoansScreen'

    def go_to_closed_loans(self):
        modal_view = ModalView(size_hint=(None, None), size=(150, 100), background_color=[0, 0, 0, 0])

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
        Clock.schedule_once(lambda dt: self.performance_go_to_closed_loans(modal_view), 2)


    def performance_go_to_closed_loans(self, modal_view):
        # self.manager.current = 'ViewProfileScreen'
        modal_view.dismiss()
        sm = self.manager

        # Create a new instance of the LoginScreen
        closed = ViewClosedLoansScreen(name='ViewClosedLoansScreen')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(closed)

        # Switch to the LoginScreen
        sm.current = 'ViewClosedLoansScreen'

class OpenViewLoanScreen(Screen):
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
            self.ids.container1.add_widget(item)


    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(value, data)

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
        self.manager.current = 'ViewLoansScreen'


    def refresh(self):
        self.ids.container1.clear_widgets()
        self.__init__()


    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

class ViewLoansProfileScreens(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        if self.ids.status.text == 'disbursed':
            self.manager.current = 'OpenViewLoanScreen'
        elif self.ids.status.text == 'approved':
            self.manager.current = 'ViewApprovedLoansScreen'
        elif self.ids.status.text == 'rejected':
            self.manager.current = 'ViewRejectedLoansScreen'
        elif self.ids.status.text == 'under process':
            self.manager.current = 'ViewUnderProcessLoansScreen'
        elif self.ids.status.text == 'closed':
            self.manager.current = 'ViewClosedLoansScreen'

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        member_rom = []
        member_since = []
        credit_limit = []
        beseem_score = []
        name = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            credit_limit.append(i['credit_limit'])
            name.append(i['borrower_full_name'])
            status.append(i['loan_updated_status'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.name.text = str(name[index])
            self.ids.status.text = str(status[index])

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
        if self.ids.status.text == 'disbursed':
            self.manager.current = 'OpenViewLoanScreen'
        elif self.ids.status.text == 'approved':
            self.manager.current = 'ViewApprovedLoansScreen'
        elif self.ids.status.text == 'rejected':
            self.manager.current = 'ViewRejectedLoansScreen'
        elif self.ids.status.text == 'under process':
            self.manager.current = 'ViewUnderProcessLoansScreen'
        elif self.ids.status.text == 'closed':
            self.manager.current = 'ViewClosedLoansScreen'

class ViewLoansProfileScreens2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_back_button_press(self):
        self.manager.current = 'ALlLoansScreen'

    def initialize_with_value(self, value, data):
        customer_id = []
        loan_id = []
        tenure = []
        interest_rate = []
        loan_amount = []
        member_rom = []
        member_since = []
        credit_limit = []
        beseem_score = []
        name = []
        status = []
        for i in data:
            customer_id.append(i['borrower_customer_id'])
            loan_id.append(i['loan_id'])
            tenure.append(i['tenure'])
            interest_rate.append(i['interest_rate'])
            loan_amount.append(i['loan_amount'])
            credit_limit.append(i['credit_limit'])
            name.append(i['borrower_full_name'])
            status.append(i['loan_updated_status'])

        if value in loan_id:
            index = loan_id.index(value)
            self.ids.loan_id.text = str(loan_id[index])
            self.ids.user1.text = str(customer_id[index])
            self.ids.interest.text = str(interest_rate[index])
            self.ids.tenure.text = str(tenure[index])
            self.ids.amount_applied.text = str(loan_amount[index])
            self.ids.limit.text = str(credit_limit[index])
            self.ids.name.text = str(name[index])
            self.ids.status.text = str(status[index])

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

        self.manager.current = 'ALlLoansScreen'
class ViewApprovedLoansScreen(Screen):
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
            self.ids.container3.add_widget(item)


    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(value, data)

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
        self.manager.current = 'ViewLoansScreen'


    def refresh(self):
        self.ids.container3.clear_widgets()
        self.__init__()


    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

class ViewRejectedLoansScreen(Screen):
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
            item.bind(on_release=self.icon_button_clicked)  # Corrected the binding
            self.ids.container4.add_widget(item)

    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(value, data)

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
        self.manager.current = 'ViewLoansScreen'

    def refresh(self):
        self.ids.container4.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

class ViewUnderProcessLoansScreen(Screen):
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
            item.bind(on_release=self.icon_button_clicked)  # Corrected the binding
            self.ids.container5.add_widget(item)

    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(value, data)

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
        self.manager.current = 'ViewLoansScreen'

    def refresh(self):
        self.ids.container5.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')

class ViewClosedLoansScreen(Screen):
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
            self.ids.container6.add_widget(item)

    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:]
        data = self.get_table_data()
        sm = self.manager

        # Create a new instance of the LoginScreen
        profile = ViewLoansProfileScreens(name='ViewLoansProfileScreens')

        # Add the LoginScreen to the existing ScreenManager
        sm.add_widget(profile)

        # Switch to the LoginScreen
        sm.current = 'ViewLoansProfileScreens'
        self.manager.get_screen('ViewLoansProfileScreens').initialize_with_value(value, data)

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
        self.manager.current = 'ViewLoansScreen'

    def refresh(self):
        self.ids.container6.clear_widgets()
        self.__init__()

    def get_table_data(self):
        # Make a call to the Anvil server function
        # Replace 'YourAnvilFunction' with the actual name of your Anvil server function
        return anvil.server.call('get_table_data')
class MyScreenManager(ScreenManager):
    pass
