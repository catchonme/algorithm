import DisjointSet from '../../../data-structures/disjoint-set/DisjointSet';


export default function detectUndirectedCycleUsingDisjointSet(graph) {
    const keyExtract = graphVertex => graphVertex.getKey();
    const disjointSet = new DisjointSet(keyExtract);
    graph.getAllVertices().forEach(graphVertex => disjointSet.makeSet(graphVertex));

    let cycleFound = false;
    graph.getAllEdges().forEach((graphEdge) => {
        if (disjointSet.inSameSet(graphEdge.startVertex, graphEdge.endVertex)) {
            cycleFound = true;
        } else {
            disjointSet.union(graphEdge.startVertex, graphEdge.endVertex);
        }
    })

    return cycleFound;
}