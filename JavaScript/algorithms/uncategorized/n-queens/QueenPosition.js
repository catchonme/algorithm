export default class QueenPosition {
    constructor(rowIndex, columnIndex) {
        this.rowIndex = rowIndex;
        this.columnIndex = columnIndex;
    }

    get leftDiagonal() {
        return this.rowIndex - this.columnIndex;
    }

    get rightDiagonal() {
        return this.rowIndex + this.columnIndex;
    }

    toString() {
        return `${this.rowIndex}, ${this.columnIndex}`;
    }
}