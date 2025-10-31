from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import datetime

class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # This runs when each row is created in the repeating panel
    # Each row represents one assignment

    # Set Form properties and Data Bindings
    self.init_components(**properties)

    # Set the background colour based on the assignment's priority level
    # Wrap in try/except to handle any missing components gracefully
    try:
      self.set_priority_color()
    except Exception as e:
      print(f"Error setting priority color: {e}")

    # Calculate how much time is left and display it
    try:
      self.calculate_time_remaining()
    except Exception as e:
      print(f"Error calculating time remaining: {e}")

  def set_priority_color(self):
    """Set the background color of the card based on priority level"""

    # Get the priority value from this assignment's data
    # self.item contains all the data for this specific assignment
    priority = self.item['priority']

    # Change the card's background color based on priority
    if priority == "High":
      # High priority = light red background (urgent!)
      self.card_1.background = "#ffcccc"

    elif priority == "Medium":
      # Medium priority = light yellow background
      self.card_1.background = "#fff9cc"

    else:  # Low priority
      # Low priority = light green background (less urgent)
      self.card_1.background = "#ccffcc"

  def calculate_time_remaining(self):
    """Calculate how many days until the assignment is due and display it"""

    # Get the due date for this assignment
    due_date = self.item['due_date']

    # Get today's date (without the time)
    today = datetime.now().date()

    # Only calculate if there is a due date set
    if due_date:
      # Calculate the difference in days
      # Subtracting dates gives us a timedelta, .days converts to number of days
      days_remaining = (due_date - today).days

      # Check if assignment is overdue (negative days)
      if days_remaining < 0:
        # If overdue, show how many days past due
        # abs() makes the number positive so we can say "overdue by X days"
        self.label_time_remaining.text = f"⚠️ OVERDUE by {abs(days_remaining)} days!"
        self.label_time_remaining.foreground = "red"     # Make text red (danger!)
        self.label_time_remaining.bold = True            # Make text bold to stand out

      # Check if assignment is due today
      elif days_remaining == 0:
        self.label_time_remaining.text = "🔥 Due TODAY!"
        self.label_time_remaining.foreground = "orange"  # Orange = urgent warning
        self.label_time_remaining.bold = True

      # Check if assignment is due tomorrow
      elif days_remaining == 1:
        self.label_time_remaining.text = "⏰ Due tomorrow"
        self.label_time_remaining.foreground = "orange"  # Still urgent

      # Assignment is due 2+ days in the future
      else:
        # Show the number of days remaining
        self.label_time_remaining.text = f"📅 {days_remaining} days remaining"
        # Default color (black) - no special formatting needed
    else:
      # If no due date is set
      self.label_time_remaining.text = "No due date set"

  def button_complete_click(self, **event_args):
    """This runs when the 'Complete' button is clicked"""

    # Mark this assignment as completed in the database
    # self.item refers to this specific assignment's row in the database
    self.item['completed'] = True

    # Record when the assignment was completed
    self.item['date_completed'] = datetime.now()

    # Show a motivational message to encourage the student
    # List of different positive messages
    messages = [
      "Great job! Keep up the good work! 🎉",
      "Awesome! You're making progress! 💪",
      "Well done! One step closer to your goals! ⭐",
      "Excellent work! Stay motivated! 🚀",
      "Amazing! You're crushing it! 🏆",
      "Fantastic! Keep the momentum going! 🌟",
      "Outstanding work! You got this! 💯",
      "Brilliant! You're on fire! 🔥"
    ]

    # Import the random module to pick a random message
    import random
    # Pick one message randomly from the list and show it
    alert(random.choice(messages))

    # Remove this assignment from the display
    # Since it's complete, we don't need to see it anymore
    self.remove_from_parent()

  def button_delete_click(self, **event_args):
    """This runs when the 'Delete' button is clicked"""

    # Ask the user to confirm they want to delete
    # confirm() shows a popup with Yes/No buttons and returns True if they click Yes
    if confirm("Are you sure you want to delete this assignment? This cannot be undone."):
      # Delete this assignment from the database permanently
      self.item.delete()

      # Remove this assignment from the display
      self.remove_from_parent()

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def create_new_click(self, **event_args):
    """This method is called when the link is clicked"""
    pass
