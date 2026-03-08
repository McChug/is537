class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedList {
    constructor(head) {
        this.head = head;
    }

    delete(index) {
        if (!this.head) {
            return;
        }

        if (index <= 0) {
            this.head = this.head.next;
            return;
        }

        let currentNode = this.head;
        let previousNode = null;

        while (currentNode && index > 0) {
            previousNode = currentNode;
            currentNode = currentNode.next;
            index -= 1;
        }

        previousNode.next = currentNode.next;
    }

    insert(index, node) {
        if (!this.head) {
            this.head = node;
            return;
        }

        let currentNode = this.head;
        let previousNode = null;

        while (currentNode && index > 0) {
            previousNode = currentNode;
            currentNode = currentNode.next;
            index -= 1;
        }

        node.next = currentNode;

        if (previousNode) {
            previousNode.next = node;
        } else {
            this.head = node;
        }
    }

    prepend(node) {
        node.next = this.head;
        this.head = node;
    }

    read(index) {
        let currentNode = this.head;

        while (currentNode && index > 0) {
            currentNode = currentNode.next;
            index -= 1;
        }

        return currentNode ?? null;
    }

    search(value) {
        if (!this.head) {
            return null;
        }

        let currentNode = this.head;

        while (currentNode) {
            if (currentNode.value === value) {
                return currentNode;
            }

            currentNode = currentNode.next;
        }

        return null;
    }
}

const node1 = new Node("wow");
const node2 = new Node("this");
const node3 = new Node("is");
const node4 = new Node("cool");
const node5 = new Node("!");

console.log(node1, node2, node3, node4, node5);

const list = new LinkedList(null);

list.insert(0, node1);
console.log(list);
list.insert(0, node2);
console.log(list);
[node3, node4, node5].forEach((node) => {
    list.insert(1, node);
});
console.log(JSON.stringify(list, ["head", "value", "next"], 2));
console.log(list.read(4));
console.log(list.search("!"));
list.delete(3);
console.log(JSON.stringify(list, ["head", "value", "next"], 2));
