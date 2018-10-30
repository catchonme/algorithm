function btPowerSetRecursive(originalSet, allSubsets = [[]], currentSubSet = [], startAt = 0) {
    for (let position = startAt; position < originalSet.length; position += 1) {
        currentSubSet.push(originalSet[position]);
        allSubsets.push([...currentSubSet]);
        btPowerSetRecursive(originalSet, allSubsets, currentSubSet, position + 1);
        currentSubSet.pop();
    }

    return allSubsets;
}

export default function btPowerSet(originalSet) {
    return btPowerSetRecursive(originalSet);
}