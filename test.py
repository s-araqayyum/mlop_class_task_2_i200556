from main import StudentsInMLOps

def test_enroll_drop_students():
    classroom = StudentsInMLOps()
    classroom.enrollStudents(5)
    assert classroom.getTotalStrength() == 5
    classroom.dropStudents(2)
    assert classroom.getTotalStrength() == 3

def test_get_class_name():
    classroom = StudentsInMLOps()
    assert classroom.getClassName() == "MLOps"
