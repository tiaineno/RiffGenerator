import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.trie import Trie, Node

def test_node():
    """
    test if single node is initialized correctly
    """
    node = Node()
    assert node.children == [None] * 128
    assert node.probabilities == {}

def test_trie_find():
    """
    test if find method works
    query_order_1 tests if trie can return the probabilities in a case where
    the desired order isnt found
    """
    trie = Trie()

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])

    query = trie.find([40,41])
    query_order_1 = trie.find([40,43])

    assert query == {40: 2, 43: 1}
    assert query_order_1 == {41: 3, 42: 1}

def test_trie_find_nonexistent():
    """
    test if find works with nonexistent or empty sequences
    """
    trie = Trie()

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])

    query_no_matches = trie.find([44,41])
    assert query_no_matches == {}

    empty_query = trie.find([])
    assert empty_query == {}

def test_trie_insert_more_and_find():
    """
    test if inserting multiple sequences works
    """
    trie = Trie()

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])

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

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])

    tree = repr(trie)
    assert "Node(children=[41, 42], probabilities={41: 3, 42: 1})" in tree
    assert "Node(children=[], probabilities={41: 1, 42: 1})" in tree
