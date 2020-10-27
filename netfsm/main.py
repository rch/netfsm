import os
import re
from core import model
from core import graph
from core import fsm


NORMALIZE_NAMES = os.getenv('NORMALIZE_NAMES', True)

register = [
    model.StartNode(),
    model.LakeNode(),
    model.OceanNode(),
    model.VolcanoNode(),
    model.ForestNode(),
    model.FieldNode(),
    model.MountainNode()
]
digraph = graph.TGF.load_digraph('digraph.tgf', register)

fsm = fsm.FSM(digraph)

# This is the main file for the finite state machine implementation. It contains
# A stub definition for processing events, and a command line input for events to
# be entered. The spec and the state diagram are provided separately.
def handle_event(event):
    """Handles events within the context of the defined state machine as defined by
    the spec for this project.
    Parameters
    ----------
    event : string
    event name to be processed by the state machine
    """
    # ---------- STATE HANDLING CODE HERE -----------------
    transition = fsm.handle(event)
    # print structure
    print(transition)
    # ---------- END STATE HANDLING CODE ------------------

if __name__ == "__main__":
    while True:
        event = input("Enter an event to handle, or 'quit': ")
        # special case for quitting the test
        if event == "quit":
            break
        handle_event(event)
