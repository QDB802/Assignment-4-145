# Name: Ken Duff
# NSID: qdb802
# Student#: 11318955
# CMPT 145
# Instructor: Lauresa Stilling

from a4q3 import to_string
import node as n

def test_driver():
    fails = 0
    tests = 0

    # Testing an empty node chain
    test_node = None
    expected = 'EMPTY'
    result = to_string(test_node)
    if result != expected:
        fails += 1
        print("Testing to_string() with a blank chain, Expected:", expected, " Got: ", result)
    tests += 1

    # Testing a one node chain
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

    print(f"Tests Ran: {tests}" "\n"
          f"Tests Succeeded: {tests-fails}/{tests}" "\n"
          f"Tests Failed: {fails}")


test_driver()
