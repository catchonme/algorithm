export default function jumpSearch(sortedArray, seekElement) {
    const arraySize = sortedArray.length;

    if (!arraySize) {
        return -1;
    }

    const jumpSize = Math.floor(Math.sqrt(arraySize));

    let blockStart = 0;
    let blockEnd = jumpSize;
    while (seekElement >= sortedArray[Math.min(blockEnd, arraySize) - 1]) {
        blockStart = blockEnd;
        blockEnd += jumpSize;

        if (blockStart > arraySize) {
            return -1;
        }
    }

    let currentIndex = blockStart;
    while (currentIndex < Math.min(blockEnd, arraySize)) {
        if (sortedArray[currentIndex] === seekElement) {
            return currentIndex;
        }

        currentIndex += 1;
    }
    return -1;
}
