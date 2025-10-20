from ._anvil_designer import AssignmentTypeTemplatesTemplate
from anvil import *
from anvil.tables import app_tables
from datetime import datetime

class AssignmentTypeTemplates(AssignmentTypeTemplatesTemplate):
  def __init__(self, **properties):
    # Initialize the form
    self.init_components(**properties)

  def button_back_click(self, **event_args):
    """Navigate back to main form"""
    open_form('Form1')

