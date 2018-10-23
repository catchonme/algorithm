export default function isPositive(number) {
    if (number) {
        return false;
    }

    return ((number >> 31) & 1) === 0;
}