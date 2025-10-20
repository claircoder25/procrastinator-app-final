from ._anvil_designer import AssignmentTypeTemplatesTemplate
from anvil import *
from anvil.tables import app_tables
from datetime import datetime

class AssignmentTypeTemplates(AssignmentTypeTemplatesTemplate):
  def __init__(self, **properties):
    # Initialise the form
    self.init_components(**properties)

  def button_back_click(self, **event_args):
    """Navigate back to main form"""
    open_form('Form1')

def button_essay_click(self, **event_args):
  """Show essay writing template and tips"""
  essay_template = """
📝 ESSAY WRITING TEMPLATE

INTRODUCTION (1 paragraph)
• Hook: Start with an interesting fact, quote, or question
• Background: Provide context about your topic
• Thesis Statement: Your main argument (usually last sentence)

BODY PARAGRAPHS (3-5 paragraphs)
Each paragraph should have:
• Topic Sentence: Main point of the paragraph
• Evidence: Facts, quotes, or examples supporting your point
• Analysis: Explain how evidence supports your thesis
• Transition: Connect to the next paragraph

CONCLUSION (1 paragraph)
• Restate thesis (in different words)
• Summarize main points
• Final thought: Why does this matter? What's next?

TIPS:
✓ Write your thesis first
✓ Use transition words (However, Therefore, Furthermore)
✓ Cite your sources properly
✓ Proofread multiple times
✓ Read it aloud to catch errors
    """
  alert(essay_template, large=True, title="Essay Template")

  # ==================== RESEARCH REPORT TEMPLATE ====================
  def button_report_click(self, **event_args):
    """Show research report template"""
    report_template = """
📊 RESEARCH REPORT TEMPLATE

TITLE PAGE
• Title of your report
• Your name
• Date
• Class/Subject

ABSTRACT (Optional for school reports)
• Brief summary of your entire report (150-250 words)

TABLE OF CONTENTS
• List all sections with page numbers

INTRODUCTION
• What is your topic?
• Why is it important?
• What questions will you answer?
• Overview of what's in the report

LITERATURE REVIEW / BACKGROUND
• What have others said about this topic?
• Summarize key research and findings
• Identify gaps in knowledge

METHODOLOGY (if applicable)
• How did you conduct your research?
• What sources did you use?

FINDINGS / RESULTS
• What did you discover?
• Present data, facts, and information
• Use headings and subheadings

DISCUSSION / ANALYSIS
• What do your findings mean?
• How do they answer your questions?
• Limitations of your research

CONCLUSION
• Summary of key findings
• Implications
• Suggestions for future research

REFERENCES / BIBLIOGRAPHY
• List all sources in proper format

TIPS:
✓ Use headings and subheadings
✓ Include charts, graphs, or images
✓ Keep formal, academic tone
✓ Cite sources throughout
    """
    alert(report_template, large=True, title="Research Report Template")

# ==================== EXAM STUDY GUIDE CREATOR ====================
def button_exam_guide_click(self, **event_args):
  """Show exam preparation guide"""
  exam_guide = """
📚 EXAM PREPARATION GUIDE

STUDY SCHEDULE TEMPLATE:
□ 2 weeks before: Review all notes, identify weak areas
□ 10 days before: Create summary sheets for each topic
□ 1 week before: Practice problems/questions
□ 3 days before: Review summaries, take practice tests
□ 1 day before: Light review, get good sleep
□ Exam day: Eat well, arrive early, stay calm

STUDY TECHNIQUES:
✓ Active Recall: Test yourself without looking at notes
✓ Spaced Repetition: Review material multiple times over days
✓ Pomodoro Technique: Study 25 min, break 5 min
✓ Teach Someone: Explain concepts to a friend or family member
✓ Practice Problems: Do as many as possible
✓ Mind Maps: Create visual connections between concepts

NOTES ORGANIZATION:
• Use Cornell Method (notes, cues, summary)
• Colour-code by topic
• Highlight key terms and definitions
• Create flashcards for memorisation
• Summarise each page in one sentence

EXAM DAY TIPS:
✓ Read all instructions carefully
✓ Budget your time (divide by number of questions)
✓ Answer easy questions first
✓ Show your work (partial credit!)
✓ Check your answers if time allows
✓ Stay calm - you've prepared!

STRESS MANAGEMENT:
• Get 7-9 hours of sleep
• Eat nutritious meals
• Exercise or take walks
• Take breaks during study sessions
• Practice deep breathing
• Talk to someone if you're overwhelmed
    """
  alert(exam_guide, large=True, title="Exam Preparation Guide")

  # ==================== LITERATURE REVIEW TEMPLATE ====================
  def button_literature_review_click(self, **event_args):
    """Show literature review template"""
    literature_review_template = """
📚 LITERATURE REVIEW TEMPLATE

INTRODUCTION
• Define your research topic or question
• Explain the scope of your review
• State your thesis or perspective
• Outline the structure of your review

BODY - ORGANIZE BY THEMES OR CHRONOLOGICALLY

Option 1: Thematic Organisation
Theme 1: [Topic/Concept]
• Summarise key studies and findings
• Compare different perspectives
• Identify agreements and disagreements
• Your analysis of the theme

Theme 2: [Topic/Concept]
• (Repeat structure)

Theme 3: [Topic/Concept]
• (Repeat structure)

Option 2: Chronological Organisation
Early Research (dates)
• What did early scholars discover?
• What methods did they use?

Recent Research (dates)
• How has understanding evolved?
• What new methods are being used?

Current Research (dates)
• What are the latest findings?
• What questions remain unanswered?

CRITICAL ANALYSIS
For each source, consider:
• Methodology: How was the research conducted?
• Findings: What did they discover?
• Strengths: What makes this research valuable?
• Limitations: What are the weaknesses?
• Relevance: How does it relate to your topic?

SYNTHESIS
• Identify patterns across studies
• Note areas of consensus
• Highlight contradictions or debates
• Identify gaps in the research
• Show how studies relate to each other

CONCLUSION
• Summarise main findings from the literature
• Identify research gaps
• Suggest directions for future research
• Explain implications for your topic

References
• List all sources in proper format, APA, MLA and so on
    """
    alert(literature_review_template, large=True, title="Literature Review Template")