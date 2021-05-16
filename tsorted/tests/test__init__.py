import pytest
from orderedset import OrderedSet

from tsorted import CyclicGraphError, tsorted_grouped, tsorted


def test_tsorted_with_empty_graph() -> None:
    graph = {}
    assert tsorted(graph) == OrderedSet()


def test_tsorted_with_isolated_vertices() -> None:
    graph = {
        1: set(),
        2: set(),
    }
    # Without edges we cannot assert the order.
    assert tsorted(graph) == {1, 2}


def test_tsorted_with_edges() -> None:
    graph = {
        1: {2},
    }
    assert tsorted(graph) == OrderedSet([1, 2])


def test_tsorted_with_multiple_chained_edges() -> None:
    graph = {
        2: {3},
        1: {2},
    }
    assert tsorted(graph) == OrderedSet([1, 2, 3])


def test_tsorted_with_multiple_indegrees() -> None:
    graph = {
        1: {3},
        2: {3},
    }
    vertices = tsorted(graph)
    assert len(vertices) == 3
    assert 1 in vertices
    assert 2 in vertices
    assert vertices[2] == 3


def test_tsorted_with_multiple_outdegrees() -> None:
    graph = {
        1: {2, 3},
    }
    vertices = tsorted(graph)
    assert len(vertices) == 3
    assert vertices[0] == 1
    assert 2 in vertices
    assert 3 in vertices


def test_tsorted_with_cyclic_edges() -> None:
    graph = {
        1: {2},
        2: {1},
    }
    with pytest.raises(CyclicGraphError):
        tsorted(graph)


def test_tsorted_grouped_with_empty_graph() -> None:
    graph = {}
    assert tsorted_grouped(graph) == OrderedSet()


def test_tsorted_grouped_with_isolated_vertices() -> None:
    graph = {
        1: set(),
        2: set(),
    }
    assert tsorted_grouped(graph) == OrderedSet([frozenset({1, 2})])


def test_tsorted_grouped_with_edges() -> None:
    graph = {
        1: {2},
    }
    assert tsorted_grouped(graph) == OrderedSet([frozenset({1}), frozenset({2})])


def test_tsorted_grouped_with_isolated_vertices_and_edges() -> None:
    graph = {
        1: {2, 3, 4},
        5: {4, 6, 7},
        8: set(),
        9: set(),
    }
    assert tsorted_grouped(graph) == OrderedSet([
        frozenset({8, 9}),
        frozenset({1, 5}),
        frozenset({2, 3, 4, 6, 7}),
    ])


def test_tsorted_grouped_with_multiple_chained_edges() -> None:
    graph = {
        2: {3},
        1: {2},
    }
    assert tsorted_grouped(graph) == OrderedSet([frozenset({1}), frozenset({2}), frozenset({3})])


def test_tsorted_grouped_with_multiple_indegrees() -> None:
    graph = {
        1: {3},
        2: {3},
    }
    assert tsorted_grouped(graph) == OrderedSet([
        frozenset({1, 2}),
        frozenset({3}),
    ])


def test_tsorted_grouped_with_multiple_outdegrees() -> None:
    graph = {
        1: {2, 3},
    }
    assert tsorted_grouped(graph) == OrderedSet([
        frozenset({1}),
        frozenset({2, 3}),
    ])


def test_tsorted_grouped_with_cyclic_edges() -> None:
    graph = {
        1: {2},
        2: {1},
    }
    with pytest.raises(CyclicGraphError):
        tsorted_grouped(graph)
