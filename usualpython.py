"""university={'IT':54,'economy':6,'medicine':87}
university['IT']=55
university['lingustik']=556
university.pop('medicine')
total = sum(university.values())
print(total)


dict_={1:'a',2:'b',3:'c'}
new_dict={}
for key, value in dict_.items():
    new_dict.update({value: key})
print(new_dict)                          
count=int(input("how many guests"))
guests={}
for i in range(1,count+1):
    names=input()
    guests[i]=names
print(guests)"""

#my_list=[{'alma':44},
#         {'meat':33},
#         {'potato':9},
#        {'asdroid':2},
#         {'pizza':67}]
#while my_list:
 #   products_to_remove=input()
 #   for products in my_list:
 #       if products_to_remove in products:
 #           del products[products_to_remove]
 #           print(my_list)
  #  if not any(my_list):
  #      break
#print('it"s time to pay')
list_=['yellow','red','blue','dark']
list1=[]
for i in list_:
    c=i[::-1]
    list1.append(c)
list1.sort(key=lambda x: len(x))
print(list1)


#task32
list1=[1,2,3,4,5,6,7,8,9]
element='A'
step=2
for i in range(0,len(list1),step):
    list1.insert(i+step,element)
print(list1)


#task33
list1=[[1,2,3],[2,3,4,5],[43,34,343434]]
max_sublist=max(list1,key=sum)
print(max_sublist)


#task34
list_=[1,1,1,2,2,3,4,4,5]
bebra=[]
for i in list_:
    if list_.count(i) >1 and i not in bebra:
        bebra.append(i)
print(bebra)
    

    

