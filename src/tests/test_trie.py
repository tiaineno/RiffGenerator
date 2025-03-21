import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.trie import Trie

def test_trie_find():
    trie = Trie()

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])

    query = trie.find([40,41])

    assert query == {40: 2, 43: 1}

def test_trie_find_nonexistent():
    trie = Trie()

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])
    
    query_one_match = trie.find([40,43])
    assert query_one_match == {41: 3, 42: 1}

    query_no_matches = trie.find([44,41])
    assert query_no_matches == {}

    empty_query = trie.find([])
    assert empty_query == {}

def test_trie_insert_more_and_find():
    trie = Trie()

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])

    trie.insert([44, 41, 40])
    
    query_one_match = trie.find([44,41])
    assert query_one_match == {40: 1}

def test_trie_repr():
    trie = Trie()

    sequence = [40, 41, 40, 41, 43, 40, 41, 40, 42, 43]
    for i in range(len(sequence)-2):
        trie.insert(sequence[i:i+3])

    tree = repr(trie)
    assert "Node(children=[41, 42], probabilities={41: 3, 42: 1})" in tree
    assert "Node(children=[], probabilities={41: 1, 42: 1})" in tree
