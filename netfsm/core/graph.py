import re
from collections import defaultdict


class Element:
    _data = None
    _handler = None

    def __init__(self, element, handler=None):
        self._cmds = {}
        self._data = element
        if handler:
            self._handler = handler

    @property
    def key(self):
        return self._data.get("label", None)

    @property
    def handler(self):
        return self._handler

    @handler.setter
    def handler(self, handler):
        self._handler = handler

    def __str__(self):
        return self._data.get("label", self._data)


class Node(Element):

    _cmds = {}

    @property
    def id(self):
        return self._data.get("id", None)

    def add_cmd(self, key, target):
        self._cmds[key] = target


class Edge(Element):
    @property
    def source(self):
        return self._data["source"]

    @property
    def target(self):
        return self._data["target"]


class DiGraph:
    _ids = {}
    _model = {}
    _nodes = []
    _edges = []

    def __init__(self, nodes, edges, register):
        self._nodes = list(map(Node, nodes))
        self._edges = list(map(Edge, edges))
        for node in self._nodes:
            if node.key in register:
                node.handler = register[node.key]
            self._model[node.key] = node
            self._ids[node.id] = node.key
        for edge in self._edges:
            self._model[self._ids[edge.source]].add_cmd(
                edge.key, self._ids[edge.target])

    @property
    def start(self):
        start = self._model.get("Start", None)
        if start is None:
            raise ValueError("Could not find start node.")
        return start

    @property
    def model(self):
        return self._model

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges


NodeLine = re.compile(r"([0-9]+)\s(.*)")

EdgeLine = re.compile(r"([0-9]+)\s([0-9]+)\s(.*)")


class TGF:
    @staticmethod
    def _node_parser(line, fmt=NodeLine):
        m = fmt.match(line)
        if not m:
            raise ValueError(f"Incorrect format for Node: {line}")
        return {"id": m.group(1), "label": m.group(2)}

    @staticmethod
    def _edge_parser(line, fmt=EdgeLine):
        m = fmt.match(line)
        if not m:
            raise ValueError(f"Incorrect format for Edge: {line}")
        return {"source": m.group(1), "target": m.group(2), "label": m.group(3)}

    @staticmethod
    def load_digraph(filename, register):
        nodes = []
        edges = []
        with open(filename) as f:
            lst = nodes
            parser = TGF._node_parser
            for line in f:
                if not line:
                    pass
                elif line.startswith("#"):
                    lst = edges
                    parser = TGF._edge_parser
                else:
                    lst.append(parser(line))
        return DiGraph(nodes, edges, register)
