from ._anvil_designer import ViewAllFormTemplate
from anvil import *
from anvil.tables import app_tables
from datetime import datetime

class ViewAllForm(ViewAllFormTemplate):
  def __init__(self, **properties):
    # Initialise the form
    self.init_components(**properties)

    # Load all assignments when form opens
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
    self.repeating_panel_2.items = assignments

  def button_back_click(self, **event_args):
    """Go back to the main form"""
    open_form('Form1')

  def button_refresh_click(self, **event_args):
    """Reload assignments (useful after completing some)"""
    self.load_all_assignments()