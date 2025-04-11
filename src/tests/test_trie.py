import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.trie import Trie, Node

def test_node():
    """
    test if single node is initialized correctly
    """
    node = Node()
    assert node.children == {}
    assert node.probabilities == {}

def test_trie_find():
    """
    test if find method works
    """
    trie = Trie()
    order = 2

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-order):
        trie.insert(sequence[i:i+1+order])

    query = trie.find([40,41])
    assert query == {40: 2, 43: 1}

def test_trie_find_nonexistent():
    """
    test if find works with nonexistent sequences
    """
    trie = Trie()
    order = 2

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-order):
        trie.insert(sequence[i:i+1+order])

    with pytest.raises(KeyError):
        trie.find([44, 41])

    with pytest.raises(KeyError):
        trie.find([40, 43])

def test_trie_find_empty():
    """
    test if find works with an empty sequence
    """
    trie = Trie()
    order = 2

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-order):
        trie.insert(sequence[i:i+1+order])

    query = trie.find([])
    assert query == {40: 4, 41: 3, 43: 1}

def test_trie_insert_more_and_find():
    """
    test if inserting multiple sequences works
    """
    trie = Trie()
    order = 2

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-order):
        trie.insert(sequence[i:i+1+order])

    trie.insert([44, 41, 40])
    trie.insert([40, 41, 45])

    query_one_match = trie.find([44,41])
    assert query_one_match == {40: 1}
    query_more_matches = trie.find([40,41])
    assert query_more_matches == {40: 2, 43: 1, 45: 1}

def test_trie_repr():
    """
    test if repr works
    """
    trie = Trie()
    order = 2

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-order):
        trie.insert(sequence[i:i+1+order])

    tree = repr(trie)
    assert "Node(children=[41, 42], probabilities={41: 3, 42: 1})" in tree
    assert "Node(children=[], probabilities={41: 1, 42: 1})" in tree
