import sys
from notebook import Notebook

class Menu:
"""display menu and respond to choices"""

    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_notes,
        "4": self.modify_note,
        "5": self.quit,
    }
    
    def display_menu(self):
        print("""Notebook menu
1. Show notes
2. Search notes
3. add notes
4. modify notes
5.Quit
"""
        )
        
    def run(self):
    """Display the menu and respond to choices"""
    while True:
        self
