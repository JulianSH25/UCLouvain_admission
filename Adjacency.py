def mat_to_list(adj_mat):
    """ Convert adjacency matrix to an adjacency list representation

    Parameters:
    -----------
    adj_mat : (a square 0-1 matrix)
        Adjacency matrix (n x n) of the graph (of n nodes)


    Returns:
    --------
     adj_list: `list[list[int]]`
        The adjacency list of the graph

    """
    adj_list = []

    for row in range(len(adj_mat)):
        adj_list_temp = []
        for col in range(len(adj_mat[row])):
            if adj_mat[row][col] == 1:
                adj_list_temp.append(col)
        adj_list.append(adj_list_temp)

    if __name__ == '__main__':
        print(f'Dimension: {len(adj_mat)}')
    return adj_list


if __name__ == '__main__':
    adj_mat = [
        [0, 1, 0, 1, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 1, 1]
    ]

    adj_list = mat_to_list(adj_mat)
    print(adj_list)
