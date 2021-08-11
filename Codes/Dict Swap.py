old_dict = {'A': 67, 'B': 23, 'C': 45, 'E': 12, 'F': 69, 'G': 67, 'H': 23} 
print ("Original dictionary is : ") 
print(old_dict) 
new_dict = {} 
for key, value in old_dict.items(): 
    if value in new_dict:
        new_dict[value].append(key) 
    else:
        new_dict[value]=[key] 
print ("Dictionary after swapping is : ")
print(new_dict)
