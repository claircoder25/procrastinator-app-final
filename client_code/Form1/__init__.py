from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime, timedelta
import random


class Form1(Form1Template):
  def __init__(self, **properties):
    # This runs when the form first loads
    # Sets Form properties and Data Bindings
    self.init_components(**properties)

  # When this button is clicked, all the information the uder added to the text boxes are added to the database table
  def button_add_click(self, **event_args):
    """This method is called when the Add Assignment button is clicked"""
 # Get user input from each component
    assignment_name = self.text_box_name.text
    assignment_subject = self.text_box_subject.text
    assignment_due_date = self.date_picker_due.date
    assignment_priority = self.drop_down_priority.selected_value
    assignment_type = self.drop_down_type.selected_value

    # Convert date (from DatePicker) to datetime at midnight
    if assignment_due_date:
      assignment_due_date = datetime.combine(assignment_due_date, datetime.min.time())

    # Validate required fields — name, subject, and due date must not be empty
    if not assignment_name or not assignment_subject or not assignment_due_date:
      alert("⚠️ Please fill in all required fields!")
      return

    # Set default dropdown values if nothing was selected
    assignment_priority = assignment_priority or "High"
    assignment_type = assignment_type or "Essay"
    
    # Add a new record to the 'assignments' table in Anvil Data Tables
    try:
      new_row = app_tables.assignments.add_row(
        name=assignment_name,
        subject=assignment_subject,
        due_date=assignment_due_date,
        priority=assignment_priority,
        assignment_type=assignment_type,
        completed=False,
        date_created=datetime.now()
      )

      print(f"✅ SUCCESS: Assignment saved! ID: {new_row.get_id()}")
      
      # Show an error message if the database save fails
    except Exception as e:
      alert(f"❌ Error saving assignment: {e}")
      return

    # Clear the form to prepare for a new entry
    self.text_box_name.text = ""
    self.text_box_subject.text = ""
    self.date_picker_due.date = None
    self.drop_down_priority.selected_value = "High"
    self.drop_down_type.selected_value = "Essay"

    # Random motivational messages to encourage the user
    messages = [
      "🎉 Assignment added! You've got this!",
      "✨ Great job staying organised!",
      "💪 One step closer to success!",
      "🌟 Assignment tracked! Now conquer it!",
      "🚀 Added! Time to show what you can do!"
    ]
    alert(random.choice(messages))


  # when these buttons are clicked, it will take the user to the respective form
  def button_view_all_click(self, **event_args):
    """Navigate to the View All page"""
    open_form('ViewAllForm')

  def button_templates_click(self, **event_args):
   """This method is called when the button is clicked"""
   open_form('AssignmentTypeTemplates')


  # when the button is clicked, it will show users assignments due in the next 1-3 days
  def button_due_soon_click(self, **event_args):
    """Show assignments due in the next 3 days"""
    today = datetime.now().date()
    three_days_from_now = today + timedelta(days=3)

    # Search for all assignments that are not yet completed
    all_assignments = app_tables.assignments.search(completed=False)
    due_soon = [
      a for a in all_assignments
      if a['due_date'] and today <= a['due_date'].date() <= three_days_from_now
    ]
    # Filter only assignments due within the next 3 days
    if not due_soon:
      alert("✅ Great news! No assignments due in the next 3 days!")
      return
      
    # Otherwise, build a message summarising due assignments
    message = f"⏰ You have {len(due_soon)} assignment(s) due soon:\n\n"
    for a in due_soon:
      days_until = (a['due_date'].date() - today).days
      if days_until == 0:
        time_str = "TODAY! 🔴"
      elif days_until == 1:
        time_str = "Tomorrow 🟡"
      else:
        time_str = f"In {days_until} days 🟢"

      message += f"• {a['name']} ({a['subject']})\n  Due: {a['due_date'].strftime('%d/%m/%Y')} - {time_str}\n  Priority: {a['priority']}\n\n"

    alert(message, title="Due Soon")


  # when the button is clicked a pop up message will appear and show basic statistics about assignments
  # show stats on priority levels, how many assignments are due and have been completed
  def button_stats_click(self, **event_args):
    """Calculate and display statistics about assignments"""
    all_assignments = list(app_tables.assignments.search())
    total = len(all_assignments)
    completed = len([a for a in all_assignments if a['completed']])
    pending = total - completed
    completion_rate = (completed / total * 100) if total > 0 else 0

    high_priority = len([a for a in all_assignments if a['priority'] == 'High'])
    medium_priority = len([a for a in all_assignments if a['priority'] == 'Medium'])
    low_priority = len([a for a in all_assignments if a['priority'] == 'Low'])

    types_count = {}
    for a in all_assignments:
      t = a['assignment_type']
      if t:
        types_count[t] = types_count.get(t, 0) + 1

    completed_assignments = [a for a in all_assignments if a['completed']]
    total_days = sum(
      (a['date_completed'] - a['date_created']).days
      for a in completed_assignments
      if a['date_completed'] and a['date_created']
    )
    avg_days = (total_days / len(completed_assignments)) if completed_assignments else 0

    stats = f"""📊 Assignment Statistics:
📚 Total: {total}
✅ Completed: {completed}
⏳ Pending: {pending}
📈 Completion Rate: {completion_rate:.1f}%

Priority:
🔴 High: {high_priority}
🟡 Medium: {medium_priority}
🟢 Low: {low_priority}
"""

    if types_count:
      stats += "\nAssignment Types:\n"
      for t, c in types_count.items():
        stats += f"  • {t}: {c}\n"

    if avg_days > 0:
      stats += f"\n⏱️ Average Time to Complete: {avg_days:.1f} days"

    alert(stats, title="Your Progress")

 

  