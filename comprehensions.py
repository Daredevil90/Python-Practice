num=[1,2,3]
new_num = [x*2 for x in num]
print(new_num)
cookie=['c','d','e']
new_dict={key:value for (key,value) in zip(num,cookie)}
print("Using two lists:",new_dict)
new_set ={x for x in num if x not in [2]}
print(new_set)