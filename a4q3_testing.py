# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 145
# Instructor: Lauresa Stilling

from a4q3 import to_string, copy
import node as n

def test_driver():
    fails = 0
    tests = 0

    # Testing the to_string() function.

    # Testing an empty node chain.
    test_node = None
    expected = 'EMPTY'
    result = to_string(test_node)
    if result != expected:
        fails += 1
        print("Testing to_string() with a blank chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing a one node chain.
    test_node = n.node(5)
    expected = '[ 5 | / ]'
    result = to_string(test_node)
    if result != expected:
        fails += 1
        print("Testing to_string() with a single-node chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing a multi-node chain, all the same type (int).
    test_node = n.node(1, n.node(2, n.node(3)))
    expected = '[ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]'
    result = to_string(test_node)
    if result != expected:
        fails += 1
        print("Testing to_string() with a multi-node chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing a multi-node chain, all of various types.
    test_node = n.node(1, n.node('two', n.node(3.0)))
    expected = '[ 1 | *-]-->[ two | *-]-->[ 3.0 | / ]'
    result = to_string(test_node)
    if result != expected:
        fails += 1
        print("Testing to_string() with a multi-node chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing the copy() function.

    # Testing an empty node chain.
    test_node = None
    expected = None
    result = copy(test_node)
    if result != expected:
        fails += 1
        print("Testing copy() with a blank chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing the copying of a one node chain.
    test_node = n.node(5)
    expected = '[ 5 | / ]'
    result = to_string(copy(test_node))
    if result != expected:
        fails += 1
        print("Testing to_string() with a single-node chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing a multi-node chain.
    test_node = n.node(1, n.node(2, n.node(3)))
    expected = '[ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]'
    result = to_string(copy(test_node))
    if result != expected:
        fails += 1
        print("Testing to_string() with a multi-node chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing the copied and original chain, to prove they are separated:

    # Initially creates the two nodes, but does not make string representations.
    test_node = n.node(1, n.node(2, n.node(3)))
    copied_node = copy(test_node)
    # Updates a value within the copied node, but should leave the original alone if the program works.
    copied_node.set_data(3)
    # Now creates the string representations to compare with the expected versions.
    test_node = to_string(test_node)
    copied_node = to_string(copied_node)
    expected_test = '[ 1 | *-]-->[ 2 | *-]-->[ 3 | / ]'
    expected_copy = '[ 3 | *-]-->[ 2 | *-]-->[ 3 | / ]'

    if test_node != expected_test and copied_node != expected_copy:
        fails += 1
        print("Testing to_string() with a multi-node chain, Expected:", expected_test, "&", expected_copy,
        " Got: ", test_node, "&", copied_node)
    tests += 1

    # Testing the replace() function.

    print(f"Tests Ran: {tests}" "\n"
          f"Tests Succeeded: {tests - fails}/{tests}" "\n"
          f"Tests Failed: {fails}")

test_driver()
