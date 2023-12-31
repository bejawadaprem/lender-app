from ._anvil_designer import main_login_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class main_login_form(main_login_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
def login_sign_up_main_form_link_click(self, **event_args):
    anvil.users.login_with_form()
    current_user = anvil.users.get_user()
    if current_user:
      user_email = current_user['email']
      user_module.email = user_email
      email = user_email
      parts = email.split("@")
      if len(parts) == 2:
        split_name = parts[0]
        user_module.name =split_name
        
    check_user_already_exist = user_module.check_user_profile(current_user['email'])

    if check_user_already_exist:
      user_module.add_email_and_user_id(current_user['email'])
      open_form('bank_users.user_form')
    else:
      user_module.add_email_and_user_id(current_user)
      open_form('bank_users.user_form')
    



  
