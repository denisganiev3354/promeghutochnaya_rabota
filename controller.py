class Controller(object):
    def __init__(self, model, view) :
        self.model = model
        self.view = view

    def create_note(self, note):
        self.model.create_note(note)
        self.view.display_note_stored()
    
    def notes_exist(self):
        notes = self.model.read_notes()

    def show_note(self, note_id);
        try:
            note = self.model.read_note(note_id)
            self.view.show_note(note)
        except ValueError:
            self.view.display_note_id_not_exist(note_id)
