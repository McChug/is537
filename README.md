# DSA Portfolio

## About

This repo contains a collection of personal projects I have completed (largely in the form of LeetCode problems or similar types of coding challenges.

## Projects

### Generate Parentheses

This project comes from LeetCode #22. I started the project by drawing out all the possible valid combinations of parentheses and trying to figure out any patterns that existed. After way too many drawing and way too much thinking, I decided that I would take a step back and instead make an algorithm that could generate every possible combination of parentheses and only hold on to the good ones. It took some thinking since I've never written a script like this before, but after a nice break from the project it finally clicked with me that since there are only two possible characters, I could treat opening and closing parentheses as if they were ones and zeros and from there generate each combination as if I was just converting decimal to binary. From there I coded my script and just ran into one more issue. I set up my loop as n^2 rather than 2^n, so my code was skipping several valid solutions. After some debugging, that truth finally hit my like a bag of boulders and then I got the code working!
