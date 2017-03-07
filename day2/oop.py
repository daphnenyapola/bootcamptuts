# demonstrating inheritance i.e student from teacher
class teacher:
	def assign_course_work(self):
		print("this semesters coursework includes")
#illustrate encapsulation
	def marking_schemes_location(self,location="cabinet"):
		self.__location=location

class student(teacher):
	def print_course_name(self,a=1,b=2):
		print("introduction to programming",a,".",b)
		


#illustrate polymorphism(method print_course_name)
class new_vesrion(teacher):
	def print_course_name(self,a=1,b=2):
		print("introduction to programming",a*b)

second=new_vesrion()		
course=student()
second.print_course_name()
course.assign_course_work()
course.print_course_name()
