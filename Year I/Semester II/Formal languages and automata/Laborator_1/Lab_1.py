f = open("input.txt", "r")
l = f.readline()
sigma = []
states = []
transitions = []

while l:
    if l.startswith('Sigma'):
        l = f.readline()
        while l.startswith('End') is False:
            l = l.strip('\t\n').replace(" ","")
            sigma.append(l)
            l = f.readline()
    elif l.startswith('States'):
        l = f.readline()
        while l.startswith('End') is False:
            l = l.replace(" ", "").strip('\t\n')
            l = l.split(',')
            states.append(l)
            l = f.readline()
    elif l.startswith('Transitions'):
        l = f.readline()
        while l.startswith('End') is False:
            l = l.replace(" ", "").strip('\t\n')
            l = l.split(',')
            transitions.append(l)
            l = f.readline()
    l = f.readline()
e = 0

for t in transitions:
    a = b = 0
    if t[1] not in sigma:
        e += 1
        print("Nu exista elementul " + t[1])
    for s in states:
        if s[0] == t[0]:
            a = 1
        if s[0] == t[2]:
            b = 1
    if a == 0:
        e += 1
        print("Nu exista starea " + t[0] + " a elementului " + t[1])
    if b == 0:
        e += 1
        print("Nu exista starea " + t[2] + " a elementului " + t[1])
c = 0
for i in range(len(states)):
    if len(states[i])>1 and states[i][1] == "S":
            c += 1
if c != 1:
    print("Eroare in declararea starilor: " + str(c) + " variablie S")
if e == 0:
    print("Datele introduse sunt valide!")
else:
    print("S-au intrdus " + str(e) + " date eronate in tranzitii!")
