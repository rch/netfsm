class Base:
    key = None

    def __init__(self):
        pass

    def enter(self):
        print(f"Entering: {self.key}")

    def exit(self):
        print(f"Exiting: {self.key}")


class StartNode(Base):
    key = "Start"


class LakeNode(Base):
    key = "Lake"


class OceanNode(Base):
    key = "Ocean"


class VolcanoNode(Base):
    key = "Volcano"


class ForestNode(Base):
    key = "Forest"


class FieldNode(Base):
    key = "Field"


class MountainNode(Base):
    key = "Mountain"
