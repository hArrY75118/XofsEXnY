# 代码生成时间: 2025-10-01 02:15:29
import pandas as pd

"""
An online learning platform using Python and Pandas to manage courses and students.
"""

class OnlineLearningPlatform:
    def __init__(self):
        # Initialize the platform with empty DataFrames for courses and students
        self.courses = pd.DataFrame(columns=['CourseID', 'Title', 'Description', 'Duration'])
        self.students = pd.DataFrame(columns=['StudentID', 'Name', 'Email', 'EnrolledCourses'])

    def add_course(self, course_id, title, description, duration):
        """
        Add a new course to the platform.
        
        :param course_id: Unique identifier for the course
        :param title: Title of the course
        :param description: Description of the course
        :param duration: Duration of the course in hours
        """
        new_course = pd.DataFrame({'CourseID': [course_id], 'Title': [title], 'Description': [description], 'Duration': [duration]})
        self.courses = pd.concat([self.courses, new_course], ignore_index=True)

    def add_student(self, student_id, name, email):
        """
        Add a new student to the platform.
        
        :param student_id: Unique identifier for the student
        :param name: Name of the student
        :param email: Email of the student
        """
        new_student = pd.DataFrame({'StudentID': [student_id], 'Name': [name], 'Email': [email], 'EnrolledCourses': []})
        self.students = pd.concat([self.students, new_student], ignore_index=True)

    def enroll_student(self, student_id, course_id):
        """
        Enroll a student in a course.
        
        :param student_id: Unique identifier for the student
        :param course_id: Unique identifier for the course
        """
        try:
            student_row = self.students[self.students['StudentID'] == student_id]
            course_row = self.courses[self.courses['CourseID'] == course_id]
            if not student_row.empty and not course_row.empty:
                student_row.iloc[0]['EnrolledCourses'].append(course_id)
                self.students[self.students['StudentID'] == student_id] = student_row.iloc[0]
            else:
                raise ValueError("Student or course not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def list_courses(self):
        """
        List all courses available on the platform.
        """
        return self.courses

    def list_students(self):
        """
        List all students registered on the platform.
        """
        return self.students

# Example usage:
if __name__ == '__main__':
    platform = OnlineLearningPlatform()
    platform.add_course('CS101', 'Introduction to Computer Science', 'An introductory course on computer science.', 40)
    platform.add_student('S001', 'John Doe', 'john.doe@example.com')
    platform.enroll_student('S001', 'CS101')
    print(platform.list_courses())
    print(platform.list_students())