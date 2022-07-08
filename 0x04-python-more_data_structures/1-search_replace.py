#!/usr/bin/python3
def search_replace(my_list, search, replace):
<<<<<<< HEAD
    copy = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] == search:
            copy[i] = replace
    return copy
=======
copy = my_list.copy()
for i in range(len(my_list)):
if my_list[i] == search:
copy[i] = replace
return copy
>>>>>>> 9fe8971604197c0f07d9f1a59cb46be84a35ad02
