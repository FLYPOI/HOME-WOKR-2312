f = open('dick.txt', 'r', encoding = 'utf-8')
dick=f.readlines()
fi=open('bip.txt', 'r', encoding = 'utf-8')






dict={}
for each in fi.readlines():
    dict[each.strip()]=0
#Create a dictionary containing all bips





for each in dick:
    for each2 in dict.keys():
        dict[each2]+=each.count(each2)
#Count occurrences of each bip




a=sorted(dict.items(), key=lambda item:item[1], reverse=True)
#Sort dictionary values



print(a[:20])





