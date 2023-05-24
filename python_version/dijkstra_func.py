import random as rm
import sys
import matplotlib.pyplot as plt

def check_neighbours(i, j, matrix): #проверяем всех соседей точки
    neighbours = []
    if i == 0 and j == 0:
        neighbours.append([matrix[i][j+1], [i, j+1]])
        neighbours.append([matrix[i+1][j], [i+1, j]])
    elif i == 0 and j == len(matrix[i]) - 1:
        neighbours.append([matrix[i][j-1], [i, j-1]])
        neighbours.append([matrix[i+1][j], [i+1, j]])
    elif i == len(matrix) - 1 and j == 0:
        neighbours.append([matrix[i][j+1], [i, j+1]])
        neighbours.append([matrix[i-1][j], [i-1, j]])
    elif i == len(matrix) - 1 and j == len(matrix[i]) - 1:
        neighbours.append([matrix[i][j-1], [i, j-1]])
        neighbours.append([matrix[i-1][j], [i-1, j]])
    elif i == 0:
        neighbours.append([matrix[i][j+1], [i, j+1]])
        neighbours.append([matrix[i][j-1], [i, j-1]])
        neighbours.append([matrix[i+1][j], [i+1, j]])
    elif j == 0:
        neighbours.append([matrix[i+1][j], [i+1, j]])
        neighbours.append([matrix[i-1][j], [i-1, j]])
        neighbours.append([matrix[i][j+1], [i, j+1]])
    elif i == len(matrix) - 1:
        neighbours.append([matrix[i][j+1], [i, j+1]])
        neighbours.append([matrix[i][j-1], [i, j-1]])
        neighbours.append([matrix[i-1][j], [i-1, j]])
    elif j == len(matrix[i]) - 1:
        neighbours.append([matrix[i+1][j], [i+1, j]])
        neighbours.append([matrix[i-1][j], [i-1, j]])
        neighbours.append([matrix[i][j-1], [i, j-1]])
    else:
        neighbours.append([matrix[i+1][j], [i+1, j]])
        neighbours.append([matrix[i-1][j], [i-1, j]])
        neighbours.append([matrix[i][j+1], [i, j+1]])
        neighbours.append([matrix[i][j-1], [i, j-1]])
    return neighbours


def take_min_from_unvisitted(unvisited_nodes): #берем минимальную точку из списка непосещенных
    min_el = [sys.maxsize, [0, 0]]
    for elmnt in unvisited_nodes:
        if min_el[0] > elmnt[0]:
            min_el = elmnt
    return min_el


def delete_rn_fr_unvisitted(node, unvisited_nodes): #удаляем закрытую точку из списка непосещенных
    for nd in unvisited_nodes:
        if nd[1] == node[1]:
            unvisited_nodes.pop(unvisited_nodes.index(nd))


def add_rn_to_visitted(node, visited_nodes): #переносим эту точку в список посещенных
    visited_nodes.append(node)


def restore_the_path(path_dict, stop_i, stop_j, start_i, start_j):
    node = [stop_i, stop_j]
    path_list = [node]
    while node != [start_i, start_j]:
        node = path_dict[str(node)]
        path_list.append(node)
    return path_list[::-1]


def edit_unvisitted_list(neighbours, min_node, previous_nodes, unvisited_nodes): #в списке непосещенных меняем веса соседей
    for nd in unvisited_nodes:
        for nb in neighbours:
            if nd[1] == nb[1] and nd[0] > (nb[0] + min_node[0]):
                if nd[0] == sys.maxsize:
                    nd[0] = 0
                nd[0] += nb[0]
                nd[0] += min_node[0]
                previous_nodes[str(nb[1])] = min_node[1]
    return neighbours.reverse()