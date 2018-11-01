import depthFirstSeatch from '../depth-first-search/depthFirstSearch';

class VisitMetadata {
    constructor({ discoveryTime, lowDiscoveryTime }) {
        this.discoveryTime = discoveryTime;
        this.lowDiscoveryTime = lowDiscoveryTime;

        this.independentChildrenCount = 0;
    }
}

export default function articulationPoints(graph) {
    const visitedSet = {};

    const articulationPointsSet = {};

    let discoveryTime = 0;

    const startVertex = graph.getAllVertices()[0];

    const dfsCallbacks = {
        enterVertex: ({ currentVertex, previousVertex }) => {
            discoveryTime += 1;

            visitedSet[currentVertex.getKey()] = new VisitMetadata({
                discoveryTime,
                lowDiscoveryTime: discoveryTime
            })

            if (previousVertex) {
                visitedSet[previousVertex.getKey()].independentChildrenCount += 1;
            }
        },

        leaveVertex: ({ currentVertex, previousVertex }) => {
            if (previousVertex === null) {
                return;
            }

            visitedSet[currentVertex.getKey()].lowDiscoveryTime = currentVertex.getNeighbors()
                .filter(earlyNeighbor => earlyNeighbor.getKey() !== previousVertex.getKey())
                .reduce(
                    (lowestDiscoveryTime, neighbor) => {
                        const neighborLowTime = visitedSet[neighbor.getKey()].lowDiscoveryTime;
                        return neighborLowTime < lowestDiscoveryTime ? neighborLowTime : lowestDiscoveryTime;
                    },
                    visitedSet[currentVertex.getKey()].lowDiscoveryTime,
                );

            if (previousVertex === startVertex) {
                if (visitedSet[previousVertex.getKey()].independentChildrenCount >= 2) {
                    articulationPointsSet[previousVertex.getKey()] = previousVertex;
                }
            } else {
                const currentLowDiscoveryTime = visitedSet[currentVertex.getKey()].lowDiscoveryTime;
                const parentDiscoveryTime = visitedSet[previousVertex.getKey()].lowDiscoveryTime;

                if (parentDiscoveryTime <= currentLowDiscoveryTime) {
                    articulationPointsSet[previousVertex.getKey()] = previousVertex;
                }
            }
        },
        allowTraversal: ({ nextVertex }) => {
            return !visitedSet[nextVertex.getKey()];
        }
    };

    depthFirstSeatch(graph, startVertex, dfsCallbacks);

    return articulationPointsSet;
}