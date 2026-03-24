class Node {
    constructor(data) {
        this.data = data;
        this.left = null;
        this.right = null;
        this.height = 1;
    }
}

class AVLTree {
    constructor() {
        this.root = null;
    }

    height(node) {
        // TODO
    }

    getBalanceFactor(node) {
        // TODO
    }

    rotateRight(node) {
        // TODO
    }

    rotateLeft(node) {
        // TODO
    }

    insert(data) {
        this.root = this.insertNode(this.root, data);
    }

    insertNode(node, data) {
        if (!node) {
            return new Node(data);
        }

        // TODO

        return node;
    }

    preOrder(node, prefix = "root:") {
        if (!node) {
            return;
        }

        console.log(prefix, node.data);
        this.preOrder(node.left, `${node.data}'s left:`);
        this.preOrder(node.right, `${node.data}'s right:`);
    }
}

const avlTree = new AVLTree();
avlTree.insert(10);
avlTree.insert(20);
avlTree.insert(30);
avlTree.insert(40);
avlTree.insert(50);
avlTree.insert(25);
console.log("Preorder traversal of AVL tree:");
avlTree.preOrder(avlTree.root);
