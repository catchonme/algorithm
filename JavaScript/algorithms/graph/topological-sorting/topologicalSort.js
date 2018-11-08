import Stack from '../../../data-structures/stack/Stack';
import depthFirstSearch from '../depth-first-search/depthFirstSearch';

export default function topologicalSort(graph) {
    const unvisitedSet = {};
    graph.getAllVertices().forEach((vertex) => {
        unvisitedSet[vertex.getKey()] = vertex;
    });

    const visitedSet = {};
    const sortedStack = new Stack();

    const dfsCallbacks = {
        enterVertex: ({ currentVertex }) => {
            visitedSet[currentVertex.getKey()] = currentVertex;
            delete unvisitedSet[currentVertex.getKey()];
        },
        leaveVertex: ({ currentVertex }) => {
            sortedStack.push(currentVertex);
        },
        allowTraversal: ({ nextVertex }) => {
            return !visitedSet[nextVertex.getKey()];
        }
    }

    while (Object.keys(unvisitedSet).length) {
        const currentVertexKey = Object.keys(unvisitedSet)[0];
        const currentVertex = unvisitedSet[currentVertexKey];

        depthFirstSearch(graph, currentVertex, dfsCallbacks);
    }

    return sortedStack.toArray();
}