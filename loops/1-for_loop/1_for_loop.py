# for loop in python

tech_stack = ["AI","ML","cloud","cyber","IoT","Blockchain","MERN","Data Science"]

for tech in tech_stack:
    if len(tech) > 4:
        print(f"long tech name : {tech}")
    else:
        print(f"short tech name : {tech}")
print(type(tech))


# range is keyword in python
# used : range is used to generate a sequence of numbers
# syntax range(start,stop,step_size)


list = ["AI","ML","cloud","cyber","IoT","Blockchain","MERN","Data Science"]

for id in range(len(list)):
    print(f"Tech stack {id} : {list[id]}")

