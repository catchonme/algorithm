import MinHeap from '../heap/MinHeap';

export default class PriorityQueue extends MinHeap {
    constructor() {
        super();
        this.priorities = {};
    }

    add(item, priority = 0) {
        this.priorities[item] = priority;
        super.add(item);
        return this;
    }

    remove(item, customFindingComparator) {
        super.remove(item, customFindingComparator);
        delete this.priorities[item];

        return this;
    }

    changePriotity(item, priority) {
        this.remove(item);
        this.add(item, priority);

        return this;
    }

    findByValue(item) {
        return this.find(item);
    }

    hasValue(item) {
        return this.findByValue(item).length > 0;
    }

    comparePriority(a, b) {
        if (this.priorities[a] === this.priorities[b]) {
            return 0;
        }

        return this.priorities[a] < this.priorities[b] ? -1 : 1;
    }

    compareValue(a, b) {
        if (a === b) {
            return 0;
        }

        return a < b ? -1 : 1;
    }
}