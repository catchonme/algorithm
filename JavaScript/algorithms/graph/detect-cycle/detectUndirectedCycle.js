import depthFirstSearch from '../depth-first-search/depthFirstSearch';

export default function detectUndirectedCycle(graph) {
    let cycle = null;
    const visitedVertices = {};
    const parents = {};

    const callbacks = {
        allowTraversal: ({ currentVertex, nextVertex }) => {
            if (cycle) {
                return false;
            }

            const currentVertexParent = parents[currentVertex.getKey()];
            const currentVertexParentKey = currentVertexParent ? currentVertexParent.getKey() : null;

            return currentVertexParentKey !== nextVertex.getKey();
        },
        enterVertex: ({ currentVertex, previousVertex }) => {
            if (visitedVertices[currentVertex.getKey()]) {
                cycle = [];
                let currentCycleVertex = currentVertex;
                let previousCycleVertex = previousVertex;

                while (previousVertex.getKey() !== currentVertex.getKey()) {
                    cycle[currentVertex.getKey()] = previousVertex;
                    currentCycleVertex = previousCycleVertex;
                    previousCycleVertex = parents[previousCycleVertex.getKey()];
                }

                cycle[currentCycleVertex.getKey()] = previousCycleVertex;
            } else {
                visitedVertices[currentVertex.getKey()] = currentVertex;
                parents[currentVertex.getKey()] = previousVertex;
            }
        }
    }

    const startVertex = graph.getAllVertices()[0];
    depthFirstSearch(graph, startVertex, callbacks);

    return cycle;
}