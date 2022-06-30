import math
from queue import Queue
import weaver_vars

AllWords = []
with open('4letterwords_official.txt') as file:
    lines = file.readlines()
for l in lines:
    AllWords.append(l[:4])

def lets_in_common(string_a, string_b):
    if len(string_a) != 4 or len(string_b) != 4:
        return 0
    score = 0
    lower_a = string_a.lower()
    lower_b = string_b.lower()
    for i in range(4):
        if lower_a[i] == lower_b[i]:
            score += 1
    return score

def next_words(current_word):
    result = []
    for w in AllWords:
        if lets_in_common(current_word, w) == 3:
            result.append(w)
    return result

def generate_graph():
    word_graph = {}
    for current_word in AllWords:
        word_graph[current_word] = next_words(current_word)
        print("'{}': {},".format(current_word,word_graph[current_word]))


def search(root, goal):
    q = Queue(maxsize = len(AllWords))
    visited = {}
    visited[root] = ""
    q.put(root)
    while not q.empty():
        current_word = q.get()
        if current_word == goal:
##            return visited
            print(current_word)
            return
        for word in next_words(current_word):
            if not word in visited:
                # labels words with their path
                visited[word] = current_word
                q.put(word)

def finish(root, goal):
    visited = search(root, goal)
    path = [goal]
    current = visited[goal]
    while True:
        if not current == "":
            path.append(current)
            current = visited[current]
        else:
            break
    print(path)
        
    

