class Node:
    """
    implementation of a single node,
    the number of children is 128 since that is the amount of midi notes
    """
    def __init__(self):
        self.children = [None] * 128
        self.probabilities = {}

    def __repr__(self):
        children = [i for i, child in enumerate(self.children) if child]
        return f"Node(children={children}, probabilities={self.probabilities})"

class Trie:
    """
    implementation of the used trie data structure
    """
    def __init__(self):
        self.root = Node()

    def insert(self, sequence):
        """
        inserts a single sequence to the tree
        probabilities are saved in each node, so that smaller orders can be utilized as well
        works with any markovs chain order
        """
        current = self.root

        for i in range(len(sequence)-1):
            note = sequence[i]
            if not current.children[note]:
                current.children[note] = Node()
            current = current.children[note]

            next_note = sequence[i + 1]
            if next_note in current.probabilities:
                current.probabilities[next_note] += 1
            else:
                current.probabilities[next_note] = 1

    def find(self, sequence):
        """
        takes a sequence as a parameter and returns the probabilites of the last node that exists
        """
        current = self.root
        for i in range(len(sequence)):
            note = sequence[i]
            if current.children[note] is None:
                return current.probabilities
            current = current.children[note]
        return current.probabilities

    def __repr__(self):
        """
        returns the structure of the data structure with DFS
        """
        def traverse(node, level=0):
            result = "  " * level + repr(node) + "\n"
            for child in node.children:
                if child:
                    result += traverse(child, level + 1)
            return result

        return traverse(self.root)
