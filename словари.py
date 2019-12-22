all = open("predators_prey.txt",'r')
d = {}
for line in all:
    key, *value = line.strip().split(' eats ')
    if key:
        d.setdefault(key,[])
        d[key].append(', '.join(value))
all.close()


print('Predators and prey:')
for k,v in d.items():
    print(str(k)+' eats '+', '.join(v))
    



file = open("formated_predators_prey.txt", 'w')
file.write('Predators and prey:\n')
for k,v in d.items():
    file.write(str(k)+' eats '+', '.join(v)+'\n')
file.close()


















