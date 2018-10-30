export default function permutateWithRepetitions(
    permutationOptions,
    permutationLength = permutationOptions.length
) {
    if (permutationLength === 1) {
        return permutationOptions.map(permutationOption => [permutationOption]);
    }

    const permutations = [];

    permutationOptions.forEach((currentOption) => {
        const smallerPermutations = permutateWithRepetitions(
            permutationOptions,
            permutationLength - 1
        );

        smallerPermutations.forEach((smallerPermutation) => {
            permutations.push([currentOption].concat(smallerPermutation));
        })
    })

    return permutations;
}