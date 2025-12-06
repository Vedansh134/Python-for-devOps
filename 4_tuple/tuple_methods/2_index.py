# Index method in tuple
# Used : To find the indexing position of an element in tuple

tuple = (2,4,6,8,(1,3,5,7),10,True,""," ","string",0,10)

no1 = 10
no2 = "" # 3 so error handle by try-catch

index1 = tuple.index(no1)
print(f"Indexing position of {no1} : {index1}")

index2 = tuple.index(no2)
print(f"Indexing position of {no2} : {index2}")
