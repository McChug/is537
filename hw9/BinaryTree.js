class TreeNode {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

function fillTree(node, currentDepth, maxHeight) {
  if (!node) return;

  if (currentDepth < maxHeight) {
    if (!node.left) {
      node.left = new TreeNode("");
    }
    if (!node.right) {
      node.right = new TreeNode("");
    }

    fillTree(node.left, currentDepth + 1, maxHeight);
    fillTree(node.right, currentDepth + 1, maxHeight);
  }
}

function getMaxHeight(node) {
  if (!node) return 0;

  return Math.max(getMaxHeight(node.left), getMaxHeight(node.right)) + 1;
}

function convertToCompleteBinaryTree(root, maxHeight = null) {
  if (!root) return null;

  if (maxHeight === null) {
    maxHeight = getMaxHeight(root);
  }

  fillTree(root, 1, maxHeight);

  return root;
}

function breadthFirstPrettyPrint(root) {
  if (!root) return;

  const maxHeight = getMaxHeight(root);
  convertToCompleteBinaryTree(root, maxHeight);

  const queue = [root];
  let levelHeight = maxHeight;

  while (queue.length > 0) {
    const levelSize = queue.length;
    const levelValues = [];

    for (let i = 0; i < levelSize; i++) {
      const node = queue.shift();
      levelValues.push(node.value);

      if (node.left) queue.push(node.left);
      if (node.right) queue.push(node.right);
    }

    if (levelHeight !== maxHeight) {
      logTreeLevelConnectors([...levelValues], levelHeight);
    }

    logTreeLevelCharacters([...levelValues], levelHeight);

    levelHeight -= 1;
  }
}

function logTreeLevelCharacters(values, height) {
  //   const NODE_CHARS = "☐☐☐";
  const SPACE_CHAR = " ";

  const firstSpacing = 2 ** height - 2;
  const betweenSpacing = 2 ** (height + 1) - 3;

  let line = "";
  line += SPACE_CHAR.repeat(firstSpacing);

  while (values.length > 0) {
    // line += NODE_CHARS;
    const value = values.shift();

    if (value) {
      line += SPACE_CHAR + value + SPACE_CHAR;
    } else {
      line += SPACE_CHAR.repeat(3);
    }

    if (values.length > 0) {
      line += SPACE_CHAR.repeat(betweenSpacing);
    }
  }

  console.log(line);
}

function logTreeLevelConnectors(values, height) {
  const SPACE_CHAR = " ";
  const CHILDREN_LINE_CHAR = "┴";
  const LINE_CHAR = "─";
  const LEFT_END_CHAR = "┌";
  const RIGHT_END_CHAR = "┐";

  const spacing = 2 ** height - 1;

  let line = "";
  line += SPACE_CHAR.repeat(spacing);

  while (values.length > 1) {
    // This condition is for >1 instead of >0 for safety because it shifts two items at a time,
    // though the values queue should always have an even number of elements
    const leftValue = values.shift();
    const rightValue = values.shift();

    // each if...else will generate (spacing * 2 + 3) characters
    if (leftValue && rightValue) {
      line += LEFT_END_CHAR;
      line += LINE_CHAR.repeat(spacing);
      line += CHILDREN_LINE_CHAR;
      line += LINE_CHAR.repeat(spacing);
      line += RIGHT_END_CHAR;
    } else if (leftValue) {
      line += LEFT_END_CHAR;
      line += LINE_CHAR.repeat(spacing);
      line += CHILDREN_LINE_CHAR;
      line += SPACE_CHAR.repeat(spacing + 1);
    } else if (rightValue) {
      line += SPACE_CHAR.repeat(spacing + 1);
      line += CHILDREN_LINE_CHAR;
      line += LINE_CHAR.repeat(spacing);
      line += RIGHT_END_CHAR;
    } else {
      line += SPACE_CHAR.repeat(spacing * 2 + 3);
    }

    if (values.length > 0) {
      line += SPACE_CHAR.repeat(spacing * 2 + 1);
    }
  }

  console.log(line);
}

const n1 = new TreeNode("m");
const n2 = new TreeNode("f");
const n3 = new TreeNode("a");
const n4 = new TreeNode("z");
const n5 = new TreeNode("k");
const n6 = new TreeNode("b");
const n7 = new TreeNode("q");
const n8 = new TreeNode("r");
const n9 = new TreeNode("t");
const n10 = new TreeNode("w");
const n11 = new TreeNode("h");
const n12 = new TreeNode("i");
const n13 = new TreeNode("l");
const n14 = new TreeNode("e");
n1.left = n2;
n1.right = n4;
n2.left = n3;
n2.right = n5;
n4.left = n6;
n4.right = n7;
n3.left = n8;
n3.right = n9;
n5.left = n10;
n6.right = n13;
n10.left = n11;
n10.right = n12;
n12.left = n14;

breadthFirstPrettyPrint(n1);
