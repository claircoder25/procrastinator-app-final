from ._anvil_designer import ViewAllFormTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime


class ViewAllForm(ViewAllFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Load all assignments when the form opens
    self.load_all_assignments()

  def load_all_assignments(self):
    """Load and display all pending assignments"""
    # Get all incomplete assignments from database
    assignments = app_tables.assignments.search(completed=False)

    # Sort by due date (earliest first)
    assignments = sorted(
      assignments, 
      key=lambda x: x['due_date'] if x['due_date'] else datetime.max.date()
    )

    # Display in the repeating panel
    self.repeating_panel_1.items = assignments

  def button_back_click(self, **event_args):
    """Go back to the main form"""
    # Import your main form
    from.Form1 import Form1

    # Navigate back to main form
    open_form('Form1')