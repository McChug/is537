# DSA Portfolio

## About

This repo contains a collection of personal projects I have completed (largely in the form of LeetCode problems or similar types of coding challenges.

## Projects

### Valid Sudoku

My first project for this class ended up being a lot more difficult than I thought, but it was a lot of fun to think through! I figured that if a went for an algorithm with a space complexity of O(N), then I could make the time complexity O(N) as well. (Or O(N^2) for each of these depending on if you consider N to be 9 or 9x9).

By storing what already exists in each column, row, and subgrid, I could just loop through each cell of the board and make sure there were no collisions, so I initialized three arrays that could present each of these conditions to check and I pushed 9 sets into each. I also removed row sets after each loop to take back some space. Although figuring out how to put cells into their respective column and row sets was easy, coming up with what defined a subgrid was not! I diagrammed a sudoku board in Excel and started looking through what would need to happen to satisfy the condition. After writing down lots of numbers and looking for patterns, the equation finally clicked and I was able to set the variable `s` in my code which made the script come together!

Also, as a side note, it was important to me to make an algorithm that could work with any size board, as long as the length and width were the same and could be square rooted. This was just for fun since I didn't want to hard-code 9's, and I'm happy with how it turned out!

### Rotate Image

When I started on this algorithm, it looked a whole lot like a sudoku board to me, and since I had just spent so much time and mental energy trying to come up with all the patterns and sequences I could on these boards, I thought that I would be able to solve this problem intuitively. I was very wrong.

I originally intialized my two for loops with variables named i and j, and my code looked fairly similar to what I ended up with, but I couldn't keep everything in my head in order to define all the switching I had to do. Eventually, it occured to me to switch the name of my first index to `front`, and I also renamed my length variable to `end`, which started to help me conceptually pick up on what my code was meant to do better. Things still weren't quite right until I renamed my inner loop's index to `offset`, and at that point I was finally able to write out in code the ideas that I had in my head and actually keep track of what it was doing.

I was pleased to see after the fact that these names are used in solutions posted online. It really was in coming up with these names that I could finally see the pattern that could perform a rotation not just on a 3x3 grid, but also a 4x4 and 5x5 and on.

### Generate Parentheses

This project comes from LeetCode #22. I started the project by drawing out all the possible valid combinations of parentheses and trying to figure out any patterns that existed. After way too many drawing and way too much thinking, I decided that I would take a step back and instead make an algorithm that could generate every possible combination of parentheses and only hold on to the good ones. It took some thinking since I've never written a script like this before, but after a nice break from the project it finally clicked with me that since there are only two possible characters, I could treat opening and closing parentheses as if they were ones and zeros and from there generate each combination as if I was just converting decimal to binary. From there I coded my script and just ran into one more issue. I set up my loop as n^2 rather than 2^n, so my code was skipping several valid solutions. After some debugging, that truth finally hit my like a bag of boulders and then I got the code working!

This was an incredibly satisying problem to finally solve, and a lot of fun to work on throughout.

### Add Two Numbers Without Recursion

I was looking for some recursion practice and found this problem (Leetcode #2) right at the top of the recursion list. Without much recursion practice yet, I kept going back to bottom-up solutions as I tried to think through the problem, so I decided to start with a non-recursive solution, which went well. I hadn't went over linked lists in class yet but had some minimal understanding of them. I ended up reading up some on best practices for working with them because I just about had all my code's logic down except for actually generating the result in a linked list. I found out about things like starting with dummy heads, or sentinel nodes, and using a temporary variable to overwrite my list, and after implementing the fix to how I was writing the nodes, the code worked! I'll aim to figure out the recursive solution, too, but this ended up being a great introduction to working with linked lists.

As far as the adding logic went for this algorithm, I just kept a running carry bit of sorts that would change to a 0 or 1 after each sum was calculated. It seemed intuitive and the effeciency ended up great so this script ran in O(N) time.
