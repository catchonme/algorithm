import pascalTriangle from '../../math/pascal-triangle/pascalTriangle'

export default function uniquePaths(width, height) {
    const pascalLine = width + height - 2;
    const pascalLinePosition = Math.min(width, height) - 1;

    return pascalTriangle(pascalLine)[pascalLinePosition];
}