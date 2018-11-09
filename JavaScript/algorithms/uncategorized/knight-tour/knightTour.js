function getPossibleMoves(chessboard, position) {
    const possibleMoves = [
        [position[0] - 1, position[1] - 2],
        [position[0] - 2, position[1] - 1],
        [position[0] + 1, position[1] - 2],
        [position[0] + 2, position[1] - 1],
        [position[0] - 2, position[1] + 1],
        [position[0] - 1, position[1] + 2],
        [position[0] + 1, position[1] + 2],
        [position[0] + 2, position[1] + 1],
    ];

    return possibleMoves.filter((move) => {
        const boardSize = chessboard.length;
        return move[0] >= 0 && move[1] >= 0 && move[0] < boardSize && move[1] < boardSize;
    });

    function isMoveAllowed(chessboard, move) {
        return chessboard[move[0]][move[1]] !== 1;
    }

    function isBoardCompletelyVisited(chessboard, moves) {
        const totalPossibleMovesCount = chessboard.length ** 2;
        const existingMovesCount = moves.length;

        return totalPossibleMovesCount === existingMovesCount;
    }

    function knightTourRecursive(chessboard, moves) {
        const currentChessboard = chessboard;
        if (isBoardCompletelyVisited(currentChessboard, moves)) {
            return true;
        }

        const lastMove = moves[moves.length - 1];
        const possibleMoves = getPossibleMoves(currentChessboard, lastMove);

        for (let moveIndex = 0; moveIndex < possibleMoves.length; moveIndex += 1) {
            const currentMove = possibleMoves[moveIndex];

            if (isMoveAllowed(currentChessboard, currentMove)) {
                moves.push(currentMove);
                currentChessboard[currentMove[0]][currentMove[1]] = 1;

                if (knightTourRecursive(currentChessboard, moves)) {
                    return true;
                }

                moves.pop();
                currentChessboard[currentMove[0]][currentMove[1]] = 0;
            }
        }

        return false;
    }
}