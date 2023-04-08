def read_file(file):
#verific existenta fisierului
    try:
        f = open(file)
    # citirea numarului de noduri si muchii
        sizes = [int(s) for s in f.readline().strip('\t\n').split(' ')]
        edges_no = sizes[1]
    # citirea muchiilor
        edges = [[element for element in f.readline().strip('\t\n').replace(' ', '')] for edge in range(edges_no)]
    # citirea nodurilor initiale si finale
        initial = f.readline().strip('\t\n').replace(' ', '')
        final = f.readline().strip('\t\n').split(' ')
        final.pop(0)
    # citirea cuvintelor de test
        words_no = int(f.readline())
        words = [f.readline().strip('\t\n') for i in range(words_no)]
        f.close()
        return edges, initial, final, words
# fisier inexistent
    except FileNotFoundError:
        print("Nu s-a gasit fisierul specificat!")
        return False, False, False, False


def dfa_verify(word, initial_state, final, edges):
    actual_state = initial_state
    processed_letters = 0
    path = [actual_state]
# verificarea existentei unui drum spre un nod termial
    for letter in word:
        for i in range(len(edges)):
            if edges[i][0] == actual_state and edges[i][2] == letter:
                processed_letters += 1
                actual_state = edges[i][1]
                path.append(actual_state)
                break
# verificarea rezultatului (nod terminal si toate litere procesate)
    if actual_state in final and  processed_letters == len(word):
        return True, path
    else:
        return False, path

def __main__():
    edges = []
    final = []
    words = []
    path = []
# citirea automatului si a cuvintelor de test
    edges, initial_state, final, words = read_file("input.in")

    if initial_state is not False:
        g = open("output.out", "w")
    # verificarea cuvintelor de test printr-un DFA
        for word in words:
            result, path = dfa_verify(word, initial_state, final, edges)
            if result is False:
                g.write("NU\n")
            else:
                g.write("DA\n")
                p = ' '.join([str(node) for node in path])
                g.write("Traseu: " + p +"\n")
        g.close()

__main__()
