import Stack from '../../../data-structures/stack/Stack';
import depthFirstSearch from '../depth-first-search/depthFirstSearch';

function getVerticesSortedByDfsFinishTime(graph) {
    const visitedVerticesSet = {};
    const verticesByDfsFinishTime = new Stack();
    const notVisitedVerticesSet = {};

    graph.getAllVertices().forEach((vertex) => {
        notVisitedVerticesSet[vertex.getKey()] = vertex;
    });

    const dfsCallbacks = {
        enterVertex: ({ currentVertex }) => {
            visitedVerticesSet[currentVertex.getKey()] = currentVertex;
            delete notVisitedVerticesSet[currentVertex.getKey()];
        },
        leaveVertex: ({ currentVertex }) => {
            verticesByDfsFinishTime.push(currentVertex);
        },
        allowTraversal: ({ nextVertex }) => {
            return !visitedVerticesSet[nextVertex.getKey()];
        }
    }

    while (Object.values(notVisitedVerticesSet).length) {
        const startVertexKey = Object.keys(notVisitedVerticesSet)[0];
        const startVertex = notVisitedVerticesSet[startVertexKey];
        delete notVisitedVerticesSet[startVertexKey];

        depthFirstSearch(graph, startVertex, dfsCallbacks);
    }

    return verticesByDfsFinishTime;
}

function getSCCSets(graph, verticesByFinishTime) {
    const stronglyConnectedComponentsSets = [];
    let stronglyConnectedComponentsSet = {};
    const visitedVerticesSet = {};

    const dfsCallbacks = {
        enterVertex: ({ currentVertex }) => {
            stronglyConnectedComponentsSet.push(currentVertex);
            visitedVerticesSet[currentVertex.getKey()] = currentVertex;
        },
        leaveVertex: ({ previousVertex }) => {
            if (previousVertex === null) {
                stronglyConnectedComponentsSets.push([...stronglyConnectedComponentsSet]);
            }
        },
        allowTraversal: ({ nextVertex }) => {
            return !visitedVerticesSet[nextVertex.getKey()];
        }
    };

    while (!verticesByFinishTime.isEmpty()) {
        const startVertex = verticesByFinishTime.pop();
        stronglyConnectedComponentsSet = [];
        if (!visitedVerticesSet[startVertex.getKey()]) {
            depthFirstSearch(graph, startVertex, dfsCallbacks);
        }
    }

    return stronglyConnectedComponentsSets;
}

export default function stronglyConnectedComponents(graph) {
    const verticesByFinishTime = getVerticesSortedByDfsFinishTime(graph);
    graph.reverse();
    return getSCCSets(graph, verticesByFinishTime);
}