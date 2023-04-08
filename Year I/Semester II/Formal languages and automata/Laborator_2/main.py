import argparse

def get_line_arguments():
    parser = argparse.ArgumentParser()
# declarare argumente si introducerea lor intr-o lista
    parser.add_argument('file', help="dfa_config_file")
    parser.add_argument('word', help="word_input")
    args = parser.parse_args()

    return args.file, args.word

def read_file(input_file):
    f = open(input_file, "r")
    line = f.readline()
    sigma = []
    states = []
    transitions = []
    while line:
        if line.startswith('Sigma'):
            line = f.readline()
            while line.startswith('End') is False:
                line = line.replace(" ", "").strip('\t\n')
                sigma.append(line)
                line = f.readline()
        elif line.startswith('States'):
            line = f.readline()
            while line.startswith('End') is False:
                line = line.replace(" ", "").strip('\t\n')
                line = line.split(',')
                states.append(line)
                line = f.readline()
        elif line.startswith('Transitions'):
            line = f.readline()
            while line.startswith('End') is False:
                line = line.replace(" ", "").strip('\t\n')
                line = line.split(',')
                transitions.append(line)
                line = f.readline()
        line = f.readline()

    return sigma, states, transitions

def file_verify(sigma, states, transitions):
    t_errors = 0
# verificare tranzitii
    for t in transitions:
        if t[1] not in sigma:
            t_errors += 1
            print("Nu exista litera " + t[1] + " din tanzitia " + str(t))
        node1 = node2 = False
        for s in states:
            if s[0] == t[0]:
                node1 = True
            if s[0] == t[2]:
                node2 = True
        if not node1:
            t_errors += 1
            print("Nu exista starea " + t[0] + " din tranzitia " + str(t))
        if not node2:
            t_errors += 1
            print("Nu exista starea " + t[2] + " din tranzitia " + str(t))
# verificare unicitate stare initiala
    init_nr = 0
    for i in range(len(states)):
        if len(states[i]) > 1 and states[i][1] == "S":
            init_nr += 1
            initial_state = states[i][0]
    if t_errors != 0:
        print("S-au intrdus " + str(t_errors) + " date eronate in tranzitii!")
        initial_state = -1
    if init_nr != 1:
        print("Eroare in declararea starilor: " + str(init_nr) + " stari initiale")
        initial_state = -1

    return initial_state

def dfa_verify(word, initial_state, states, transitions):

    actual_state = initial_state
    processed_letters = 0

    for letter in word:
        for i in range(len(transitions)):
            if transitions[i][0] == actual_state and transitions[i][1] == letter:
                processed_letters += 1
                actual_state = transitions[i][2]
                break

    final_state = 0
    for i in range(len(states)):
        if states[i][0] == actual_state:
            if len(states[i]) == 2 and states[i][1] == "F":
                final_state += 1
                break
            if len(states[i]) == 3 and states[i][2] == "F":
                final_state += 1
                break
    if final_state == 0 or processed_letters != len(word):
        print(">>reject")
    else:
        print(">>accept")

def __main__():
# citire argumente
    input_file, word = get_line_arguments()
# citire fisier
    sigma, states, transitions = read_file(input_file)
# validare fisier
    initial_state = file_verify(sigma, states, transitions)
# verificare printr-un DFA a cuvantului citit
    if initial_state != -1:
        dfa_verify(word, initial_state, states, transitions)

__main__()
