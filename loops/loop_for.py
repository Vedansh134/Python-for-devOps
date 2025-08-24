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

