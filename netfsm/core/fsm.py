from . import model


class Event:
    _event = None

    def __init__(self, event):
        self._event = event


class Transition:
    _elements = None
    _source = None
    _target = None
    _event = None

    def __init__(self, state, model, event):
        self._elements = [None] * 3
        self.source = state
        self.event = event
        if event in state._cmds:
            self.target = state._cmds[event]

    @property
    def source(self):
        return self._source
    
    @source.setter
    def source(self, element):
        self._source = element
        self._elements[0] = element
    
    @property
    def target(self):
        return self._target
    
    @target.setter
    def target(self, element):
        self._target = element
        self._elements[2] = element
    
    @property
    def event(self):
        return self._event
    
    @event.setter
    def event(self, element):
        self._event = element
        self._elements[1] = element

    def __str__(self):
        lst = ["({})".format(el) for el in self._elements]
        return " -> ".join(lst)


class FSM:
    _state = None
    _model = None

    def __init__(self, digraph, start=None):
        self._model = digraph.model
        if start is None:
            self._state = digraph.start
        else:
            self._state = start

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, node):
        if issubclass(type(self._state.handler), model.Base):
            self._state.handler.exit()
        if issubclass(type(node.handler), model.Base):
            node.handler.enter()
        self._state = node

    def handle(self, event):
        txn = Transition(self._state, self._model, event)
        if txn.target:
            self.state = self._model[txn.target]
        return txn
