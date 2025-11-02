from ._anvil_designer import ViewAllFormTemplate
from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables

class ViewAllForm(ViewAllFormTemplate):
  def __init__(self, **properties):
    """Runs when the 'View All Assignments' form loads"""
    self.init_components(**properties)

    # Load and display all assignments sorted by priority by default
    self.load_assignments(sort_by='priority')

  def load_assignments(self, sort_by='priority'):
    """Load all assignments from the database and display in repeating panel"""

    # Get all rows from the 'assignments' table
    assignments = list(app_tables.assignments.search())

    # Handle empty table gracefully
    if not assignments:
      alert("No assignments found. Add one from the home page.")
      return

    # Sort by priority or subject
    if sort_by == 'priority':
      # Define sorting order for priority levels
      priority_order = {'High': 1, 'Medium': 2, 'Low': 3}
      assignments.sort(key=lambda x: priority_order.get(x['priority'], 4))
    elif sort_by == 'subject':
      assignments.sort(key=lambda x: x['subject'] or '')

    # Display sorted assignments in the repeating panel
    self.repeating_panel_1.items = assignments

  def button_back_click(self, **event_args):
    """Go back to the main form (Form1)"""
    open_form('Form1')

  def button_sort_by_priority_click(self, **event_args):
    """Sort assignments by priority"""
    self.load_assignments(sort_by='priority')
    alert("📊 Sorted by Priority!")

  def button_sort_by_subject_click(self, **event_args):
    """Sort assignments by subject"""
    self.load_assignments(sort_by='subject')
    alert("📚 Sorted by Subject!")

 