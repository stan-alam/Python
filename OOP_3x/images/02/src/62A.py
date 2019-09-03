def __find_note(self, note_id):
    """Locate the note with the id"""
    for note in self.notes:
        if note.id == note_id:
            return note
    return None
    
def modify_memo(self, note_id, memo):
    """find the note with the given id and change its memo to the entered id"""
    self._find_note(note_id).memo = memo
    
def modify_tags(self, note_id, tags):
    """Find the note with the given id and change its tags to the given value"""
    self._find_note(note_id).tags = tags
