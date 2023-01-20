class School:

    def create(self, lesson):
        self.lesson_name = lesson


teacher = School()

# create the name of lesson for children
teacher.create('History')

print(teacher.__dict__)
