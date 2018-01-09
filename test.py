list1 = ["%.2d" % i for i in range(2,48)]
list2 = []
print(list1)
str = 'http://www.kinghome.it/theme1/?home&flCode='
for i in list1:

    list2.append(str+i)

print(list2)