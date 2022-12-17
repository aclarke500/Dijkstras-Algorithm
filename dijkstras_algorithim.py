def get_index_of_vertex(V, v):
    for i in range(len(V)):
        if v == V[i]:
            return i

    return None

'''
    Implements Dijkstra's algorithim
'''
def dijkstra(V, E, source):

    unvisted = V.copy()
    shortest_distance = []
    vi_neighbours = []

    # get neighbours
    for v in V:
        # neighbours of particular node
        neighbours = []
        for e in E:
            # if v is part of an edge, add the vertex is not v
            if e[0] == v:
                neighbours.append(e[1])
            elif e[1] == v:
                neighbours.append(e[0])
        # adds list of neighbours at correct index
        vi_neighbours.append(neighbours)

    for v in V: # set distance to source to 0, all other nodes could 
        if v == source: # be up to infinity
            shortest_distance.append(0)
        else: 
            shortest_distance.append(float('inf'))


    for i in range(0, len(V)):
        temp = float('inf')
        current_node = None

        for v in unvisted:
            if shortest_distance[get_index_of_vertex(V, v)] < temp:
                current_node = v
 
        neighbours = vi_neighbours[get_index_of_vertex(V, current_node)]
        distance = shortest_distance[get_index_of_vertex(V, current_node)]

        for n in neighbours:
            # distance including our node
            temp_dist = distance+1
            neighbour_index = get_index_of_vertex(V, n)

            # if the path we found is shorter, update that
            if shortest_distance[neighbour_index] > temp_dist:
                shortest_distance[neighbour_index] = temp_dist

        # make sure we don't repeat nddes
        unvisted.remove(current_node)


        # vertices will be strings v1 ... vn,
    return shortest_distance


    # sample list for practice
V = ['v1', 'v2', 'v3', 'v4', 'v5', 'v6']


E = [
    ('v1', 'v2'), ('v1', 'v5'), ('v1', 'v4'), ('v2', 'v5'), (
        'v2', 'v3'), ('v5', 'v3'), ('v4', 'v6')
]


for i in range(0, 6):
    print(dijkstra(V, E, V[i]))
