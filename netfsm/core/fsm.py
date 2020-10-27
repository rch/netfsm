

class Event:
    _event = None

    def __init__(self, event):
        self._event = event


class Transition:
    _elements = None

    def __init__(self, state, model, event):
        self._elements = [state, event]
    
    def add(self, element):
        self._elements.append(element)

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
        self._state = node

    def handle(self, event):
        txn = Transition(self._state, self._model, event)
        return txn

