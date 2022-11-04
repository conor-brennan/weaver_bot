import math
from queue import Queue
import weaver_vars

AllWords = []
with open('4letterwords_official.txt') as file:
    lines = file.readlines()
for l in lines:
    AllWords.append(l[:4])


# returns # of letters in common for 4 letter words
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

# returns array of all words 1 letter swap away from current_word
def next_words(current_word):
    result = []
    for w in AllWords:
        if lets_in_common(current_word, w) == 3:
            result.append(w)
    return result

# returns 'graph' dictionary. <key,val> = <word,[neighbours]>
def generate_graph():
    word_graph = {}
    for current_word in AllWords:
        word_graph[current_word] = next_words(current_word)
        print("'{}': {},".format(current_word,word_graph[current_word]))
    return word_graph

# bfs search over word list
def bfs_search(start, goal):
    #initialize queue and vars
    q = Queue(maxsize = len(AllWords))
    start = start.upper()
    goal = goal.upper()
    visited = {}
    visited[start] = ""
    q.put(start)

    #loop over queue, adding all connected words to back of queue
    while not q.empty():
        current_word = q.get()
        if current_word == goal:
            return visited
        for word in weaver_vars.word_graph[current_word]:
            if not word in visited:
                #labels words with their 'parent' node to preserve path
                visited[word] = current_word
                q.put(word)

def do_weaver(start, goal):
    start = start.upper()
    goal = goal.upper()
    visited = bfs_search(start, goal)
    path = [goal]
    try:
        current = visited[goal]
        while True:
            if not current == "":
                path.append(current)
                current = visited[current]
            else:
                break
        return path[::-1]
    except:
        print("No path found")
        return []
    
def path_compare(word1, word2):
    path1_2 = do_weaver(word1,word2)
    path2_1 = do_weaver(word2,word1)
    if path1_2 == path2_1[::-1]:
        print("Same path: {}".format(path2_1))
    else:
        print("Different paths: {}\n\t\t{}".format(path1_2,path2_1[::-1]))
