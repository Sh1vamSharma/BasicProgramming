class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for source, destination in edges:
            if source in self.graph_dict:
                self.graph_dict[source].append(destination)
            else:
                self.graph_dict[source] = [destination]
        print("Graph Dictionary : ", self.graph_dict)

    def get_path(self, source, destination, path=[]):
        path = path + [source]
        if source == destination:
            return [path]
        if source not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[source]:
            if node not in path:
                new_path = self.get_path(node, destination, path)
                for p in new_path:
                    paths.append(p)

        return paths

    def get_shortest_path(self, source, destination, path=[]):
        path = path + [source]
        if source == destination:
            return [path]
        if source not in self.graph_dict:
            return []
        shortest_path = None
        for node in self.graph_dict[source]:
            if node not in path:
                sp = self.get_path(node, destination, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp

        return shortest_path

if __name__ == "__main__":
    routs = [
        ('Mumbai' , 'Paris'),
        ('Mumbai' , 'Dubai'),
        ('Paris' , 'Dubai'),
        ('Paris' , 'Newyork') ,
        ('Dubai' , 'Newyork') ,
        ('Newyork' , 'Torronto')
    ]

    route_graph = Graph(routs)

    # d = {
    #     'Mumbai' : ['Paris', 'Newyork'],
    #     'Mumbai' : ['Dubai', 'Newyork'],
    #     'Paris' : ['Newyork'],
    #     'Paris' : ['Dubai', 'Newyork'],
    #     'Dubai' : ['Newyork'],
    #     'Newyork' : ['Torronto']
    # }
    source = 'Mumbai'
    destination = 'Newyork'
    path = route_graph.get_path(source,destination)
    shortest_path = route_graph.get_shortest_path(source, destination)
    print(f"paths from {source} to {destination} : {path}")
    print(f"paths from {source} to {destination} : {shortest_path}")

