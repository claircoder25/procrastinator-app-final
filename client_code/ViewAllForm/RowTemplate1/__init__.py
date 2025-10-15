from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Initialize components first
    self.init_components(**properties)

    # Only run color/time functions if we have the required components
    try:
      self.set_priority_color()
    except Exception as e:
      print(f"Color setting error: {e}")

    try:
      self.calculate_time_remaining()
    except Exception as e:
      print(f"Time calculation error: {e}")

  def set_priority_color(self):
    """Set card background color based on priority"""
    priority = self.item['priority']

    if priority == "High":
      self.card_1.background = "#ffcccc"  # Light red
    elif priority == "Medium":
      self.card_1.background = "#fff9cc"  # Light yellow
    else:  # Low
      self.card_1.background = "#ccffcc"  # Light green

  def calculate_time_remaining(self):
    """Calculate and display days until due"""
    due_date = self.item['due_date']
    today = datetime.now().date()

    if due_date:
      days_remaining = (due_date - today).days

      if days_remaining < 0:
        self.label_time_remaining.text = f"OVERDUE by {abs(days_remaining)} days!"
        self.label_time_remaining.foreground = "red"
        self.label_time_remaining.bold = True
      elif days_remaining == 0:
        self.label_time_remaining.text = "Due TODAY!"
        self.label_time_remaining.foreground = "orange"
        self.label_time_remaining.bold = True
      elif days_remaining == 1:
        self.label_time_remaining.text = "Due tomorrow"
        self.label_time_remaining.foreground = "orange"
      else:
        self.label_time_remaining.text = f"{days_remaining} days remaining"
    else:
      self.label_time_remaining.text = "No due date"

  def button_complete_click(self, **event_args):
    """Mark assignment complete"""
    self.item['completed'] = True
    self.item['date_completed'] = datetime.now()

    import random
    messages = [
      "Great job!",
      "Awesome work!",
      "Well done!",
      "Excellent!",
      "You're crushing it! 🏆"
    ]
    alert(random.choice(messages))
    self.remove_from_parent()

  def button_delete_click(self, **event_args):
    """Delete assignment"""
    if confirm("Delete this assignment?"):
      self.item.delete()
      self.remove_from_parent()

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass
