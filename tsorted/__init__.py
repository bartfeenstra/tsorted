from typing import Iterable, Tuple, Dict, Hashable, Set

from orderedset import OrderedSet

Vertex = Hashable
Edge = Tuple[Vertex, Vertex]
Graph = Dict[Vertex, Set[Vertex]]


class GraphError(BaseException):
    pass  # pragma: no cover


class CyclicGraphError(GraphError):
    pass  # pragma: no cover


def tsorted(graph: Graph) -> OrderedSet:
    """
    Sort a graph topologically.

    This function uses the algorithm described by Kahn (1962).

    Returns
    -------
    OrderedSet[Vertex]
    """
    edges = set(_graph_to_edges(graph))
    sorted_vertices = OrderedSet()
    outdegree_vertices = {edge[0] for edge in edges if not _is_target(edge[0], edges)}
    while outdegree_vertices:
        outdegree_vertex = outdegree_vertices.pop()
        sorted_vertices.add(outdegree_vertex)
        outdegree_vertex_edges = {edge for edge in edges if edge[0] == outdegree_vertex}
        for edge in outdegree_vertex_edges:
            edges.remove(edge)
            if not _is_target(edge[1], edges):
                outdegree_vertices.add(edge[1])
    if edges:
        raise CyclicGraphError
    isolated_vertices = set(graph.keys() - sorted_vertices)
    return sorted_vertices | isolated_vertices


def tsorted_grouped(graph: Graph) -> OrderedSet:
    """
    Sort a graph topologically.

    This function uses the algorithm described by Kahn (1962), with the following additional properties:
    - Optimized for concurrent processing: each item of the returned first-level OrderedSet is a second-level set of
      vertices that can be processed concurrently.

    Returns
    -------
    OrderedSet[Set[Vertex]]
    """
    edges = set(_graph_to_edges(graph))
    sorted_vertices = set()
    sorted_vertex_groups = OrderedSet()
    upcoming_outdegree_vertices = set()
    while True:
        outdegree_vertices = upcoming_outdegree_vertices | {edge[0] for edge in edges if not _is_target(edge[0], edges)}
        upcoming_outdegree_vertices = set()
        if not outdegree_vertices:
            break
        vertex_group = set()
        for outdegree_vertex in outdegree_vertices:
            if outdegree_vertex not in sorted_vertices:
                sorted_vertices.add(outdegree_vertex)
                vertex_group.add(outdegree_vertex)
            outdegree_vertex_edges = {edge for edge in edges if edge[0] == outdegree_vertex}
            for edge in outdegree_vertex_edges:
                edges.remove(edge)
                if not _is_target(edge[1], edges):
                    upcoming_outdegree_vertices.add(edge[1])
        sorted_vertex_groups.add(frozenset(vertex_group))

    if edges:
        raise CyclicGraphError

    isolated_vertices = {vertex for vertex in graph.keys() if vertex not in sorted_vertices}
    if isolated_vertices:
        return {frozenset(isolated_vertices)} | sorted_vertex_groups
    return sorted_vertex_groups


def _graph_to_edges(graph: Graph) -> Iterable[Edge]:
    for from_vertex, to_vertices in graph.items():
        for to_vertex in to_vertices:
            yield from_vertex, to_vertex


def _is_target(vertex: Vertex, edges: Iterable[Edge]) -> bool:
    for edge in edges:
        if vertex == edge[1]:
            return True
    return False
