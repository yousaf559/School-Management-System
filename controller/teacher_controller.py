from model.teacher import Teacher

class TeacherController():
    @classmethod
    def login(cls, username, password):
        teacher = Teacher()
        return teacher.login(username, password)
        