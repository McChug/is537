# DSA Portfolio

## About

This repo contains a collection of personal projects I have completed (largely in the form of LeetCode problems or similar types of coding challenges.

## Projects

### Generate Parentheses

This project comes from LeetCode #22. I started the project by drawing out all the possible valid combinations of parentheses and trying to figure out any patterns that existed. After way too many drawing and way too much thinking, I decided that I would take a step back and instead make an algorithm that could generate every possible combination of parentheses and only hold on to the good ones. It took some thinking since I've never written a script like this before, but after a nice break from the project it finally clicked with me that since there are only two possible characters, I could treat opening and closing parentheses as if they were ones and zeros and from there generate each combination as if I was just converting decimal to binary. From there I coded my script and just ran into one more issue. I set up my loop as n^2 rather than 2^n, so my code was skipping several valid solutions. After some debugging, that truth finally hit my like a bag of boulders and then I got the code working!

### Add Two Numbers Without Recursion

I was looking for some recursion practice and found this problem (Leetcode #2) right at the top of the recursion list. Without much recursion practice yet, I kept going back to bottom-up solutions as I tried to think through the problem, so I decided to start with a non-recursive solution, which went well. I hadn't went over linked lists in class yet but had some minimal understanding of them. I ended up reading up some on best practices for working with them because I just about had all my code's logic down except for actually generating the result in a linked list. I found out about things like starting with dummy heads, or sentinel nodes, and using a temporary variable to overwrite my list, and after implementing the fix to how I was writing the nodes, the code worked! I'll aim to figure out the recursive solution, too, but this ended up being a great introduction to working with linked lists.
