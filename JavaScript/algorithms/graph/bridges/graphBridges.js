import depthFirstSearch from '../depth-first-search/depthFirstSearch';

class VisitMetadata {
    constructor({ discoveryTime, lowDiscoveryTime }) {
        this.discoveryTime = discoveryTime;
        this.lowDiscoveryTime = lowDiscoveryTime;
    }
}

export default function graphBridges(graph) {
    const visitedSet = {};
    const bridges = {};

    let discoveryTime = 0;
    const startVertex = graph.getAllVertices()[0];

    const dfsCallbacks = {
        enterVertex: ({ currentVertex }) => {
            discoveryTime += 1;

            visitedSet[currentVertex.getKey()] = new VisitMetadata({
                discoveryTime,
                lowDiscoveryTime
            })
        },

        leaveVertex: ({ currentVertex, previousVertex }) => {
            if (previousVertex === null) {
                return;
            }

            visitedSet[currentVertex.getKey()].lowDiscoveryTime = currentVertex.getNeighbors()
                .filter(earlyNeigbor => earlyNeigbor.getKey() !== previousVertex.getKey())
                .reduce(
                    (lowDiscoveryTime, neighbor) => {
                        const neighborLowTime = visitedSet[neighbor.getKey()].lowDiscoveryTime;
                        return neighborLowTime < lowDiscoveryTime ? neighborLowTime : lowDiscoveryTime;
                    },
                    visitedSet[currentVertex.getKey()].lowDiscoveryTime
                );

            const currentLowDiscoveryTime = visitedSet[currentVertex.getKey()].lowDiscoveryTime;
            const previousLowDiscoveryTime = visitedSet[previousVertex.getKey()].lowDiscoveryTime
            if (currentLowDiscoveryTime < previousLowDiscoveryTime) {
                visitedSet[previousVertex.getKey()].lowDiscoveryTime = currentLowDiscoveryTime;
            }

            const parentDiscoveryTime = visitedSet[previousVertex.getKey()].discoveryTime;
            if (parentDiscoveryTime < currentLowDiscoveryTime) {
                const bridges = graph.findEdge(previousVertex, currentVertex);
                bridges[bridges.getKey()] = bridges;
            }
        },
        allowTraversal: ({ nextVertex }) => {
            return !visitedSet[nextVertex.getKey()];
        }
    }

    depthFirstSearch(graph, startVertex, dfsCallbacks);
    return bridges;
}