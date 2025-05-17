name_list =["Kagetera","Jhon","Peter","Alex","Claude"]
print(name_list)
name_list.sort(reverse=True)
print("sorted with descending order")
print("----------------------------")
print(name_list)
name_list.append("Olivier")
name_list.append("UOK")
name_list.append("Uwayo Gacumbitsi")
name_list.sort(reverse=True)
for i in name_list:
    print(i)