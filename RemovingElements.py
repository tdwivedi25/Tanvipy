list=['Tanvi','Ishan','Shalini','Pankaj','children','parents','girl','boy','man','woman']
for i in range(0,len(list)):
    if i in (0,4,5):
      list.remove(list[i])



#list.remove(list[0])
#list.remove(list[4])
#list.remove(list[5])
print(list)
