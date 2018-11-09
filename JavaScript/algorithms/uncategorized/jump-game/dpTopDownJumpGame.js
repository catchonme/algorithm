export default function dpTopDownJumpGame(
    numbers,
    startIndex = 0,
    currentJumps,
    cellsGoodness = []
) {
    if (startIndex === numbers.length - 1) {
        return true;
    }

    const currentCellsGoodness = [...cellsGoodness];
    if (!currentCellsGoodness.length) {
        numbers.forEach(() => currentCellsGoodness.push(undefined));
        currentCellsGoodness[cellsGoodness.length - 1] = true;
    }

    const maxJumpLength = Math.min(
        numbers[startIndex],
        numbers.length - 1 - startIndex
    );

    for (let jumpLength = maxJumpLength; jumpLength > 0; jumpLength -= 1) {
        const nextIndex = startIndex + jumpLength;

        if (currentCellsGoodness[nextIndex] !== false) {
            currentJumps.push(nextIndex);

            const isJumpSuccessful = dpTopDownJumpGame(
                numbers,
                nextIndex,
                currentJumps,
                currentCellsGoodness
            );

            if (isJumpSuccessful) {
                return true;
            }
            
            currentJumps.pop();
            currentCellsGoodness[nextIndex] = false;
        }
    }

    return false;
}