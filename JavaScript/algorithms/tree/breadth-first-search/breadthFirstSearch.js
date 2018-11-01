import Queue from '../../../data-structures/queue/Queue';

function initCallbacks(callbacks = {}) {
    const initiatedCallback = callbacks;

    const stubCallback = () => {};
    const defaultAllowTraversal = () => true;

    initiatedCallback.allowTraversal = callbacks.allowTraversal || defaultAllowTraversal;
    initiatedCallback.enterNode = callbacks.enterNode || stubCallback;
    initiatedCallback.leaveNode = callbacks.leaveNode || stubCallback;

    return initiatedCallback;
}

export default function breadthFirstSearch(rootNode, originalCallbacks) {
    const callbacks = initCallbacks(originalCallbacks);
    const nodeQueue = new Queue();

    nodeQueue.enqueue(rootNode);

    while (!nodeQueue.isEmpty()) {
        const currentNode = nodeQueue.dequeue();

        callbacks.enterNode(currentNode);

        if (currentNode.left && callbacks.allowTraversal(currentNode, currentNode.left)) {
            nodeQueue.enqueue(currentNode.left);
        }

        if (currentNode.right && callbacks.allowTraversal(currentNode, currentNode.right)) {
            nodeQueue.enqueue(currentNode.right);
        }

        callbacks.leaveNode(currentNode);
    }
}