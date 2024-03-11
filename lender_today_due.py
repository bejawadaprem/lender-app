from datetime import datetime, timezone
from bson import utc
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, SlideTransition, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.list import ThreeLineAvatarIconListItem, IconLeftWidget
import anvil.server

anvil.server.connect("server_VRGEXX5AO24374UMBBQ24XN6-ZAWBX57M6ZDN6TBV")

lender_today_due = '''

<WindowManager>:
    TodayDuesTD:
    ViewProfileTD:

<TodayDuesTD>
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "Today's Dues"
            elevation: 3
            left_action_items: [['arrow-left', lambda x: root.go_back()]]
            right_action_items: [['refresh', lambda x: root.refresh()]]
            md_bg_color: 0.043, 0.145, 0.278, 1
        MDScrollView:

            MDList:
                id: container
<ViewProfileTD>:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar:
            title: "View Details"
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
                        text: " Today Dues Details"
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
                        height: dp(950)
                        padding: [10, 0, 0, 0]
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
                                text: "Loan ID" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loan_id
                                text: "" 
                            MDLabel:
                                text: "Loan Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: loan_amount
                                text: "" 

                            MDLabel:
                                text: "Loan Tenure" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: tenure
                                text: "" 
                            MDLabel:
                                text: "Interest Rate" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: interest
                                text: "" 
                            MDLabel:
                                text: "Account Number" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: number
                                text: "" 
                            MDLabel:
                                text: "Emi Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: emi_amount
                                text: "" 
                            MDLabel:
                                text: "Extra Amount" 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: extra_amount
                                text: "" 
                            MDLabel:
                                text: "Total Emi Amount " 
                                size_hint_y:None
                                height:dp(50)
                            MDLabel:
                                id: total_emi_amount
                                text: "" 
                            MDRaisedButton:
                                text: "PayNow"
                                md_bg_color: 194/255, 2/255, 21/255, 1
                                theme_text_color: 'Primary'
                                on_release: app.root.current = 'LoansDetails'
                                text_color: 0, 0, 0, 1
                                font_name: "Roboto-Bold.ttf"
                                size_hint: 1, None

'''
Builder.load_string(lender_today_due)
date = datetime.today().date()
print(date)


class TodayDuesTD(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        data = self.get_table_data()
        loan_id = []
        schedule_payment = []
        scheduled_payment_date_list = []  # Assuming this is a list of datetime objects
        s = 0

        for i in data:
            s += 1
            loan_id.append(i['loan_id'])
            print(loan_id)
            schedule_payment.append(i['scheduled_payment'])
            print(schedule_payment)
            scheduled_payment_date_list.append(i['scheduled_payment_made'])

        c = -1
        index_list = []

        for i in range(s):
            c += 1

            if schedule_payment[i] == date:
                index_list.append(c)

        b = 1
        k = -1

        for i in index_list:
            b += 1
            k += 1
            today_date = datetime.combine(date.today(), datetime.min.time()).replace(tzinfo=utc)

            # Access the specific date corresponding to the current iteration
            current_scheduled_payment_date = scheduled_payment_date_list[i]

            # Make sure current_scheduled_payment_date is offset-aware (e.g., using pytz)
            current_scheduled_payment_date = current_scheduled_payment_date.replace(tzinfo=utc)

            # Calculate the difference in days
            days_until_payment = (current_scheduled_payment_date - today_date).days

            print(f"Today's date: {today_date}")
            print(f"Scheduled payment date: {current_scheduled_payment_date}")
            print(f"Days until scheduled payment date: {days_until_payment} days")

            item = ThreeLineAvatarIconListItem(
                IconLeftWidget(
                    icon="card-account-details-outline"
                ),
                text=f"Loan ID : {loan_id[i]}",
                secondary_text=f"Schedule Payment: {schedule_payment[i]}",
                tertiary_text=f"Day Passed Due Date: {days_until_payment}",
            )
            item.bind(on_release=self.icon_button_clicked)
            self.ids.container.add_widget(item)

    def icon_button_clicked(self, instance):
        # Handle the on_release event here
        value = instance.text.split(':')
        value = value[-1][1:].strip()
        data = self.get_table_data()
        schedule_payment = None
        for loan in data:
            if loan['loan_id'] == value:
                schedule_payment = loan['scheduled_payment']
                print(schedule_payment)
                break

    def get_table_data(self):

        return anvil.server.call('get_today_data')

    def on_pre_enter(self):
        # Bind the back button event to the on_back_button method
        Window.bind(on_keyboard=self.on_back_button)

    def on_pre_leave(self):
        # Unbind the back button event when leaving the screen
        Window.unbind(on_keyboard=self.on_back_button)

    def on_back_button(self, instance, key, scancode, codepoint, modifier):

        if key == 27:
            self.go_back()
            return True
        return False

    def refresh(self):
        self.ids.container.clear_widgets()
        self.__init__()

    def go_back(self):
        self.manager.current = 'LenderDashboard'

class ViewProfileTD(Screen):
    pass


class MyScreenManager(ScreenManager):
    pass