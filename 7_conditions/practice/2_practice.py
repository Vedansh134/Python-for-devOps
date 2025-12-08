# 2. Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = float(input("Enter physics marks : "))
sub2 = float(input("Enter chemistry marks : "))
sub3 = float(input("Enter maths marks : "))

total_marks_obtained = sub1 + sub2 + sub3
total_max_marks = 300

avg = (sub1 + sub2 + sub3)/3

percentage = (total_marks_obtained / total_max_marks) * 100
# test
# print(percentage)

# Define passing criteria
minimum_passing_percentage = 40.0
minimum_passing_marks = 33.0

passed_total = percentage >= minimum_passing_percentage
passed_subjects = ( sub1 >= minimum_passing_marks ) and ( sub2 >= minimum_passing_marks ) and ( sub3 >= minimum_passing_marks )

if passed_total and passed_subjects:
    print(f"Congratuations! Pass.\nPercentage : {percentage:.2f}%")
    print(f"Student : PASS! as total greater >= 40% and all subjects >= 33%")
else:
    print(f"Result : FAIL! Not meet elgiblity criteria")
    print(f"Percentage : {percentage:.2f}%")


