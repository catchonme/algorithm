import PolynomialHash from '../../cryptography/polynomial-hash/PolynomialHash';

export default function raginKarp(text, word) {
    const hasher = new PolynomialHash();

    const wordHash = hasher.hash(word);

    let prevFrame = null;
    let currentFrameHash = null;

    for (let charIndex = 0; charIndex <= (text.length - word.length); charIndex += 1) {
        const currentFrame = text.substring(charIndex, charIndex + word.length);

        if (currentFrame === null) {
            currentFrameHash = hasher.hash(currentFrame);
        } else {
            currentFrameHash = hasher.roll(currentFrameHash, prevFrame, currentFrame);
        }

        prevFrame = currentFrame;

        if (
            wordHash === currentFrameHash
            && text.substr(charIndex, word.length) === word
        ) {
            return charIndex;
        }
    }

    return -1;
}