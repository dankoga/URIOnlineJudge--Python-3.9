def vector_dot(U, V):
    return U[0] * V[0] + U[1] * V[1] + U[2] * V[2]


def vector_cross(U, V):
    return [U[1] * V[2] - U[2] * V[1],
            U[2] * V[0] - U[0] * V[2],
            U[0]*V[1] - U[1]*V[0]]


def vector_sub(U, V):
    return [U[0] - V[0],
            U[1] - V[1],
            U[2] - V[2]]


FACES_IDX = [[1, 2, 3],
             [0, 2, 3],
             [0, 1, 3],
             [0, 1, 2]]

if __name__ == '__main__':
    while True:
        try:
            pyramid_vertex = [list(map(float, input().split()))]
        except EOFError:
            break
        pyramid_vertex.append(list(map(float, input().split())))
        pyramid_vertex.append(list(map(float, input().split())))
        pyramid_vertex.append(list(map(float, input().split())))
        viewer = list(map(float, input().split()))

        pyramid_center = [sum(pyramid_vertex[v][0] for v in range(4)) / 4.0,
                          sum(pyramid_vertex[v][1] for v in range(4)) / 4.0,
                          sum(pyramid_vertex[v][2] for v in range(4)) / 4.0]

        for v in range(4):
            opposing_face_center = [(pyramid_vertex[FACES_IDX[v][0]][i] +
                                     pyramid_vertex[FACES_IDX[v][1]][i] +
                                     pyramid_vertex[FACES_IDX[v][2]][i]) / 3.0
                                    for i in range(3)]

            opposing_face_U = vector_sub(pyramid_vertex[FACES_IDX[v][1]], pyramid_vertex[FACES_IDX[v][0]])
            opposing_face_V = vector_sub(pyramid_vertex[FACES_IDX[v][2]], pyramid_vertex[FACES_IDX[v][0]])
            opposing_face_orthogonal = vector_cross(opposing_face_U, opposing_face_V)
            center_to_vertex = vector_sub(pyramid_vertex[v], pyramid_center)
            if vector_dot(opposing_face_orthogonal, center_to_vertex) > 0:
                opposing_face_orthogonal = vector_sub([0, 0, 0], opposing_face_orthogonal)

            view_direction = vector_sub(opposing_face_center, viewer)
            opposing_face_orientation = vector_dot(view_direction, opposing_face_orthogonal)
            if opposing_face_orientation > -0.0001:
                print('N', end='')
            else:
                print('S', end='')
        print()
