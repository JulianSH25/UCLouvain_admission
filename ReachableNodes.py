def reachable(adj_list, start_node, reachable_nodes=None):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    if reachable_nodes is None:
        reachable_nodes = set()

    reachable_nodes.add(start_node)

    for node in adj_list[start_node]:
        reachable(adj_list, node, reachable_nodes) if node not in reachable_nodes else None

    return reachable_nodes


if __name__ == '__main__':
    adj_list = [[1, 3], [2], [0], [4], [3], []]
    print(reachable(adj_list, 0))
    print(reachable(adj_list, 3))
