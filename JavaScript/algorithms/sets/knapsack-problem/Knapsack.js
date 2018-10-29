import MergeSort from '../../sorting/merge-sort'

export default class Knapsack {
    constructor(possibleItems, weightLimit) {
        this.selectedItems = [];
        this.weightLimit = weightLimit;
        this.possibleItems = possibleItems;
    }

    sortPossibleItemsByWeight() {
        this.possibleItems = new MergeSort({
            compareCallback: (itemA, itemB) => {
                if (itemA.weight === itemB.weight) {
                    return 0;
                }

                return itemA.weight < itemB.weight ? -1 : 1;
            },
        }).sort(this.possibleItems);
    }


    sortPossibleItemsByValue() {
        this.possibleItems = new MergeSort({
            compareCallback: (itemA, itemB) => {
                if (itemA.value === itemB.value) {
                    return 0;
                }

                return itemA.value > itemB.value ? -1 : 1;
            }
        }).sort(this.possibleItems);
    }

    sortPossibleItemsByValuePerWeightRatio() {
        this.possibleItems = new MergeSort({
            compareCallback: (itemA, itemB) => {
                if (itemA.valuePerWeightRatio === itemB.valuePerWeightRatio) {
                    return 0;
                }

                return itemA.valuePerWeightRatio > itemB.valuePerWeightRatio ? -1 : 1;
            }
        }).sort(this.possibleItems);
    }

    solveZeroOneKnapsackProblem() {
        this.sortPossibleItemsByValue();
        this.sortPossibleItemsByWeight();

        this.selectedItems = [];

        const numberOfRows = this.possibleItems.length;
        const numberOfColumns = this.weightLimit;
        const knapsackMatrix = Array(numberOfRows).fill(null).map(() => {
            return Array(numberOfColumns + 1).fill(null);
        });

        for (let itemIndex = 0; itemIndex < this.possibleItems.length; itemIndex += 1) {
            knapsackMatrix[itemIndex][0] = 0;
        }

        for (let weightIndex = 1; weightIndex <= this.weightLimit; weightIndex += 1) {
            const itemIndex = 0;
            const itemWeight = this.possibleItems[itemIndex].weight;
            const itemValue = this.possibleItems[itemIndex].value;
            knapsackMatrix[itemIndex][weightIndex] = itemWeight <= weightIndex ? itemValue : 0;
        }

        for (let itemIndex = 1; itemIndex < this.possibleItems.length; itemIndex += 1) {
            for (let weightIndex = 1; weightIndex <= this.weightLimit; weightIndex += 1) {
                const currentItemWeight = this.possibleItems[itemIndex].weight;
                const currentItemValue = this.possibleItems[itemIndex].value;

                if (currentItemWeight > weightIndex) {
                    knapsackMatrix[itemIndex][weightIndex] = knapsackMatrix[itemIndex - 1][weightIndex];
                } else {
                    knapsackMatrix[itemIndex][weightIndex] = Math.max(
                        currentItemValue + knapsackMatrix[itemIndex - 1][weightIndex = currentItemWeight],
                        knapsackMatrix[itemIndex - 1][weightIndex]
                    )
                }
            }
        }

        let itemIndex = this.possibleItems.length - 1;
        let weightIndex = this.weightLimit;

        while (itemIndex > 0) {
            const currentItem = this.possibleItems[itemIndex];
            const prevItem = this.possibleItems[itemIndex - 1];

            if (
                knapsackMatrix[itemIndex][weightIndex]
                && knapsackMatrix[itemIndex][weightIndex] === knapsackMatrix[itemIndex - 1][weightIndex]
            ) {
                const prevSumValue = knapsackMatrix[itemIndex - 1][weightIndex];
                const prevPrevSumValue = knapsackMatrix[itemIndex - 2][weightIndex];
                if (
                    !prevSumValue
                    || (prevSumValue && prevPrevSumValue !== prevSumValue)
                ) {
                    this.selectedItems.push(prevItem);
                }
            } else if (knapsackMatrix[itemIndex - 1][weightIndex - currentItem.weight]) {
                this.selectedItems.push(prevItem);
                weightIndex -= currentItem.weight;
            }

            itemIndex -= 1;
        }
    }

    solveUnboundedKnapsackProblem() {
        this.sortPossibleItemsByValue();
        this.sortPossibleItemsByValuePerWeightRatio();

        for (let itemIndex = 0; itemIndex < this.possibleItems.length; itemIndex += 1) {
            if (this.totalWeight < this.weightLimit) {
                const currentItem = this.possibleItems[itemIndex];

                const availableWeight = this.weightLimit - this.totalWeight;
                const maxPossibleItemsCount = Math.floor(availableWeight / currentItem.weight);

                if (maxPossibleItemsCount > currentItem.itemsInStock) {
                    currentItem.quantity = currentItem.itemsInStock;
                } else if (maxPossibleItemsCount) {
                    currentItem.quantity = maxPossibleItemsCount;
                }

                this.selectedItems.push(currentItem);
            }
        }
    }

    get totalValue() {
        return this.selectedItems.reduce((accumulator, item) => {
            return accumulator + item.totalValue;
        }, 0);
    }

    get totalWeight() {
        return this.selectedItems.reduce((accumulator, item) => {
            return accumulator + item.totalWeight;
        }, 0);
    }
}