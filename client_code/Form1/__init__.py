from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import random
from datetime import datetime, timedelta

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def add_assignment_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # Get values from inputs
    name = self.assignment_name_input.text
    subject = self.subject_input.text
    due_date = self.due_date_picker.date
    priority = self.priority_dropdown.selected_value
    assignment_type = self.assignment_type_dropdown.selected_value

    # Validation
    if not name or not subject or not due_date:
      alert("⚠️ Please fill in Assignment Name, Subject, and Due Date!")
      return

    if not priority:
      priority = "High"  # Default value

    if not assignment_type:
      assignment_type = "Essay"  # Default value

    try:
      # Add to database
      app_tables.assignments.add_row(
        name=name,
        subject=subject,
        due_date=due_date,
        priority=priority,
        assignment_type=assignment_type,
        completed=False,
        date_created=datetime.now()
      )

      # Random motivational messages
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

      # Clear the form
      self.assignment_name_input.text = ""
      self.subject_input.text = ""
      self.due_date_picker.date = None
      self.priority_dropdown.selected_value = "High"
      self.assignment_type_dropdown.selected_value = "Essay"

      # Navigate to ViewAllForm
      open_form('ViewAllForm')

    except Exception as e:
      alert(f"Error adding assignment: {str(e)}")

  def assignment_type_templates_button_click(self, **event_args):
    """This method is called when the Assignment Type Templates button is clicked"""
    open_form('AssignmentTypeTemplates')

  def due_soon_button_click(self, **event_args):
    """This method is called when the Due Soon button is clicked"""
    today = datetime.now().date()
    three_days_from_now = today + timedelta(days=3)

    # Query assignments due within 3 days that are not completed
    due_soon = app_tables.assignments.search(
      completed=False
    )

    # Filter by date (Anvil query operators)
    due_soon_filtered = [
      assignment for assignment in due_soon 
      if assignment['due_date'] and 
      today <= assignment['due_date'].date() <= three_days_from_now
    ]

    if len(due_soon_filtered) == 0:
      alert("✅ Great news! No assignments due in the next 3 days!")
    else:
      message = f"⏰ You have {len(due_soon_filtered)} assignment(s) due soon:\n\n"
      for assignment in due_soon_filtered:
        days_until = (assignment['due_date'].date() - today).days
        if days_until == 0:
          time_str = "Today!"
        elif days_until == 1:
          time_str = "Tomorrow"
        else:
          time_str = f"In {days_until} days"

        message += f"• {assignment['name']} ({assignment['subject']})\n"
        message += f"  Due: {assignment['due_date'].strftime('%m/%d/%Y')} - {time_str}\n"
        message += f"  Priority: {assignment['priority']}\n\n"
      alert(message)

  def statistics_button_click(self, **event_args):
    """Calculate and display statistics about assignments"""
    all_assignments = list(app_tables.assignments.search())
    completed = [a for a in all_assignments if a['completed']]
    incomplete = [a for a in all_assignments if not a['completed']]

    # Count by priority
    high_priority = [a for a in all_assignments if a['priority'] == 'High']
    medium_priority = [a for a in all_assignments if a['priority'] == 'Medium']
    low_priority = [a for a in all_assignments if a['priority'] == 'Low']

    # Count by type
    types_count = {}
    for assignment in all_assignments:
      atype = assignment['assignment_type']
      if atype:
        types_count[atype] = types_count.get(atype, 0) + 1

    # Calculate completion rate
    completion_rate = (len(completed) / len(all_assignments) * 100) if len(all_assignments) > 0 else 0

    # Build statistics message
    stats = f"""📊 Assignment Statistics:
    
    
Total Assignments: {len(all_assignments)}
Completed: {len(completed)}
Incomplete: {len(incomplete)}
Completion Rate: {completion_rate:.1f}%

Priority Breakdown:
🔴 High: {len(high_priority)}
🟡 Medium: {len(medium_priority)}
🟢 Low: {len(low_priority)}
"""

    if types_count:
      stats += "\nAssignment Types:\n"
      for atype, count in sorted(types_count.items()):
        stats += f"  • {atype}: {count}\n"

    alert(stats, title="Your Progress")

  def view_all_button_click(self, **event_args):
    """This method is called when the View All button is clicked"""
    open_form('ViewAllForm')