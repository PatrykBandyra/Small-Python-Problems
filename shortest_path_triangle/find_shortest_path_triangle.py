from dijkstar import Graph, find_path
import dijkstar


def read_data(filename):
    with open(filename) as file:
        values = []
        for line in file:
            row = []
            for value in line.split():
                row.append(int(value))
            values.append(row)
    return values


def create_graph(values):
    graph = Graph()
    for i, row in enumerate(values):
        for j, val in enumerate(row):
            try:
                graph.add_edge((i, j), (i + 1, j), values[i + 1][j])  # lower left value in triangle
                graph.add_edge((i, j), (i + 1, j + 1), values[i + 1][j + 1])  # lower right value in triangle
            except IndexError:
                return graph


def main(filename):
    values = read_data(filename)
    graph = create_graph(values)
    last_row_index = len(values) - 1
    paths_info = []
    for i in range(len(values[-1])):
        ob = find_path(graph, (0, 0), (last_row_index, i))
        ob.edges.insert(0, values[0][0])
        ob.costs.insert(0, values[0][0])
        ob = dijkstar.algorithm.PathInfo(ob.nodes, ob.edges, ob.costs, ob.total_cost+values[0][0])
        paths_info.append(ob)

    # find shortest path
    total_costs = []
    for i, ob in enumerate(paths_info):
        total_costs.append((i, ob))
    total_costs = sorted(total_costs, key=lambda x: x[1].total_cost)

    answer_objects = [total_costs[0]]
    for i in range(1, len(total_costs)):
        if total_costs[i][1].total_cost == answer_objects[0]:
            answer_objects.append(total_costs[i])
        else:
            break

    # display shortest paths
    for a in answer_objects:
        print(paths_info[a[0]])


if __name__ == '__main__':
    # main('1-very_easy.txt')
    # main('2-easy.txt')
    main('3-medium.txt')
