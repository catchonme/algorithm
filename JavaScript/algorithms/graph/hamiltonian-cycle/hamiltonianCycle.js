import GraphVertex from '../../../data-structures/graph/GraphVertex';

function isSafe(adjacencyMatrix, verticesIndices, cycle, vertexCandidate) {
    const endVertex = cycle[cycle.length - 1];

    const candidateVertexAdjacencyIndex = verticesIndices[vertexCandidate.getKey()];
    const endVertexAdjacencyIndex = verticesIndices[endVertex.getKey()];

    if (adjacencyMatrix[endVertexAdjacencyIndex][candidateVertexAdjacencyIndex] === Infinity) {
        return false;
    }

    const candidateDuplicate = cycle.find(vertex => vertex.getKey() === vertexCandidate.getKey());

    return !candidateDuplicate;
}

function isCycle(adjacencyMatrix, verticesIndices, cycle) {
    const startVertex = cycle[0];
    const endVertex = cycle[cycle.length - 1];

    const startVertexAdjacencyIndex = verticesIndices[startVertex.getKey()];
    const endVertexAdjacencyIndex = verticesIndices[endVertex.getKey()];

    return adjacencyMatrix[endVertexAdjacencyIndex][startVertexAdjacencyIndex] !== Infinity;
}

function hamiltonianCycleRecursive({
    adjacencyMatrix,
    vertices,
    verticesIndices,
    cycles,
    cycle
}) {
    const currentCycle = [...cycle].map(vertex => new GraphVertex(vertex.value));

    if (vertices.length === currentCycle.length) {
        if (isCycle(adjacencyMatrix, verticesIndices, currentCycle)) {
            cycles.push(currentCycle);
        }
        return;
    }

    for (let vertexIndex = 0; vertexIndex < vertices.length; vertexIndex += 1) {
        const vertexCandidate = vertices[vertexIndex];

        if (isSafe(adjacencyMatrix, verticesIndices, currentCycle, vertexCandidate)) {
            currentCycle.push(vertexCandidate);

            hamiltonianCycleRecursive({
                adjacencyMatrix,
                vertices,
                verticesIndices,
                cycles,
                cycle: currentCycle
            });

            currentCycle.pop();
        }
    }
}

export default function hamiltonianCycle(graph) {
    const verticesIndices = graph.getVerticesIndices();
    const adjacencyMatrix = graph.getAdjacencyMatrix();
    const vertices = graph.getAllVertices();

    const startVertex = vertices[0];
    const cycles = [];

    const cycle = [startVertex];

    hamiltonianCycleRecursive({
        adjacencyMatrix,
        vertices,
        verticesIndices,
        cycles,
        cycle
    });

    return cycles;
}