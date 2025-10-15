from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta

class Form1(Form1Template):
  def __init__(self, **properties):
    # This runs when the form first loads
    # Initialize all components
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
    # 'not name' means "if name is empty"
    if not name or not subject or not due_date:
      # Show an error message popup if any required field is empty
      alert("Please fill in all required fields!")
      return  # Stop the function here, don't add the assignment

    # Add a new row to the 'assignments' table in the database
    # This saves the assignment permanently
    app_tables.assignments.add_row(
      name=name,                      # Assignment name
      subject=subject,                # Subject/class
      due_date=due_date,             # When it's due
      priority=priority,             # High, Medium, or Low
      assignment_type=assignment_type, # Essay, Exam, Project, etc.
      completed=False,               # New assignments start as incomplete
      date_created=datetime.now()    # Record when assignment was added
    )

    # Clear the input fields so user can add another assignment
    self.text_box_name.text = ""
    self.text_box_subject.text = ""
    self.date_picker_due.date = None

    # Show success message
    alert("Assignment added successfully! 🎉")

  def button_view_all_click(self, **event_args):
    """Navigate to the View All form"""
    # Open the ViewAllForm by name
    # Make sure 'ViewAllForm' exactly matches the form name in your App Browser
    open_form('ViewAllForm')

  def button_due_soon_click(self, **event_args):
    """Navigate to Due Soon view"""
    # Open the DueSoonForm by name
    # Only works if you've created a DueSoonForm
    # If you haven't created this form yet, you can comment out this function
    # or create the form
    try:
      open_form('DueSoonForm')
    finally:
      # If DueSoonForm doesn't exist, show message
      alert("Due Soon view coming soon! For now, use View All to see your assignments.")

  def button_weekly_view_click(self, **event_args):
    """Navigate to Weekly view"""
    # Open the WeeklyViewForm by name
    # Only works if you've created a WeeklyViewForm
    try:
      open_form('WeeklyViewForm')
    finally:
      # If WeeklyViewForm doesn't exist, show message
      alert("Weekly view coming soon! For now, use View All to see your assignments.")

  def button_stats_click(self, **event_args):
    """Calculate and display statistics about assignments"""

    # Count total number of assignments (completed and incomplete)
    # len() counts how many items are in the search results
    total = len(app_tables.assignments.search())

    # Count how many assignments are completed
    completed = len(app_tables.assignments.search(completed=True))

    # Count how many assignments are still pending
    pending = len(app_tables.assignments.search(completed=False))

    # Calculate completion rate as a percentage
    if total > 0:
      # Divide completed by total, multiply by 100 to get percentage
      completion_rate = (completed / total) * 100
    else:
      # If there are no assignments yet, completion rate is 0%
      completion_rate = 0

    # Calculate average time to complete assignments
    # Get all completed assignments
    completed_assignments = app_tables.assignments.search(completed=True)

    total_days = 0  # Keep track of total days across all completed assignments
    count = 0       # Count how many assignments had valid dates

    # Loop through each completed assignment
    for assignment in completed_assignments:
      # Make sure both dates exist (some might be missing)
      if assignment['date_created'] and assignment['date_completed']:
        # Calculate how many days between creation and completion
        days = (assignment['date_completed'] - assignment['date_created']).days
        total_days += days  # Add to running total
        count += 1          # Count this assignment

    # Calculate average (only if we have valid data)
    if count > 0:
      avg_days = total_days / count  # Divide total days by number of assignments
    else:
      avg_days = 0  # No data yet

    # Show all statistics in a popup message
    # The f-string allows us to insert variables into the text
    # {variable:.1f} formats numbers to 1 decimal place
    alert(f"""📊 Assignment Statistics:
    
Total Assignments: {total}
Completed: {completed} ✅
Pending: {pending} 📝
Completion Rate: {completion_rate:.1f}%
Average Time to Complete: {avg_days:.1f} days

Keep up the great work! 🌟
""")

  def features_menu_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass

  def button_templates_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  
def button_templates_click(self, **event_args):
    """Navigate to AssignmentTypeTemplates form"""
    open_form('AssignmentTypeTemplates')