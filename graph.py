import math as m
import random as rand
import numpy as np

class Graph:
    def __init__(self, name, width, height):
        self.width = width
        self.height = height

        self.t = 5
        self.gravity = 0.05

        with open("./tpfinal/grafos/" + name + ".txt", 'r') as f:
            line = f.readline()
            nodes_count = int(line)
            i = 0
            nodes = {}
            while i < nodes_count:
                line = f.readline().rstrip()
                nodes[line] = self.asign_coordinates()
                i = i + 1
            edges = []
            for line in f:
                splited_line = line.split(' ')
                edge = (splited_line[0],splited_line[1].rstrip())
                edges.append(edge)

        self.edges = edges
        self.nodes = nodes

        c = 0.8
        area = width * height
        self.k     = c * m.sqrt(area / len(self.nodes.keys()))

        return

    def asign_coordinates(self):
        return {'x': rand.randint(- self.width / 2, self.width / 2),
                'y': rand.randint(- self.height / 2, self.height / 2),
                'acum_x': 0, 'acum_y': 0}

    def get_coordinates(self):
        xpoints = []
        ypoints = []

        for (v, u) in self.edges:
            xpoints.append(self.nodes[v]['x'])
            ypoints.append(self.nodes[v]['y'])
            xpoints.append(self.nodes[u]['x'])
            ypoints.append(self.nodes[u]['y'])

        return (xpoints, ypoints)

    def compute_attraction_forces(self):
        for e in self.edges:
            v = np.array((self.nodes[e[0]]['x'], self.nodes[e[0]]['y']))
            u = np.array((self.nodes[e[1]]['x'], self.nodes[e[1]]['y']))
            delta_x = v[0] - u[0]
            delta_y = v[1] - u[1]
            distance = np.linalg.norm(v - u)

            if(distance != 0):
                fa = (distance ** 2) / self.k
                self.nodes[e[0]]['acum_x'] -= (delta_x/distance) * fa
                self.nodes[e[0]]['acum_y'] -= (delta_y/distance) * fa

                self.nodes[e[1]]['acum_x'] += (delta_x/distance) * fa
                self.nodes[e[1]]['acum_y'] += (delta_y/distance) * fa
        return

    def compute_repulsion_forces(self):
        for v in self.nodes.values():
            v['acum_x'] = 0
            v['acum_y'] = 0
            for u in self.nodes.values():
               if v != u:
                    v_a = np.array((v['x'], v['y']))
                    u_a = np.array((u['x'], u['y']))

                    delta_x = v_a[0] - u_a[0]
                    delta_y = v_a[1] - u_a[1]
                    distance = np.linalg.norm(v_a - u_a)
                    if(distance != 0):
                        fr = (self.k ** 2) / distance

                        v['acum_x'] += (delta_x / distance) * fr
                        v['acum_y'] += (delta_y / distance) * fr
        return

    def update_positions(self):
        for n in self.nodes.values():
            acum_dist = np.linalg.norm([n['acum_x'], n['acum_y']])
            if(acum_dist > self.t):
                n['acum_x'], n['acum_y'] = (n['acum_x'] / acum_dist) * self.t , (n['acum_y'] / acum_dist) * self.t

            n['x'] += n['acum_x']
            n['y'] += n['acum_y']

            n['x'] = min(self.width / 2, max(- self.width / 2, n['x']))
            n['y'] = min(self.height / 2, max(- self.height / 2, n['y']))

        self.t *= 0.8
        return

    def compute_gravity(self):
        for v in self.nodes.values():
            v['acum_x'] -= v['x'] * self.gravity
            v['acum_y'] -= v['y'] * self.gravity

    def apply_repulsion():
        pass
