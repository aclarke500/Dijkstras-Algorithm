


def get_index_of_vertex(V, v):
    for i in range(len(V)):
        if v == V[i]:
            return i

    return None

def done(distances):
    for d in distances:
        if d == float('inf'):
            return False






def dijkstra(V, E, source):
    unvisted = V.copy()
    visted = []

    shortest_distance = []
    previous_vertex = [None, None, None, None, None]

    vi_neighbours = []

    # get neighbours
    for v in V:
        neighbours = []
        for e in E:

            if e[0] == v:
                neighbours.append(e[1])
            elif e[1] == v:
                neighbours.append(e[0])

        vi_neighbours.append(neighbours)

    for v in V:
        if v == source:
            shortest_distance.append(0)
        else:
            shortest_distance.append(float('inf'))


    # print(shortest_distance)
    for i in range(0, 5):




            temp = 99999
            current_node = None
            for v in unvisted:
                if shortest_distance[get_index_of_vertex(V, v)] < temp:
                    current_node = v
                    # print(v, "ste")
            # print(current_node)
            # print(current_node, 'cn', V)
            neighbours=vi_neighbours[get_index_of_vertex(V, current_node)]
            distance=shortest_distance[get_index_of_vertex(V, current_node)]
            for n in neighbours:
                temp_dist=distance+1
                neighbour_index = get_index_of_vertex(V, n)
                # print(neighbour_index)
                if shortest_distance[neighbour_index] > temp_dist:
                    shortest_distance[neighbour_index] = temp_dist
                    # previous_vertex[neighbour_index] = current_node

            unvisted.remove(current_node)
            # print(unvisted)
        

   




        # vertices will be strings v1 ... vn,
    print(shortest_distance)
        # sample list for practice
V = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']


E = [
    ('v1', 'v2'), ('v1', 'v5'), ('v1', 'v4'), ('v2', 'v5'), (
        'v2', 'v3'), ('v5', 'v3'), ('v4', 'v6')
]


for i in range(0, 6):
    dijkstra(V, E, V[i])