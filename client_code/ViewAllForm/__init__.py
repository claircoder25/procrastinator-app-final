from ._anvil_designer import ViewAllFormTemplate
from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime

class ViewAllForm(ViewAllFormTemplate):
  def __init__(self, **properties):
    # This runs when the form opens
    self.init_components(**properties)

    # Automatically load all assignments when form opens
    self.load_all_assignments()

  def load_all_assignments(self):
    """Load and display all pending assignments"""

    # Search the database for all incomplete assignments
    assignments = app_tables.assignments.search(completed=False)

    # Sort assignments by due date (earliest first)
    # If an assignment has no due date, put it at the end
    assignments = sorted(
      assignments, 
      key=lambda x: x['due_date'] if x['due_date'] else datetime.max.date()
    )

    # Display the assignments in the repeating panel
    # The repeating panel uses the row template to show each assignment
    self.repeating_panel_2.items = assignments

    # Update the count label (if you have one)
    # This shows "Showing 5 assignments" at the top
    self.label_count.text = f"Showing {len(assignments)} pending assignments"

  def button_back_click(self, **event_args):
    """Go back to the main form/home screen"""

    # Import the main form (Form1)
    from .Form1 import Form1

    # Navigate back to Form1
    # This replaces the current screen with Form1
    open_form('Form1')

  def button_refresh_click(self, **event_args):
    """Reload the assignments (useful after completing some)"""

    # Simply call load_all_assignments again
    # This will update the display with current database data
    self.load_all_assignments()

  def button_sort_by_priority_click(self, **event_args):
    """Sort assignments by priority instead of due date"""

    # Get all incomplete assignments
    assignments = app_tables.assignments.search(completed=False)

    # Define priority order (High > Medium > Low)
    priority_order = {"High": 1, "Medium": 2, "Low": 3}

    # Sort by priority level
    assignments = sorted(
      assignments,
      key=lambda x: priority_order.get(x['priority'], 4)
    )

    # Update the display
    self.repeating_panel_2.items = assignments
    self.label_count.text = f"Showing {len(assignments)} assignments (sorted by priority)"

  def button_sort_by_subject_click(self, **event_args):
    """Sort assignments by subject alphabetically"""

    # Get all incomplete assignments
    assignments = app_tables.assignments.search(completed=False)

    # Sort alphabetically by subject name
    assignments = sorted(
      assignments,
      key=lambda x: x['subject'] if x['subject'] else ""
    )

    # Update the display
    self.repeating_panel_2.items = assignments
    self.label_count.text = f"Showing {len(assignments)} assignments (sorted by subject)"
  