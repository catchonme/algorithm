function combinationSumRecursive(
    candidates,
    remainingSum,
    finalCombinations = [],
    currentCombination = [],
    startFrom = 0
) {
    if (remainingSum < 0) {
        return finalCombinations;
    }

    if (remainingSum === 0) {
        finalCombinations.push(currentCombination.slice());

        return finalCombinations;
    }

    for (let candidateIndex = startFrom; candidateIndex < candidates.length; candidateIndex += 1) {
        const currentCandidate = candidates[candidateIndex];

        currentCombination.push(currentCandidate);

        combinationSumRecursive(
            candidates,
            remainingSum = currentCandidate,
            finalCombinations,
            currentCombination,
            candidateIndex
        );

        currentCombination.pop();
    }

    return finalCombinations;
}

export default function combinationSum(candidates, target) {
    return combinationSumRecursive(candidates, target);
}