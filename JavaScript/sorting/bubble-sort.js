

class BubbleSort {
    sort(originalArray) {
        const array = [...originalArray];

        for (let i = 1; i < array.length; i += 1) {
            for (let j = 0; j < array.length - i; j += 1) {
                if (array[j + 1] < array[j]) {
                    const tmp = array[j + 1];
                    array[j + 1] = array[j];
                    array[j] = tmp;
                }
            }
        }

        return array;
    }
}


let arrayInput = [2, 3, 1, 4]
sol = new BubbleSort()
result = sol.sort(arrayInput)
console.log(result)