# for loop in python
# range is keyword in python range(start,stop,step_size)

tech_stack = ["AI","ML","cloud","cyber","IoT","Blockchain","MERN","Data Science"]

for tech in tech_stack:
    if len(tech) >= 4:
        print(f"Core Tech : {tech}")
    else:
        print(f"short name : {tech}")


list = ["AI","ML","cloud","cyber","IoT","Blockchain","MERN","Data Science"]
for id in range(len(list)):
    print(f"Tech {id}: {list[id]}")


for i in range(0,22,2):
    print(f"even no. : {i}")



# while and break in for loop
for i in range(1,20):
    if i == 11:
        print("not print 10")
        continue
    if i == 15:
        print("stop from 15")
        break
    print(f"num : {i}")


# create /modify/separate list from existing list
tech_stack = ["python","java","node.js","aws"]
techC = []
for tech in tech_stack:
    cap = tech.upper()
    techC.append(cap)
print(techC)

# Nested loop multiplication table
for i in range(1,11):
    row = []
    for j in range(1,11):
        row.append(i*j)
    print(row)