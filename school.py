class School:
    def __init__(self, name = None, roster = {}):
        self.name = name
        self.roster = roster
    
    def add_student(self, stud_name, grade):
        if grade not in self.roster.keys():
            students = [stud_name]
            self.roster.update({grade: students})
            return self.roster
        else:
            students = self.roster[grade]
            students.append(stud_name)
            self.roster[grade] = students
            return self.roster

    def grade(self, grade):
        return self.roster[grade]
    
    def sort_roster(self):
        for grade in self.roster.keys():
            students = self.roster[grade]
            students.sort()
            self.roster[grade] = students
        return self.roster