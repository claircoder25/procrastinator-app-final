from ._anvil_designer import LiteratureReviewTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LiteratureReviewTemplate(LiteratureReviewTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

# button to go back to Assignment Template
  def button_back_click(self, **event_args):
    """Go back to templates page"""
    open_form('AssignmentTypeTemplates')
    
# button to go back to form1
  def button_home_click(self, **event_args):
    """Go back to the main form"""
    open_form('Form1')
