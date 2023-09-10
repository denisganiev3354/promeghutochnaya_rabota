class  ModelJSON(object):
    def read_notes(self):
        return self.read_json()
    
    def read_json(self):
        notes_list = list()
        try:
            with open(self.filename, "r", encoding='utf-8') as my_file:
                notes_json = my_file.read()
            data = json.loads(notes_json)
            data.sort(key=lambda x: x['date'])
            for item in data:
                notes_list.append(Note(item['id'], item['date'], item['title'], item['text']))

            return notes_list
        except ValueError:
            return self.read_notes

    def read_note(self, search_id):
        self.notes = self.read_notes()
        for note in self.notes:
            if note.note_id == search_id:
                return note
            else:
                view.display_note_id_not_exist(search_id)