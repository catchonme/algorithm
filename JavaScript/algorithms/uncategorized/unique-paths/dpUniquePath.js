export default function dpUniquePaths(width, height) {
    const board = Array(height).fill(null).map(() => {
        return Array(width).fill(0)
    })

    for (let rowIndex = 0; rowIndex < height; rowIndex += 1) {
        for (let columnIndex = 0; columnIndex < width; columnIndex += 1) {
            if (rowIndex === 0 || columnIndex === 0) {
                board[rowIndex][columnIndex] = 1;
            }
        }
    }

    for (let rowIndex = 1; rowIndex < height; rowIndex += 1) {
        for (let columnIndex = 1; columnIndex < width; columnIndex += 1) {
            const uniquesFromTop = board[rowIndex - 1][columnIndex];
            const uniquesFromLeft = board[rowIndex][columnIndex - 1];
            board[rowIndex][columnIndex] = uniquesFromTop+ uniquesFromLeft;
        }
    }

    return board[height - 1][width - 1];
}