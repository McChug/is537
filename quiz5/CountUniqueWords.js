function countUniqueWords(file) {
  // This code runs in O(N) time.
  // It runs a loop through each character in the file and on each one,
  // a regex check is performed to see if it is a letter a-z or A-Z (capital).
  // I don't know the cost of a regex check, though a quick google search leads
  // me to believe a simple check is not costly.
  // All other steps are either quick if-statements or O(1) operations like appending
  // to the end of a string or writing to or editting an object (hash table).

  const wordCounts = {};
  currentWord = "";

  for (const char of file) {
    if (/[a-zA-Z]/i.test(char)) {
      const letter = char.toLowerCase();
      currentWord += letter;
    } else if (currentWord !== "") {
      if (currentWord in wordCounts) {
        wordCounts[currentWord] += 1;
      } else {
        wordCounts[currentWord] = 1;
      }

      currentWord = "";
    }
  }

  // Console Logging
  for ([word, count] of Object.entries(wordCounts)) {
    console.log(`${word} ${count}`);
  }
}

const fs = require("fs");
let file = fs.readFileSync("./FirstNephiChapter8.txt", "utf-8");

countUniqueWords(file);
