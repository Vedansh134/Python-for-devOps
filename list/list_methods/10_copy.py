# Copy method in list
# Used : Return the shallow copy of list

import copy

skills = ["cyber security","devOps","cloud","frontend",["HTML","CSS","JS"],"IoT"]

# Create a deep copy to avoid modifying the inner list in the other list
copy_list = copy.deepcopy(skills)

skills[2] = "AI & ML"
copy_list[4][2] = "React.JS"

print("original list after update : ",skills)
print("original list after update : ",copy_list)
