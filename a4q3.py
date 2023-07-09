# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 145
# Instructor: Lauresa Stilling

def to_string(node_chain):
    """
    Purpose:
        Converts the node chain into a string representation.
    Parameters:
        node_chain: The chain of  nodes that will be converted, either into a string representation or simply will be
        returned empty.
    Returns:
        The string representation of the node, or the string 'EMPTY'.
    """

    # Checks if the node_chain is empty
    if node_chain is None:
        return 'EMPTY'
    else:
        # Copies the value from the current node, then formats it, and finally cycles to next node.
        node_value = node_chain.get_data()
        result = '[ {} |'.format(str(node_value))
        next_node = node_chain.get_next()
    if next_node is None:
        # If the node chain has reached its end, it caps it off with this.
        result += ' / ]'
    else:
        result += ' *-]-->{}'.format(str(to_string(next_node)))

    return result

