# DSA Portfolio

## About

This repo contains a collection of personal projects I have completed (largely in the form of LeetCode problems or similar types of coding challenges).

## Projects

### 1. Valid Sudoku

My first project for this class ended up being a lot more difficult than I thought, but it was a lot of fun to think through! I figured that if a went for an algorithm with a space complexity of O(N), then I could make the time complexity O(N) as well. (Or O(N^2) for each of these depending on if you consider N to be 9 or 9x9).

By storing what already exists in each column, row, and subgrid, I could just loop through each cell of the board and make sure there were no collisions, so I initialized three arrays that could present each of these conditions to check and I pushed 9 sets into each. I also removed row sets after each loop to take back some space. Although figuring out how to put cells into their respective column and row sets was easy, coming up with what defined a subgrid was not! I diagrammed a sudoku board in Excel and started looking through what would need to happen to satisfy the condition. After writing down lots of numbers and looking for patterns, the equation finally clicked and I was able to set the variable `s` in my code which made the script come together!

Also, as a side note, it was important to me to make an algorithm that could work with any size board, as long as the length and width were the same and could be square rooted. This was just for fun since I didn't want to hard-code 9's, and I'm happy with how it turned out!

### 2. Rotate Image

When I started on this algorithm, it looked a whole lot like a sudoku board to me, and since I had just spent so much time and mental energy trying to come up with all the patterns and sequences I could on these boards, I thought that I would be able to solve this problem intuitively. I was very wrong.

I originally intialized my two for loops with variables named i and j, and my code looked fairly similar to what I ended up with, but I couldn't keep everything in my head in order to define all the switching I had to do. Eventually, it occured to me to switch the name of my first index to `front`, and I also renamed my length variable to `end`, which started to help me conceptually pick up on what my code was meant to do better. Things still weren't quite right until I renamed my inner loop's index to `offset`, and at that point I was finally able to write out in code the ideas that I had in my head and actually keep track of what it was doing.

I was pleased to see after the fact that these names are used in solutions posted online. It really was in coming up with these names that I could finally see the pattern that could perform a rotation not just on a 3x3 grid, but also a 4x4 and 5x5 and on.

### 3. Generate Parentheses

This project comes from LeetCode #22. I started the project by drawing out all the possible valid combinations of parentheses and trying to figure out any patterns that existed. After way too many drawing and way too much thinking, I decided that I would take a step back and instead make an algorithm that could generate every possible combination of parentheses and only hold on to the good ones. It took some thinking since I've never written a script like this before, but after a nice break from the project it finally clicked with me that since there are only two possible characters, I could treat opening and closing parentheses as if they were ones and zeros and from there generate each combination as if I was just converting decimal to binary. From there I coded my script and just ran into one more issue. I set up my loop as n^2 rather than 2^n, so my code was skipping several valid solutions. After some debugging, that truth finally hit my like a bag of boulders and then I got the code working!

This was an incredibly satisying problem to finally solve, and a lot of fun to work on throughout.

### 4. Group Anagrams

This problem ended up being quite a bit simpler than my others. By using a hash table with keys set by taking a string through Python's native `sorted()` function, I was able to very efficiently populate the table and check to see if strings were anagrams.

### 5. Remove Outer Parentheses

We started this algorithm in class and I thougt immediately I had an idea that would work for it, but as I tried to write out the code quickly I ended up running into errors. I ended up coming back to the problem after class and was happy to see that my intuition on how it could be solved did work, but it took a little more effort to get it right. Basically, my code works because, assuming that each string of parentheses is valid, I can always delete the first index, and track that I've seen one opening parenthesis. After that, I can increment or decrement my counter and remove the next closing parenthesis when the counter hits 0. It was a simple concept and worked in O(N) time!

### 6. Add Two Numbers Without Recursion

I was looking for some recursion practice and found this problem (Leetcode #2) right at the top of the recursion list. Without much recursion practice yet, I kept going back to bottom-up solutions as I tried to think through the problem, so I decided to start with a non-recursive solution, which went well. I hadn't went over linked lists in class yet but had some minimal understanding of them. I ended up reading up some on best practices for working with them because I just about had all my code's logic down except for actually generating the result in a linked list. I found out about things like starting with dummy heads, or sentinel nodes, and using a temporary variable to overwrite my list, and after implementing the fix to how I was writing the nodes, the code worked! I'll aim to figure out the recursive solution, too, but this ended up being a great introduction to working with linked lists.

As far as the adding logic went for this algorithm, I just kept a running carry bit of sorts that would change to a 0 or 1 after each sum was calculated. It seemed intuitive and the effeciency ended up great so this script ran in O(N) time.

### 7. Add Two Numbers With Recursion

After getting my feel for linked lists in my previous algorithm for this problem, the recursive solution wasn't too bad to solve. Because I only ever make one recursive call at most in the function, no memoization or dynamic programming was needed to keep the time efficiency for this the same at O(N). And by implementing the recursive generation of nodes, I didn't have to do any odd logic with a dummy node at the head, so this ended up being a cleaner solution in my opinion. One interesting gotcha at the end of solving this was that I didn't handle the last carry bit if the last recursive call had a carry of 1, so I created a second base case to handle this.

### 8. Shipping With Minimum Weight Capacity

I started this algorithm as part of class and did not make it far. When encouraged to continue working on it, I still felt unsure about how to proceed, but the hints from class ended up helping me to solve it without too much difficulty. I had originally been attempting to find some kind of pattern that would let me loop through the list and return the minimum capacity, but was I shifted to just building a validator function that could return whether any given capacity would be good, I realized it wasn't too difficult. One thing worth noting is the binary search in this script. Instead of starting tests at a capacity of 0 or 1, I use built-in python functions to quickly return the maximum weight of any day and the total weight of the entire list's items, and these serve as the left and right parameters to a binary search that allow me to find the least valid capacity in O(logN) time.

### 9. Next Permutation

This problem seemed straightfoward when I began, but I kept getting caught up in small errors like my loops being off by one iteration, or my bubble sort starting and ending at the wrong values. Being able to work through all of these helped me build my intuition on loops. In the end, my algorithm was not a very sophisticated one, with a Big O of O(N^2\*2). I would love to revist this problem in the future because I believe that faster methods are possible.

### 10. Linked List Cycle II

After going over in class how to detect cycles in linked lists with Floyd's tortoise and hare algorithm, I wanted to see how I might be able to find an effecient solution to LeetCode 142 as well. LeetCode gave a challenge in the problem description to solve with O(1) memory, so that was my goal with my solution, though it did take O(N^2) time. I used the tortoise and hare algorithm to define a "stop node" that was proven to be somewhere in the loop, and then I ran a nested loop through this linked list where I would break if I got to the stop node twice before seeing my two indexes reference the same node.

After solving this, I found some creative solutions online that worked more effeciently and I tried to learn one algorithm in specific from a solution I found interesting, but I'm pretty happy that I was able to come up with my working solution, even if less efficient.

### 11. Balanced Binary Tree

I started this problem by writing a regular getHeight() function, and then I added my check on each left_height and right_height calculation I did to make sure they were balanced. It took me a lot of thinking to come up with a solution for what to return in that base case, though. I tried adding another parameter called balanced that held a boolean but realized that it would never be read if I only changed it after making my recursive calls.

Finally, I settled on a hacky solution of returning -100 when the tree was out of balance, and then I ended my function by checking whether the result of getBalancedHeight() was greater than 0. This passed all of LeetCode 110's cases and worked in O(N) time, but I wasn't happy with the hacky solution. I went online and saw that a more sophisticated solution just added checks to see if the left and right heights were also -1 before returning -1. I implemented this by only changing a couple lines of code.

### 12. Search 2D Matrix

This was a great problem to help me test my intuition of binary searches and O(log(N)) algorithms. My initial thought was that I could just run two simple binary searches (one to find which row the possible target was in and one to search that row for the target) back-to-back and it would immediately give back my answer, but I realized this problem was a little more complicated. Because the first binary search was targeting a range rather than a specific integer value, the logic was quite a bit different.

My biggest realization while solving this problem was that I could use the `n` value (row length) in order to check the highest value of any given row, instead of just checking the lowest at `0`. This meant that instead of the three outcomes of `==`, `>`, or `<` that I would normally check in a binary search, I should only check `>` for the smallest value of a row, only check `<` for the largest value of a row, and then I would be left with one more outcome that would mean I had found the row that I needed to search.

After getting that first part right, the second step was just implementing a regular binary search on the row.

### 13. Spiral Matrix

This problem was LeetCode 54 and coming up with the algorithm reminded me of some of the techniques that I learned while working on my solution for rotating a matrix a few months ago. I immediately thought to include an offset for each side (top, right, bottom, left) and increment those after looping through them.

The basic structure of my function came quickly, but it took a lot of testing and then retesting in order to get rid of all of my off-by-one errors in the loops. By the time it was working my function got a little messy, so I'd like to clean it up at some point, but I'm happy that it worked.

It's hard to tell the Big O from the code because everything operates within a `while True` loop with a chance to `break` after each step, but the time complexity is O(N) since it will reach every item within every subarray once. The space complexity is also linear because I declare a separate result array, but that is the only thing taking up variable space.

### 14. Word Search

This was LeetCode 79 and I wanted to try it since it had the Depth-First Search tag. The method for solving seemed immediately obvious, and I thought that if I just looped through every item in the matrix until finding one with a value that matched the first item in the target string, I could start a DFS run from there. My intuition was correct, but in order to get this passing all the test cases, I spent a lot of time refining how the algorithm worked. The biggest hold up that took me a while to figure out was when to remove an item from the `current_path` set, but once I finally got that, everything came together.

The time complexity for my algorithm is O(m _ n _ 4^L), if L is the length of the target `word`. This is because I iterate over every item in the board input (making up the O(m \* n)), and then I run the DFS where there are a max of 4 recursive calls to make for each item I explore until I have reached the depth of the target word. Because I use a set for the `current_path`, lookups happen in O(1).

### 15. Word Ladder

This problem was LeetCode 127 and it had the Breadth-First Search tag. My solution was far from the most effecient, but I think I wrote it cleanly and it makes a lot of sense. Rather than working directly in the array that the function takes as an input, I converted the array into a graph. With the graph, I then run a BFS algorithm to find the `endWord`. I store each vertex in a queue that I iterate through for the BFS portion, and I store the vertex in a tuple alongside a `depth` variable that I can use to return at the end.

Because of the nested loop I wrote to turn the array into a graph, the Big O of my script is O(N^2). It may be a cool project in the future to try creating a breadth-first search that runs in an array, and I think something like that may speed this up (though I haven't looked into it). Overall, I'm happy that I was able to create implement several data structures from memory in here, along with the BFS algorithm.
