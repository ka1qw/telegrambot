class SimpleGraph:
    def __init__(self):
        self.edges = {}
        self.weights = {}

    def neighbors(self, id):
        return self.edges[id]

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


import collections


class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


class GridWithWeights(SimpleGraph):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.weights = {}

    def cost(self, from_node, to_node):
        return self.weights.get(to_node, 1)


import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def heuristic(a, b):
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    #path.append(start) # необязательно
    path.reverse() # необязательно
    return path

## отладка графа
def breadth_first_search_1(graph, start):
    # печать того, что мы нашли
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbors(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True

def path_auditorium(path):
    new_path = []
    for next in path:
        if next[0].isnumeric() == True:
            new_path.append("Подойдите к аудитории " + str(next))
        elif next.find("Проход") != -1:
            new_path.append("Пройдите через коридор")
        elif next.find("Арка") != -1:
            new_path.append("Пройдите в арку")
        elif next.find("Дверь по левой стене") != -1:
            new_path.append("Войдите в дверь по левой стене")
        else:
            new_path.append(str(next))

    for i in range(len(new_path)-1):
        if (new_path[i].lower().find("лестница") != -1) and (new_path[i+1].lower().find("лестница") != -1):
            if int(new_path[i][new_path[i].find("лестница")+9]) > int(new_path[i+1][new_path[i+1].find("лестница")+9]):
                new_path.pop(i)
                new_path.insert(i, "Выйдите на лестницу")
                to_path_string = "Спуститесь на " + (new_path[i+1][new_path[i+1].find("лестница") + 9]) + " этаж"
                new_path.pop(i + 1)
                new_path.insert(i+1, to_path_string)
            else:
                new_path.pop(i)
                new_path.insert(i, "Выйдите на лестницу")
                to_path_string = "Поднимитесь на " + (new_path[i+1][new_path[i+1].find("лестница") + 9]) + " этаж"
                new_path.pop(i + 1)
                new_path.insert(i+1, to_path_string)

    for i in range(len(new_path)-1):
        if new_path[i].find("0 этаж") != -1:
            new_path.pop(i)
            new_path.insert(i, "Cпуститесь на цокольный этаж")

    for i in range(len(new_path)-1):
        if new_path[i] == "Пройдите через коридор" and new_path[i+1] == "Войдите в дверь по левой стене":
            new_path.pop(i)
            new_path.pop(i+1)
            new_path.insert(i, "Выйдите через дверь в конце коридора")
        if (new_path[i].lower().find("лестница") != -1):
            new_path.pop(i)
            new_path.insert(i, "Подойдите к лестнице")


    return new_path
