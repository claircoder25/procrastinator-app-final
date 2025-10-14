from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta

class Form1(Form1Template):
  def __init__(self, **properties):
    # This runs when the form first loads
    self.init_components(**properties)

  def button_add_click(self, **event_args):
    """This runs when the 'Add Assignment' button is clicked"""

    # Get the values that the user typed into each input field
    name = self.text_box_name.text
    subject = self.text_box_subject.text
    due_date = self.date_picker_due.date
    priority = self.drop_down_priority.selected_value
    assignment_type = self.drop_down_type.selected_value

    # Validate inputs - make sure user filled in the required fields
    if not name or not subject or not due_date:
      alert("Please fill in all required fields!")
      return

    # Add a new row to the 'assignments' table in the database
    app_tables.assignments.add_row(
      name=name,
      subject=subject,
      due_date=due_date,
      priority=priority,
      assignment_type=assignment_type,
      completed=False,
      date_created=datetime.now()
    )

    # Clear the input fields
    self.text_box_name.text = ""
    self.text_box_subject.text = ""
    self.date_picker_due.date = None

    # Show success message
    alert("Assignment added successfully!")

  def button_view_all_click(self, **event_args):
    """Navigate to the View All form"""
    # Open the ViewAllForm by name
    # Make sure 'ViewAllForm' exactly matches the form name in your App Browser
    open_form('ViewAllForm')

  def button_due_soon_click(self, **event_args):
    """Navigate to Due Soon view"""
    # Open the DueSoonForm by name
    # Only use this if you've created a DueSoonForm
    open_form('DueSoonForm')

  def button_weekly_view_click(self, **event_args):
    """Navigate to Weekly view"""
    # Open the WeeklyViewForm by name
    # Only use this if you've created a WeeklyViewForm
    open_form('WeeklyViewForm')

  def button_stats_click(self, **event_args):
    """Calculate and display statistics about assignments"""

    # Count total number of assignments
    total = len(app_tables.assignments.search())
    completed = len(app_tables.assignments.search(completed=True))
    pending = len(app_tables.assignments.search(completed=False))

    # Calculate completion rate
    if total > 0:
      completion_rate = (completed / total) * 100
    else:
      completion_rate = 0

    # Calculate average time to complete
    completed_assignments = app_tables.assignments.search(completed=True)
    total_days = 0
    count = 0

    for assignment in completed_assignments:
      if assignment['date_created'] and assignment['date_completed']:
        days = (assignment['date_completed'] - assignment['date_created']).days
        total_days += days
        count += 1

    avg_days = total_days / count if count > 0 else 0

    # Show all statistics in a popup message
    alert(f"""Assignment Statistics:
    
Total Assignments: {total}
Completed: {completed}
Pending: {pending}
Completion Rate: {completion_rate:.1f}%
Average Time to Complete: {avg_days:.1f} days
""")
