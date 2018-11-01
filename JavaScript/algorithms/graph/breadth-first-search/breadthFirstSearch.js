import Queue from '../../../data-structures/queue/Queue';

function initCallbacks(callbacks = {}) {
    const initiatedCallback = callbacks;
    const stubCallback = () => {};

    const allowTraversalCallback = (
        () => {
            const seen = {};
            return ({ nextVertex }) => {
                if (!seen[nextVertex.getKey()]) {
                    seen[nextVertex.getKey()] = true;
                    return true;
                }
                return false;
            }
        }
    )();

    initiatedCallback.allowTraversal = callbacks.allowTraversal || allowTraversalCallback;
    initiatedCallback.enterVertex = callbacks.enterVertex || stubCallback;
    initiatedCallback.leaveVertex = callbacks.leaveVertex || stubCallback;

    return initiatedCallback;
}

export default function breadthFirstSearch(graph, startVertex, originalCallbacks) {
    const callbacks = initCallbacks(originalCallbacks);
    const vertexQueue = new Queue();

    vertexQueue.enqueue(startVertex);

    let previousVertex = null;

    while (!vertexQueue.isEmpty()) {
        const currentVertex = vertexQueue.dequeue();
        callbacks.enterVertex({ currentVertex, previousVertex });

        graph.getNeighbors(currentVertex).forEach((nextVertex) => {
            if (callbacks.allowTraversal({ previousVertex, currentVertex, nextVertex })) {
                vertexQueue.enqueue(nextVertex);
            }
        })

        callbacks.leaveVertex({ currentVertex, previousVertex });

        previousVertex = currentVertex;
    }
}