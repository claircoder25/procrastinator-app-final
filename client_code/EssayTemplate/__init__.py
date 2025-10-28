from ._anvil_designer import EssayTemplateTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class EssayTemplate(EssayTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def button_back_click(self, **event_args):
    """Go back to templates page"""
  open_form('AssignmentTypeTemplates')

  def button_home_click(self, **event_args):
    """Go back to Form1 page"""
  open_form('Form1')
