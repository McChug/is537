// The overall big O of my code is O(N^2*2N)
// My code begins with an O(N) operation to loop through every character
// in the text file and add them to an object.
// That object is then turned into an Array, which is another O(N) operation.
// The array is then looped through with a bubble sort, which is O(N^2).
// This buble sort also hash a nested sort within it, but I only check the
// the first letter of each word to sort, so the nested sort is O(1).
// Logging after that is another O(N), but not counted for this assignment.
function sortedWordCount(file) {
  let wordCounts = {};
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

  wordCounts = Object.entries(wordCounts);

  for (let i = 0; i < wordCounts.length; i++) {
    const iWord = wordCounts[i][0];
    const iCount = wordCounts[i][1];

    for (let j = 0; j < wordCounts.length; j++) {
      const jWord = wordCounts[j][0];
      const jCount = wordCounts[j][1];

      if (jCount < iCount) {
        let tmp = wordCounts[i];
        wordCounts[i] = wordCounts[j];
        wordCounts[j] = tmp;
      } else if (jCount === iCount) {
        if (iWord[0] < jWord[0]) {
          let tmp = wordCounts[i];
          wordCounts[i] = wordCounts[j];
          wordCounts[j] = tmp;
        }
      }
    }
  }

  // Console Logging
  for (const [word, count] of wordCounts) {
    console.log(`${word}    ${count}`);
  }
}

const fs = require("fs");
let file = fs.readFileSync("./FirstNephiChapter8.txt", "utf-8");

sortedWordCount(file);
