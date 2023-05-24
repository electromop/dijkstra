import random as rm
import sys
import dijkstra_func as dijkstra
import matplotlib.pyplot as plt

n = 15
m = 15
matrix = [[rm.randint(0, 10) for i in range(n)] for j in range(m)]

start_i, start_j = int(input('Введите i start точки: ')), int(input('Введите j start точки: '))
stop_i, stop_j = int(input('Введите i stop точки: ')), int(input('Введите j stop точки: '))
unvisited_nodes = []
for i in range(n):
    for j in range(m):
        if i == start_i and j == start_j:
            unvisited_nodes.append([matrix[i][j], [i, j]])
        else:
            unvisited_nodes.append([sys.maxsize, [i, j]])

visited_nodes = []

previous_nodes = {}
min_node = [0, f'{start_i}, {start_j}']
while unvisited_nodes:
    # print(unvisited_nodes)
    prev_mn = min_node
    min_node = dijkstra.take_min_from_unvisitted(unvisited_nodes)
    # print(min_node)
    neighbours = dijkstra.check_neighbours(min_node[1][0], min_node[1][1], matrix)
    dijkstra.delete_rn_fr_unvisitted(min_node, unvisited_nodes)
    dijkstra.add_rn_to_visitted(min_node, visited_nodes)
    dijkstra.edit_unvisitted_list(neighbours, min_node, previous_nodes, unvisited_nodes)
    # previous_nodes[str(min_node)] = prev_mn
    if min_node[1][0] == stop_i and min_node[1][1] == stop_j:
        break

path = dijkstra.restore_the_path(previous_nodes, stop_i, stop_j, start_i, start_j)
total_cost = 0
for i in path:
    total_cost += matrix[i[0]][i[1]]
print(f"Путь: {path}")
print(f"Стоимость по пути: {total_cost}")
print(f"Стоимость по посещенным: {visited_nodes[-1][0]}")

fig, ax = plt.subplots()

ax.matshow(matrix, cmap=plt.cm.Blues)

for i in range(n):
    for j in range(m):
        c = matrix[j][i]
        ax.text(i, j, str(c), va='center', ha='center')

i_list = []
j_list = []

for i in path:
    i_list.append(i[1])
    j_list.append(i[0])

ax.plot(i_list, j_list, 'r')
ax.plot(start_j, start_i, 'ro')
ax.plot(stop_j, stop_i, 'ro')
ax.imshow()
