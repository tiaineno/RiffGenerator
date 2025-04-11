class Node:
    """
    implementation of a single node,
    the number of children is 128 since that is the amount of midi notes
    """
    def __init__(self):
        self.children = {}
        self.probabilities = {}

    def __repr__(self):
        children = list(self.children.keys())
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
            if note in current.probabilities:
                current.probabilities[note] += 1
            else:
                current.probabilities[note] = 1
            if note not in current.children:
                current.children[note] = Node()
            current = current.children[note]

        note = sequence[-1]
        if note in current.probabilities:
            current.probabilities[note] += 1
        else:
            current.probabilities[note] = 1

    def find(self, sequence):
        """
        takes a sequence as a parameter and returns the probabilites of the last node
        """
        current = self.root
        for i in range(len(sequence)):
            note = sequence[i]
            current = current.children[note]
        return current.probabilities

    def __repr__(self):
        """
        returns the structure of the data structure with DFS
        """
        def traverse(node, level=0):
            result = "  " * level + repr(node) + "\n"
            for child in node.children.values():
                result += traverse(child, level + 1)
            return result

        return traverse(self.root)
