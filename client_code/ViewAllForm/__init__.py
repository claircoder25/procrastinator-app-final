from ._anvil_designer import ViewAllFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class ViewAllForm(ViewAllFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # FIXED: Load assignments when form opens
    self.load_assignments()

  def load_assignments(self, sort_by='priority'):
    """Load and display all assignments from database"""
    # Get all assignments from database
    assignments = list(app_tables.assignments.search())

    # Sort assignments based on the sort_by parameter
    if sort_by == 'priority':
      # Define priority order (High=1, Medium=2, Low=3)
      priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
      assignments.sort(key=lambda x: priority_order.get(x['priority'], 4))
    elif sort_by == 'subject':
      # Sort alphabetically by subject
      assignments.sort(key=lambda x: x['subject'] or '')

    # FIXED: Update the repeating panel with sorted assignments
    # Make sure your repeating panel is named 'repeating_panel_1'
    # If it has a different name, change it here
    self.repeating_panel_1.items = assignments

  def button_back_click(self, **event_args):
    """Navigate back to home page"""
    open_form('Form1')

  def button_sort_by_priority_click(self, **event_args):
    """Sort assignments by priority"""
    self.load_assignments(sort_by='priority')
    alert("📊 Sorted by Priority!")

  def button_sort_by_subject_click(self, **event_args):
    """Sort assignments by subject"""
    self.load_assignments(sort_by='subject')
    alert("📚 Sorted by Subject!")

 