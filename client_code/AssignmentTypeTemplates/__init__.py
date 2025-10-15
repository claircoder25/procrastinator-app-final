from ._anvil_designer import AssignmentTypeTemplatesTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class AssignmentTypeTemplates(AssignmentTypeTemplatesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    
    def button_back_click(self, **event_args):
      """Go back to the main form/home screen"""
    # Open Form1
    open_form('Form1')

    # Import the main form (Form1)
    from ..Form1 import Form1

    # Navigate back to Form1
    # This replaces the current screen with Form1
    open_form('Form1')
