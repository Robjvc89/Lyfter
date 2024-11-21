class Student:
    def __init__(self, name, section, spanish_note, english_note, social_note, science_note):
        self.name = name
        self.section = section
        self.notes = {
            "Spanish": spanish_note,
            "English": english_note,
            "Social": social_note,
            "Science": science_note,
        }
        self.average = (spanish_note + english_note + social_note + science_note) / 4 

    def to_dict(self):
        return {
            "name": self.name,
            "section": self.section,
            "notes": self.notes,
            "average": self.average
        }
    
    def from_dict(cls, data):

        spanish_note = float(data['notes']["Spanish"])
        english_note = float(data['notes']["English"])
        social_note = float(data['notes']["Social"])
        science_note = float(data['notes']["Science"])
        
        return cls(
            data["name"],
            data["section"],
            spanish_note,
            english_note,
            social_note,
            science_note
        )
    
