from ._anvil_designer import AssignmentTypeTemplatesTemplate
from anvil import *

class AssignmentTypeTemplates(AssignmentTypeTemplatesTemplate):
  def __init__(self, **properties):
    self.init_components(**properties)

  # Button to home page
  def button_back_click(self, **event_args):
    """Go back to main form"""
    open_form('Form1')
    
# Click button to go to Essay template
  def button_essay_click(self, **event_args):
    """Open Essay Template form"""
    open_form('EssayTemplate')

  def button_report_click(self, **event_args):
    """Open Report Template form"""
    open_form('ReportTemplate')

  def button_exam_guide_click(self, **event_args):
    """Open Exam Guide form"""
    open_form('ExamGuideTemplate')

  def button_literature_review_click(self, **event_args):
    """Open Literature Review Template form"""
    open_form('LiteratureReviewTemplate')



