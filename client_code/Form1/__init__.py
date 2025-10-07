# This imports all the necessary Anvil libraries
from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta

class Form1(Form1Template):
  def __init__(self, **properties):
    # This runs when the form first loads
    # It sets up the form and loads all assignments
    self.init_components(**properties)

    # Call the function to load assignments from the database
    self.load_assignments()

  def load_assignments(self):
    """This function loads all incomplete assignments from the database and displays them"""

    # Search the database for assignments that are NOT completed (completed=False)
    assignments = app_tables.assignments.search(completed=False)

    # Sort the assignments by due date (earliest first)
    # The 'key' tells Python what to sort by - in this case, the due_date
    # The 'if x['due_date'] else datetime.max.date()' handles assignments with no due date
    assignments = sorted(assignments, key=lambda x: x['due_date'] if x['due_date'] else datetime.max.date())

    # Put the assignments into the repeating panel so they show on screen
    self.repeating_panel_1.items = assignments

  def button_add_click(self, **event_args):
    """This runs when the user clicks the 'Add Assignment' button"""

    # Get the text/values from each input box
    name = self.text_box_name.text  # Assignment name (e.g., "Math Homework")
    subject = self.text_box_subject.text  # Subject (e.g., "Mathematics")
    due_date = self.date_picker_due.date  # The date it's due
    priority = self.drop_down_priority.selected_value  # High, Medium, or Low
    assignment_type = self.drop_down_type.selected_value  # Essay, Exam, etc.

    # CHECK: Make sure the user filled in all the important fields
    # If any field is empty, show an error message and stop
    if not name or not subject or not due_date:
      alert("Please fill in all required fields!")
      return  # Stop here - don't add the assignment

    # ADD TO DATABASE: Create a new row in the assignments table
    app_tables.assignments.add_row(
      name=name,  # Save the assignment name
      subject=subject,  # Save the subject
      due_date=due_date,  # Save when it's due
      priority=priority,  # Save priority level
      assignment_type=assignment_type,  # Save the type
      completed=False,  # New assignments are not completed yet
      date_created=datetime.now()  # Record when it was created (today)
    )

    # CLEAR THE FORM: Empty all the input boxes so user can add another
    self.text_box_name.text = ""
    self.text_box_subject.text = ""
    self.date_picker_due.date = None

    # REFRESH: Reload all assignments to show the new one
    self.load_assignments()

  def button_due_soon_click(self, **event_args):
    """This runs when user clicks 'Due Soon' - shows assignments due in next 3 days"""

    # Get today's date
    today = datetime.now().date()

    # Calculate the date 3 days from now
    three_days = today + timedelta(days=3)

    # SEARCH DATABASE: Find assignments that are:
    # 1. Not completed (completed=False)
    # 2. Due between today and 3 days from now
    due_soon = app_tables.assignments.search(
      completed=False,
      due_date=q.between(today, three_days)  # q.between finds dates in a range
    )

    # Sort them by due date (earliest first)
    due_soon = sorted(due_soon, key=lambda x: x['due_date'] if x['due_date'] else datetime.max.date())

    # Display only these assignments
    self.repeating_panel_1.items = due_soon

  def button_view_all_click(self, **event_args):
    """This runs when user clicks 'View All' - shows all pending assignments"""

    # Just reload all assignments (same as when app first opens)
    self.load_assignments()

  def button_weekly_view_click(self, **event_args):
    """This runs when user clicks 'This Week' - shows assignments due in next 7 days"""

    # Get today's date
    today = datetime.now().date()

    # Calculate the date 7 days from now (one week)
    week_end = today + timedelta(days=7)

    # SEARCH DATABASE: Find assignments due this week
    weekly = app_tables.assignments.search(
      completed=False,
      due_date=q.between(today, week_end)
    )

    # Sort by due date
    weekly = sorted(weekly, key=lambda x: x['due_date'] if x['due_date'] else datetime.max.date())

    # Display these assignments
    self.repeating_panel_1.items = weekly

  def button_stats_click(self, **event_args):
    """This runs when user clicks 'Statistics' - shows completion stats"""

    # COUNT: How many total assignments exist?
    total = len(app_tables.assignments.search())

    # COUNT: How many are completed?
    completed = len(app_tables.assignments.search(completed=True))

    # COUNT: How many are still pending?
    pending = len(app_tables.assignments.search(completed=False))

    # CALCULATE: What percentage are completed?
    if total > 0:  # Make sure we don't divide by zero
      completion_rate = (completed / total) * 100
    else:
      completion_rate = 0  # If no assignments, rate is 0%

    # CALCULATE AVERAGE TIME: How long does it take to complete assignments?
    # Get all completed assignments
    completed_assignments = app_tables.assignments.search(completed=True)
    total_days = 0  # Keep track of total days
    count = 0  # Keep track of how many we counted

    # Loop through each completed assignment
    for assignment in completed_assignments:
      # Check if it has both creation and completion dates
      if assignment['date_created'] and assignment['date_completed']:
        # Calculate how many days it took
        days = (assignment['date_completed'] - assignment['date_created']).days
        total_days += days  # Add to our total
        count += 1  # Count this assignment

    # Calculate the average (mean)
    if count > 0:  # Make sure we don't divide by zero
      avg_days = total_days / count
    else:
      avg_days = 0

    # SHOW STATISTICS: Display all the stats in a popup message
    alert(f"""Assignment Statistics:
    
Total Assignments: {total}
Completed: {completed}
Pending: {pending}
Completion Rate: {completion_rate:.1f}%
Average Time to Complete: {avg_days:.1f} days
""")

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def drop_down_type_change(self, **event_args):
    """This method is called when an item is selected"""
    pass
