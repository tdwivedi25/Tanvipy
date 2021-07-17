color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])


list1=[2,3,4,5]
list2=['sd','td','id','pd']
dictnew=dict(zip(list1,list2))
print(dictnew)