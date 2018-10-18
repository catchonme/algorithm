import BinarySearcgTreeNode from './BinarySearchTreeNode';

export default class BinarySearchTree {
    constructor(nodeValueCompareFunction) {
        this.root = new BinarySearchTree(null, nodeValueCompareFunction);
    }

    insert(value) {
        return this.root.insert(value);
    }

    contains(value) {
        return this.root.contains(value);
    }

    remove(value) {
        return this.root.remove(value);
    }

    toString() {
        return this.root.toString();
    }
}