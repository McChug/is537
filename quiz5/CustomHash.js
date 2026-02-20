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

  const uniqueWordsCount = Object.keys(wordCounts).length;

  const capacity = Math.ceil(1.3 * uniqueWordsCount);

  const hashTable = new Array(capacity).fill(null);

  for ([word, count] of Object.entries(wordCounts)) {
    const originalHash = hash(word, capacity);
    const entry = [originalHash, word, count];

    if (!hashTable[originalHash]) {
      hashTable[originalHash] = entry;
    } else {
      let isInserted = false;
      let i = 0;
      while (!isInserted) {
        i += 1;
        let probedHash = originalHash + (i % (capacity - 1));

        if (!hashTable[probedHash]) {
          hashTable[probedHash] = entry;
          isInserted = true;
        }
      }
    }
  }

  // Console Logging
  for (let i = 0; i < hashTable.length && i < 20; i++) {
    console.log(`${i}    ${hashTable[i]}`);
  }

  const lookupWord = "tree";
  console.log(
    `${lookupWord} occurs ${lookup(hashTable, lookupWord, capacity)} times`,
  );
}

function hash(word, capacity) {
  let hash = 0;

  for (let i = 0; i < word.length; i++) {
    hash = (hash << 5) - hash + word.charCodeAt(i);
    hash |= 0;
  }

  return Math.abs(hash) % (capacity - 1);
}

function lookup(hashTable, word, capacity) {
  const originalHash = hash(word, capacity);

  if (hashTable[originalHash][1] === word) {
    return hashTable[originalHash][2];
  } else {
    let isFound = false;
    let i = 0;
    while (!isFound) {
      i += 1;
      let probedHash = originalHash + (i % (capacity - 1));

      if (!hashTable[probedHash]) {
        return null;
      } else if (hashTable[probedHash][1] === word) {
        return hashTable[probedHash][2];
      }
    }
  }
}

const fs = require("fs");
let file = fs.readFileSync("./FirstNephiChapter8.txt", "utf-8");

sortedWordCount(file);
