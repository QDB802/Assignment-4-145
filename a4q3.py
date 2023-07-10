# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 145
# Instructor: Lauresa Stilling

import node as n


def to_string(node_chain):
    """
    Purpose:
        Converts the node chain into a string representation.
    Parameters:
        node_chain: The chain of nodes that will be converted, either into a string representation or simply will be
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


def copy(node_chain):
    """
    Purpose:
        Makes a copy of a pre-existing node.
    Parameters:
        node_chain: The set of nodes that will be cycled and copied.
    Returns:
        A reference to the location of the first node of the new copied chain.
    """
    # Checks if the node to be copied is empty.
    if node_chain is None:
        return None
    else:
        # Initializes a blank copy, copies the first value of the original node and sets the first value to the copy.
        node_copy = n.node(None)
        node_val = node_chain.get_data()
        node_copy.set_data(node_val)
        next_node = node_chain.get_next()
    # Recursively calls the program until the ending node has been reached.
    if next_node is not None:
        next_copy = copy(next_node)
        node_copy.set_next(next_copy)

    return node_copy


def replace(node_chain, target, replacement):
    # Checks if the node that is empty.
    if node_chain is None:
        return None
    else:
        # If the specified node has the target, it updates the node and then cycles to the next.
        if node_chain.get_data() == target:
            node_chain.set_data(replacement)
            next_node = node_chain.get_next()
        # If the specified node doesn't have the target, it simply cycles to the next.
        else:
            next_node = node_chain.get_next()
    # Once the node chain reaches the end it recursively performs the actions.
    if next_node is not None:
        replace(next_node, target, replacement)
    return node_chain
