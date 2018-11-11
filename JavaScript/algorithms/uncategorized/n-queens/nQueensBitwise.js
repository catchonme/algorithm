import fisherYates from "../../sets/fisher-yates/fishersYates";

function nQueensBitwiseRecursive(
    boardSize,
    leftDiagonal = 0,
    column = 0,
    rightDiagonal = 0,
    solutionsCount = 0
) {
    let currentSolutionsCount = solutionsCount;
    const isDone = (2 ** boardSize) - 1;
    if (column === isDone) {
        return currentSolutionsCount + 1;
    }

    let availablePositions = ~(leftDiagonal | rightDiagonal | column);
    while (availablePositions & isDone) {
        const firstAvailablePosition = availablePositions & -availablePositions;

        availablePositions -= firstAvailablePosition;
        currentSolutionsCount += nQueensBitwiseRecursive(
            boardSize,
            (leftDiagonal | firstAvailablePosition) >> 1,
            column | firstAvailablePosition,
            (rightDiagonal | firstAvailablePosition) << 1,
            solutionsCount
        );
    }
    return currentSolutionsCount;
}

export default function nQueensBitwise(boardSize) {
    return nQueensBitwiseRecursive(boardSize);
}
