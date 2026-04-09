def ladderLength(beginWord, endWord, wordList):
    # Step 1: Build Graph
    v1 = Vertex(beginWord)
    graph = [Vertex(x) for x in wordList]
    graph.append(v1)

    length = len(graph)

    for i in range(length):

        cur = graph[i]

        for j in range(i + 1, length):
            inner = graph[j]

            if offByOne(inner.val, cur.val):
                inner.adj_list.append(cur)
                cur.adj_list.append(inner)

    # Step 2: Run BFS on Graph
    queue = Queue()
    queue.enqueue((v1, 1))

    visited = set()

    while queue:
        cur, depth = queue.dequeue()
        
        for vertex in cur.adj_list:
            if vertex in visited:
                continue
                
            if vertex.val == endWord:
                return depth + 1
            
            visited.add(vertex)
            queue.enqueue((vertex, depth + 1))
    
    return 0
            

def offByOne(s1, s2):
    if len(s1) != len(s2) or s1 == s2:
        return False

    hasDiffChar = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if hasDiffChar:
                return False
            hasDiffChar = True
    
    return True
                
class Vertex:
    def __init__(self, val):
        self.val = val
        self.adj_list = []

class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __bool__(self):
        return self.length > 0

    def enqueue(self, val):
        node = LinkedListNode(val)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def dequeue(self):
        result = self.head.val

        if self.head.next:
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None

        self.length -= 1

        return result