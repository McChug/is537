# DSA Portfolio

## Table of Contents

- [1. Valid Sudoku](#valid-sudoku)
- [2. Rotate Image](#rotate-image)
- [3. Generate Parentheses](#generate-parentheses)
- [4. Group Anagrams](#group-anagrams)
- [5. Remove Outer Parentheses](#remove-outer-parentheses)
- [6. Add Two Numbers Without Recursion](#add-two-numbers-without-recursion)
- [7. Add Two Numbers With Recursion](#add-two-numbers-with-recursion)
- [8. Shipping With Minimum Weight Capacity](#shipping-with-minimum-weight-capacity)
- [9. Next Permutation](#next-permutation)
- [10. Linked List Cycle II](#linked-list-cycle-ii)
- [11. Balanced Binary Tree](#balanced-binary-tree)
- [12. Search 2D Matrix](#search-2d-matrix)
- [13. Spiral Matrix](#spiral-matrix)
- [14. Word Search](#word-search)
- [15. Word Ladder](#word-ladder)

## About

This repository contains a collection of personal coding challenges I have completed (largely in the form of LeetCode problems or similar types of coding challenges).

This document covers 15 challenges I wanted to share. I completed each of these with minimal online searches and without LLM help. Sometimes I'd step away from a problem for some time and come back later with a fresh mind, but I'm proud to know that everything in here is my work and represents my growth in learning to problem solve.

Most code was written in Python because I have worked less in Python than JavaScript and wanted practice writing better Python.

## Projects

### <a id="valid-sudoku"></a>1. Valid Sudoku ([Source](ValidSudoku/IsBoardValid.js))

```js
function isBoardValid(board) {
  // Check whether a Sudoku board is valid
  const size = board.length;
  const factor = Math.sqrt(size);
  if (!Number.isInteger(factor)) {
    throw Error("Invalid Board! The number of row/columns is invalid.");
  }

  const checks = { row: [], col: [], subgrid: [] };

  for (let r = 0; r < size; r++) {
    const row = board[r];
    if (!Array.isArray(row) || row.length !== size) {
      throw Error(`Invalid Row at index of ${r}.`);
    }

    checks.row.push(new Set());

    for (let c = 0; c < size; c++) {
      if (r < 1) {
        checks.col.push(new Set());
      }

      if (c % factor === 0) {
        checks.subgrid.push(new Set());
      }

      const digit = board[r][c];
      if (!Number(digit)) {
        continue;
      }

      const s = Math.floor(r / factor) * factor + Math.floor(c / factor);

      if (checks.row[r].has(digit)) {
        return false;
      }
      if (checks.col[c].has(digit)) {
        return false;
      }
      if (checks.subgrid[s].has(digit)) {
        return false;
      }

      checks.row[r].add(digit);
      checks.col[c].add(digit);
      checks.subgrid[s].add(digit);
    }

    checks.row[r] = null;
  }

  return true;
}
```

My first project for this class ended up being a lot more difficult than I thought, but it was a lot of fun to think through. I figured that if a went for an algorithm with a space complexity of O(N), then I could make the time complexity O(N) as well. (Or O(N^2) for each of these depending on if you consider N to be 9 or 9x9).

By storing what already exists in each column, row, and subgrid, I could just loop through each cell of the board and make sure there were no collisions, so I initialized three arrays that could present each of these conditions to check and I pushed 9 sets into each. I also removed row sets after each loop to take back some space. Although figuring out how to put cells into their respective column and row sets was easy, coming up with what defined a subgrid was not! I diagrammed a sudoku board in Excel and started looking through what would need to happen to satisfy the condition. After writing down lots of numbers and looking for patterns, the equation finally clicked and I was able to set the variable `s` in my code which made the script come together!

Also, as a side note, it was important to me to make an algorithm that could work with any size board, as long as the length and width were the same and could be square rooted. This was just for fun since I didn't want to hard-code 9's, and I'm happy with how it turned out!

### <a id="rotate-image"></a>2. Rotate Image ([Source](rotate_image/rotate_image.py))

```python
def rotate_image(matrix):
    end = len(matrix)

    for front in range(0, end // 2):
        end = end - 1

        for offset in range(0, int(math.ceil(end + 1 / 2)) - front):
            if len(matrix[offset]) != len(matrix):
                raise ValueError("Matrix must be square.")

            (
                matrix[front][front + offset],
                matrix[end - offset][front],
                matrix[end][end - offset],
                matrix[front + offset][end],
            ) = (
                matrix[end - offset][front],
                matrix[end][end - offset],
                matrix[front + offset][end],
                matrix[front][front + offset],
            )

        front = front - 1

```

When I started on this algorithm, it looked a whole lot like a sudoku board to me, and since I had just spent so much time and mental energy trying to come up with all the patterns and sequences I could on these boards, I thought that I would be able to solve this problem intuitively. I was very wrong.

I originally intialized my two for loops with variables named i and j, and my code looked fairly similar to what I ended up with, but I couldn't keep everything in my head in order to define all the switching I had to do. Eventually, it occured to me to switch the name of my first index to `front`, and I also renamed my length variable to `end`, which started to help me conceptually pick up on what my code was meant to do better. Things still weren't quite right until I renamed my inner loop's index to `offset`, and at that point I was finally able to write out in code the ideas that I had in my head and actually keep track of what it was doing.

I was pleased to see after the fact that these names are used in solutions posted online. It really was in coming up with these names that I could finally see the pattern that could perform a rotation not just on a 3x3 grid, but also a 4x4 and 5x5 and on.

### <a id="generate-parentheses"></a>3. Generate Parentheses ([Source](GenerateParentheses.py))

```python
def generateParentheses(n: int):
    solutions: list[str] = []

    for i in range(2 ** (n * 2 - 1)):
        solution = "("
        open = 1
        close = 0

        while close <= open and open <= n:
            if len(solution) == n * 2:
                solutions.append(solution)
                break

            if i % 2 == 0:
                solution += ")"
                close += 1
            else:
                solution += "("
                open += 1

            i = i // 2

    return solutions
```

This project comes from LeetCode #22. I started the project by drawing out all the possible valid combinations of parentheses and trying to figure out any patterns that existed. After way too many drawing and way too much thinking, I decided that I would take a step back and instead make an algorithm that could generate every possible combination of parentheses and only hold on to the good ones. It took some thinking since I've never written a script like this before, but after a nice break from the project it finally clicked with me that since there are only two possible characters, I could treat opening and closing parentheses as if they were ones and zeros and from there generate each combination as if I was just converting decimal to binary. From there I coded my script and just ran into one more issue. I set up my loop as n^2 rather than 2^n, so my code was skipping several valid solutions. After some debugging, that truth finally hit my like a bag of boulders and then I got the code working!

This was an incredibly satisying problem to finally solve, and a lot of fun to work on throughout.

### <a id="group-anagrams"></a>4. Group Anagrams ([Source](GroupAnagrams.py))

```python
def groupAnagrams(strs: list[str]):
    result: list[list[str]] = []

    current_index = 0
    addresses: dict[str, int] = {}

    for word in strs:
        ordered = "".join(sorted(word))

        if ordered in addresses:
            result[addresses[ordered]].append(word)
        else:
            result.append([word])
            addresses[ordered] = current_index
            current_index += 1

    return result
```

This problem ended up being quite a bit simpler than my others. By using a hash table with keys set by taking a string through Python's native `sorted()` function, I was able to very efficiently populate the table and check to see if strings were anagrams.

### <a id="remove-outer-parentheses"></a>5. Remove Outer Parentheses ([Source](RemoveOutParentheses.py))

```python
def removeOuterParentheses(s: str) -> str:
    s_list = list(s)
    counter = 0

    for i in range(len(s_list)):
        if s_list[i] == "(":
            counter += 1
            prep_delete = counter == 1
        else:
            counter -= 1
            prep_delete = counter == 0

        if prep_delete:
            s_list[i] = ""

    return "".join(s_list)
```

We started this algorithm in class and I thougt immediately I had an idea that would work for it, but as I tried to write out the code quickly I ended up running into errors. I ended up coming back to the problem after class and was happy to see that my intuition on how it could be solved did work, but it took a little more effort to get it right. Basically, my code works because, assuming that each string of parentheses is valid, I can always delete the first index, and track that I've seen one opening parenthesis. After that, I can increment or decrement my counter and remove the next closing parenthesis when the counter hits 0. It was a simple concept and worked in O(N) time!

### <a id="add-two-numbers-without-recursion"></a>6. Add Two Numbers Without Recursion ([Source](AddTwoNumbers/WithoutRecursion.ts))

```python
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null,
): ListNode | null {
  let carry: 0 | 1 = 0;
  let dummy: ListNode = new ListNode();
  let temp = dummy;

  while (l1 || l2 || carry) {
    const val1 = l1 ? l1.val : 0;
    const val2 = l2 ? l2.val : 0;

    let sum = val1 + val2 + carry;

    if (sum >= 10) {
      sum -= 10;
      carry = 1;
    } else {
      carry = 0;
    }

    const current = new ListNode(sum);
    temp.next = current;
    temp = current;

    l1 = l1?.next ?? null;
    l2 = l2?.next ?? null;
  }

  return dummy.next;
}
```

I was looking for some recursion practice and found this problem (Leetcode #2) right at the top of the recursion list. Without much recursion practice yet, I kept going back to bottom-up solutions as I tried to think through the problem, so I decided to start with a non-recursive solution, which went well. I hadn't went over linked lists in class yet but had some minimal understanding of them. I ended up reading up some on best practices for working with them because I just about had all my code's logic down except for actually generating the result in a linked list. I found out about things like starting with dummy heads, or sentinel nodes, and using a temporary variable to overwrite my list, and after implementing the fix to how I was writing the nodes, the code worked! The dummy head is useful because it lets you go straight to putting your nodes through a loop rather than writing special code for the first iteration. I'll aim to figure out the recursive solution, too, but this ended up being a great introduction to working with linked lists.

As far as the adding logic went for this algorithm, I just kept a running carry bit of sorts that would change to a 0 or 1 after each sum was calculated. It seemed intuitive and the effeciency ended up great so this script ran in O(N) time.

### <a id="add-two-numbers-with-recursion"></a>7. Add Two Numbers With Recursion ([Source](AddTwoNumbers/WithRecursion.ts))

```js
class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null,
  carry: 0 | 1 = 0,
): ListNode | null {
  const val1 = l1 ? l1.val : 0;
  const val2 = l2 ? l2.val : 0;
  const next1 = l1 ? l1.next : null;
  const next2 = l2 ? l2.next : null;

  let sum = val1 + val2 + carry;

  if (sum >= 10) {
    sum -= 10;
    carry = 1;
  } else {
    carry = 0;
  }

  if (next1 || next2)
    return new ListNode(sum, addTwoNumbers(next1, next2, carry));

  if (carry) return new ListNode(sum, new ListNode(carry));

  return new ListNode(sum);
}
```

After getting my feel for linked lists in my previous algorithm for this problem, the recursive solution wasn't too bad to solve. Because I only ever make one recursive call at most in the function, no memoization or dynamic programming was needed to keep the time efficiency for this the same at O(N). And by implementing the recursive generation of nodes, I didn't have to do any odd logic with a dummy node at the head, so this ended up being a cleaner solution in my opinion. One interesting gotcha at the end of solving this was that I didn't handle the last carry bit if the last recursive call had a carry of 1, so I created a second base case to handle this.

### <a id="shipping-with-minimum-weight-capacity"></a>8. Shipping With Minimum Weight Capacity ([Source](CapacityToShip.py))

```py
def shipWithinDays(weights: list[int], days: int) -> int:
    def isPossible(capacity: int):
        accumulator = 0
        day = 1
        i = 0
        while i < len(weights):
            accumulator += weights[i]
            if accumulator > capacity:
                accumulator = 0
                day += 1
            else:
                i += 1

            if day > days:
                return False

        return True

    bottom = max(weights)
    capacity = reduce(lambda x, y: x + y, weights)

    while bottom < capacity:
        mid = (capacity + bottom) // 2
        if isPossible(mid):
            capacity = mid
        else:
            bottom = mid + 1

    return capacity
```

I started this algorithm as part of class and did not make it far. When encouraged to continue working on it, I still felt unsure about how to proceed, but the hints from class ended up helping me to solve it without too much difficulty. I had originally been attempting to find some kind of pattern that would let me loop through the list and return the minimum capacity, but was I shifted to just building a validator function that could return whether any given capacity would be good, I realized it wasn't too difficult. One thing worth noting is the binary search in this script. Instead of starting tests at a capacity of 0 or 1, I use built-in python functions to quickly return the maximum weight of any day and the total weight of the entire list's items, and these serve as the left and right parameters to a binary search that allow me to find the least valid capacity in O(logN) time. This is interesting because rather than doing a binary search on the array, its a search on all possible solutions.

### <a id="next-permutation"></a>9. Next Permutation ([Source](NextPermutation/FirstAttempt.py))

```py
def NextPermutation(nums: list[int]) -> None:
  def palindrome(left: int, right: int):
      while left < right:
          nums[left], nums[right] = nums[right], nums[left]
          left += 1
          right -= 1

  def bubble_from(left: int, length: int):
      iteration = 0
      for _ in range(left, length - 1):
          for b in range(left, length - iteration - 1):
              if nums[b] > nums[b+1]:
                  nums[b], nums[b+1] = nums[b+1], nums[b]
          iteration += 1

  length = len(nums)
  high = -1
  low = -1

  for i in range(length - 1, 0, -1):
      for j in range(i, -1, -1):
          if nums[i] > nums[j]:
              if low == -1 or low < j:
                  high = i
                  low = j

  if high != -1 and low != -1:
      nums[high], nums[low] = nums[low], nums[high]
      bubble_from(low+1, length)
  else:
      palindrome(0, length - 1)
```

This problem seemed straightfoward when I began, but I kept getting caught up in small errors like my loops being off by one iteration, or my bubble sort starting and ending at the wrong values. Being able to work through all of these helped me build my intuition on loops. In the end, my algorithm was not a very sophisticated one, with a Big O of O(N^2\*2). I would love to revist this problem in the future because I believe that faster methods are possible.

### <a id="linked-list-cycle-ii"></a>10. Linked List Cycle II ([Source](LinkedListCycleTwo.py))

```py
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def detectCycle(head):
    stop = getStopNode(head)
    if stop == None: return None

    outside = head
    while outside:
        same_seen = False
        stop_seen = False
        inside = head

        while inside:
            if inside == outside and same_seen:
                return inside
            elif inside == outside:
                same_seen = True

            if inside == stop and stop_seen:
                break
            elif inside == stop:
                stop_seen = True

            inside = inside.next

        outside = outside.next

def getStopNode(head):
    fast, slow = head, head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
        if fast == slow:
            return fast

    return None
```

After going over in class how to detect cycles in linked lists with Floyd's tortoise and hare algorithm (running two pointers through a linked list at different speeds so that they eventually meet), I wanted to see how I might be able to find an effecient solution to LeetCode 142 as well. LeetCode gave a challenge in the problem description to solve with O(1) memory, so that was my goal with my solution, though it did take O(N^2) time. I used the tortoise and hare algorithm to define a "stop node" that was proven to be somewhere in the loop, and then I ran a nested loop through this linked list where I would break if I got to the stop node twice before seeing my two indexes reference the same node.

After solving this, I found some creative solutions online that worked more effeciently and I tried to learn one algorithm in specific from a solution I found interesting, but I'm pretty happy that I was able to come up with my working solution, even if less efficient.

### <a id="balanced-binary-tree"></a>11. Balanced Binary Tree ([Source](BalancedBinaryTree.py))

```py
def isBalanced(root) -> bool:
    def getBalancedHeight(node):
        if node == None:
            return 0

        left_height = getBalancedHeight(node.left)
        right_height = getBalancedHeight(node.right)

        if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    return getBalancedHeight(root) != -1
```

I started this problem by writing a regular getHeight() function, and then I added my check on each left_height and right_height calculation I did to make sure they were balanced. It took me a lot of thinking to come up with a solution for what to return in that base case, though. I tried adding another parameter called balanced that held a boolean but realized that it would never be read if I only changed it after making my recursive calls.

Finally, I settled on a hacky solution of returning -100 when the tree was out of balance, and then I ended my function by checking whether the result of getBalancedHeight() was greater than 0. This passed all of LeetCode 110's cases and worked in O(N) time, but I wasn't happy with the hacky solution. I went online and saw that a more sophisticated solution just added checks to see if the left and right heights were also -1 before returning -1. I implemented this by only changing a couple lines of code.

### <a id="search-2d-matrix"></a>12. Search 2D Matrix ([Source](Search2DMatrix.py))

```py
def searchMatrix(self, matrix, target):
    m = len(matrix) - 1
    n = len(matrix[0]) - 1

    bottom = 0
    top = m

    while bottom < top:
        mid = (bottom + top) // 2
        print(bottom, top, mid)

        if matrix[mid][0] == target or matrix[mid][n] == target:
            return True
        elif matrix[mid][0] > target:
            top = mid - 1
        elif matrix[mid][n] < target:
            bottom = mid + 1
        else:
            bottom = mid
            break

    row = matrix[bottom]
    print(row)
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        print(left, right, mid)

        if row[mid] == target:
            return True
        elif row[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
```

This was a great problem to help me test my intuition of binary searches and O(log(N)) algorithms. My initial thought was that I could just run two simple binary searches (one to find which row the possible target was in and one to search that row for the target) back-to-back and it would immediately give back my answer, but I realized this problem was a little more complicated. Because the first binary search was targeting a range rather than a specific integer value, the logic was quite a bit different.

My biggest realization while solving this problem was that I could use the `n` value (row length) in order to check the highest value of any given row, instead of just checking the lowest at `0`. This meant that instead of the three outcomes of `==`, `>`, or `<` that I would normally check in a binary search, I should only check `>` for the smallest value of a row, only check `<` for the largest value of a row, and then I would be left with one more outcome that would mean I had found the row that I needed to search.

After getting that first part right, the second step was just implementing a regular binary search on the row.

### <a id="spiral-matrix"></a>13. Spiral Matrix ([Source](SprialMatrix.py))

```py
def spiralOrder(matrix):
    result = []

    m = len(matrix)
    n = len(matrix[0])

    offset = {"top": 0, "right": 0, "bottom": 0, "left": 0}

    while True:
        for i in range(offset["left"], n - offset["right"]):
            result.append(matrix[0 + offset["top"]][i])
        offset["top"] += 1

        if offset["top"] + offset["bottom"] == m:
            break

        for i in range(offset["top"], m - offset["bottom"]):
            result.append(matrix[i][n - offset["right"] - 1])
        offset["right"] += 1

        if offset["right"] + offset["left"] == n:
            break

        for i in range(n - offset["right"] - 1, offset["left"] - 1, -1):
            result.append(matrix[m - offset["bottom"] - 1][i])
        offset["bottom"] += 1

        if offset["top"] + offset["bottom"] == m:
            break

        for i in range(m - offset["bottom"] - 1, offset["top"] - 1, -1):
            result.append(matrix[i][0 + offset["left"]])
        offset["left"] += 1

        if offset["right"] + offset["left"] == n:
            break

    return result
```

This problem was LeetCode 54 and coming up with the algorithm reminded me of some of the techniques that I learned while working on my solution for rotating a matrix a few months ago. I immediately thought to include an offset for each side (top, right, bottom, left) and increment those after looping through them.

The basic structure of my function came quickly, but it took a lot of testing and then retesting in order to get rid of all of my off-by-one errors in the loops. By the time it was working my function got a little messy, so I'd like to clean it up at some point, but I'm happy that it worked.

It's hard to tell the Big O from the code because everything operates within a `while True` loop with a chance to `break` after each step, but the time complexity is O(N) since it will reach every item within every subarray once. The space complexity is also linear because I declare a separate result array, but that is the only thing taking up variable space.

### <a id="word-search"></a>14. Word Search ([Source](WordSearch.py))

```py
def exist(board, word):
    m = len(board)
    n = len(board[0])

    def wordSearch(i, j, depth, current_path=None):
        if current_path == None:
            current_path = set()

        if board[i][j] != word[depth]:
            return False

        if depth >= len(word) - 1:
            return True

        current_path.add((i, j))

        adjacents = [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]
        valid_adjacents = [(y, x) for (y, x) in adjacents if 0 <= y and y < m and 0 <= x and x < n]
        for y, x in valid_adjacents:
            if (y, x) not in current_path:
                if wordSearch(y, x, depth + 1, current_path):
                    return True

        current_path.remove((i, j))

    for i in range(m):
        for j in range(n):
            if board[i][j] == word[0]:
                if wordSearch(i, j, 0):
                    return True

    return False
```

This was LeetCode 79 and I wanted to try it since it had the Depth-First Search tag. The method for solving seemed immediately obvious, and I thought that if I just looped through every item in the matrix until finding one with a value that matched the first item in the target string, I could start a DFS run from there. My intuition was correct, but in order to get this passing all the test cases, I spent a lot of time refining how the algorithm worked. The biggest hold up that took me a while to figure out was when to remove an item from the `current_path` set, but once I finally got that, everything came together.

The time complexity for my algorithm is O(m _ n _ 4^L), if L is the length of the target `word`. This is because I iterate over every item in the board input (making up the O(m \* n)), and then I run the DFS where there are a max of 4 recursive calls to make for each item I explore until I have reached the depth of the target word. Because I use a set for the `current_path`, lookups happen in O(1).

### <a id="word-ladder"></a>15. Word Ladder ([Source](WordLadder.py))

```py
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
```

This problem was LeetCode 127 and it had the Breadth-First Search tag. My solution was far from the most effecient, but I think I wrote it cleanly and it makes a lot of sense. Rather than working directly in the array that the function takes as an input, I converted the array into a graph. With the graph, I then run a BFS algorithm to find the `endWord`. I store each vertex in a queue that I iterate through for the BFS portion, and I store the vertex in a tuple alongside a `depth` variable that I can use to return at the end.

Because of the nested loop I wrote to turn the array into a graph, the Big O of my script is O(N^2). It may be a cool project in the future to try creating a breadth-first search that runs in an array, and I think something like that may speed this up (though I haven't looked into it). Overall, I'm happy that I was able to create implement several data structures from memory in here, along with the BFS algorithm.
