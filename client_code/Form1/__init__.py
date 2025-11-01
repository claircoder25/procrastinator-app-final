
from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from datetime import datetime, timedelta
import random

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
      alert("⚠️ Please fill in all required fields!")
      return  # Stop the function here, don't add the assignment

    # Set defaults if dropdowns weren't selected
    if not priority:
      priority = "High"
    if not assignment_type:
      assignment_type = "Essay"

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
    self.drop_down_priority.selected_value = "High"
    self.drop_down_type.selected_value = "Essay"

    # FIXED: Random motivational messages
    messages = [
      "🎉 Assignment added! You've got this!",
      "✨ Great job staying organized!",
      "💪 One step closer to success!",
      "🌟 Assignment tracked! Now conquer it!",
      "🚀 Added! Time to show what you can do!",
      "📝 Logged! Let's crush this semester!",
      "🎯 Perfect! Stay ahead of the game!",
      "⭐ Brilliant! You're on top of things!"
    ]
    alert(random.choice(messages))

    # FIXED: Navigate to ViewAllForm after adding
    open_form('ViewAllForm')

  def button_view_all_click(self, **event_args):
    """Navigate to the View All form"""
    # Open the ViewAllForm by name
    # Make sure 'ViewAllForm' exactly matches the form name in your App Browser
    open_form('ViewAllForm')

  def button_due_soon_click(self, **event_args):
    """FIXED: Show assignments due in the next 3 days"""
    today = datetime.now().date()
    three_days_from_now = today + timedelta(days=3)

    # Get all incomplete assignments
    all_assignments = app_tables.assignments.search(completed=False)

    # Filter to only assignments due within 3 days
    due_soon = []
    for assignment in all_assignments:
      if assignment['due_date']:
        # Convert to date for comparison
        assignment_date = assignment['due_date'].date() if hasattr(assignment['due_date'], 'date') else assignment['due_date']
        if today <= assignment_date <= three_days_from_now:
          due_soon.append(assignment)

    # Display results
    if len(due_soon) == 0:
      alert("✅ Great news! No assignments due in the next 3 days!")
    else:
      # Build the message
      message = f"⏰ You have {len(due_soon)} assignment(s) due soon:\n\n"
      for assignment in due_soon:
        # Calculate days until due
        assignment_date = assignment['due_date'].date() if hasattr(assignment['due_date'], 'date') else assignment['due_date']
        days_until = (assignment_date - today).days

        if days_until == 0:
          time_str = "TODAY! 🔴"
        elif days_until == 1:
          time_str = "Tomorrow 🟡"
        else:
          time_str = f"In {days_until} days 🟢"

        message += f"• {assignment['name']} ({assignment['subject']})\n"
        message += f"  Due: {assignment['due_date'].strftime('%m/%d/%Y')} - {time_str}\n"
        message += f"  Priority: {assignment['priority']}\n\n"

      alert(message, title="Due Soon")

  def button_weekly_view_click(self, **event_args):
    """Navigate to Weekly view"""
    # Open the WeeklyViewForm by name
    # Only works if you've created a WeeklyViewForm
    try:
      open_form('WeeklyViewForm')
    except:
      # If WeeklyViewForm doesn't exist, show message
      alert("Weekly view coming soon! For now, use View All to see your assignments.")

  def button_stats_click(self, **event_args):
    """Calculate and display comprehensive statistics about assignments"""

    # Get all assignments
    all_assignments = list(app_tables.assignments.search())

    # Count total number of assignments (completed and incomplete)
    total = len(all_assignments)

    # Count how many assignments are completed
    completed = len([a for a in all_assignments if a['completed']])

    # Count how many assignments are still pending
    pending = len([a for a in all_assignments if not a['completed']])

    # Calculate completion rate as a percentage
    if total > 0:
      completion_rate = (completed / total) * 100
    else:
      completion_rate = 0

    #Count by priority
    high_priority = len([a for a in all_assignments if a['priority'] == 'High'])
    medium_priority = len([a for a in all_assignments if a['priority'] == 'Medium'])
    low_priority = len([a for a in all_assignments if a['priority'] == 'Low'])

    #Count by assignment type
    types_count = {}
    for assignment in all_assignments:
      atype = assignment['assignment_type']
      if atype:
        types_count[atype] = types_count.get(atype, 0) + 1

    #Calculate average time to complete assignments
    completed_assignments = [a for a in all_assignments if a['completed']]

    total_days = 0
    count = 0

    for assignment in completed_assignments:
      if assignment['date_created'] and assignment.get('date_completed'):
        days = (assignment['date_completed'] - assignment['date_created']).days
        total_days += days
        count += 1
    
    if count > 0:
      avg_days = total_days / count
    else:
      avg_days = 0
    
    # FIXED: Build comprehensive statistics message
    stats = f"""📊 Assignment Statistics:
    
Total Assignments: {total}
Completed: {completed}
Pending: {pending}
Completion Rate: {completion_rate:.1f}%

Priority Breakdown:
🔴 High: {high_priority}
🟡 Medium: {medium_priority}
🟢 Low: {low_priority}
"""
    
  def button_assignment_templates_click(self, **event_args):
    """Navigate to Assignment Type Templates"""
    open_form('AssignmentTypeTemplates')