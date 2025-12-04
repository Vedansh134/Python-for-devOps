
branch = input("Enter your core branch : ")
skills = input("Enter your skills according to your branch : ")

def career_skills(skills, core_branch="Cloud Computing"):
    # Check if the passed core_branch is an empty string
    if not core_branch:
        core_branch = "Cloud Computing" # Reassign to the intended default

    field = f"Your core branch is {core_branch} and"
    skill = f"You know {skills} and related to {core_branch} field"
    return field + " " + skill

student = career_skills(skills, branch)
# or also student = career_skills("aws")
print(student)

# Output : (If mention branch)
# Enter your core branch : Cloud
# Enter your skills according to your branch : aws,azure,python,git
# Your core branch : Cloud You know aws,azure,python,git and related to Cloud field

# Output : (If not mention branch)
