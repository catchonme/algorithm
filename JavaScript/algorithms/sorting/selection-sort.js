import Sort from './Sort';

export default class SelectionSort extends Sort {
    sort(originalArray) {
        const array = [...originalArray];

        for (let i = 0; i < array.length - 1; i += 1) {
            let minIndex = i;

            this.callbacks.visitingCallback(array[i]);

            for (let j = i + 1; j < array.length; j += 1) {
                this.callbacks.visitingCallback(array[j]);

                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }

            if (minIndex != i) {
                [array[i], array[minIndex]] = [array[minIndex], array[i]];
            }
        }

        return array;
    }
}