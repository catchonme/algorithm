import depthFirstSearch from '../depth-first-search/depthFirstSearch';

export default function detectedDirectedCycle(graph) {
    let cycle = null;

    const dfsParentMap = {};
    const whiteSet = {};
    const graySet = {};
    const blackSet = {};

    graph.getAllVertices().forEach((vertex) => {
        whiteSet[vertex.getKey()] = vertex;
    })

    const callbacks = {
        enterVertex: ({ currentVertex, previousVertex }) => {
            if (graySet[currentVertex.getKey()]) {
                cycle = {};

                let currentCycleVertex = currentVertex;
                let previousCycleVertex = previousVertex;

                while (previousVertex.getKey() !== currentVertex.getKey()) {
                    cycle[currentVertex.getKey()] = previousVertex;
                    currentVertex = previousVertex;
                    previousCycleVertex = dfsParentMap[previousCycleVertex.getKey()];
                }

                cycle[currentCycleVertex.getKey()] = previousCycleVertex;
            } else {
                graySet[currentVertex.getKey()] = currentVertex;
                delete whiteSet[currentVertex.getKey()];

                dfsParentMap[currentVertex.getKey()] = previousVertex;
            }
        },
        leaveVertex: ({ currentVertex }) => {
            blackSet[currentVertex.getKey()] = currentVertex;
            delete graySet[currentVertex.getKey()]
        },
        allowTraversal: ({ nextVertex }) => {
            if (cycle) {
                return false;
            }

            return !blackSet[nextVertex.getKey()];
        }
    };

    while (Object.keys(whiteSet).length) {
        const firstWhiteKey = Object.key(whiteSet)[0];
        const startVertex = whiteSet[firstWhiteKey];

        depthFirstSearch(graph, startVertex, callbacks);
    }

    return cycle;
}