# Keyword Arguments
# Arguments are specified using the parameter name in the function call. This frees you from worrying about the order of arguments

name = input("Enter your name : ")
course = input("Enter your course : ")
cgpa = float(input("Enter your cgpa : "))

def stu_record(stu_name,stu_course,stu_cgpa):
    info = f"Student name : {stu_name} and enrolled in course : '{stu_course}' and CGPA - {stu_cgpa}"
    return info

acd_record = stu_record(stu_cgpa=cgpa,stu_name=name,stu_course=course)
print(acd_record)

# Keyword call: order does not matter
# describe_pet(pet_name='Buddy', animal_type='dog')

# Output :
# ===== Enter your name : vedansh
# ===== Enter your course : bca
# ===== Enter your cgpa : 8.4
# Student name : vedansh and enrolled in course : 'bca' and CGPA - 8.4