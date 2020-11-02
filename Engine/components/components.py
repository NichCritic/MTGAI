class Creature(object):

    def __init__(self, entity_id, power, toughness):
        self.entity_id = entity_id
        self.power = power
        self.toughness = toughness

class Artifact(object):
    def __init__(self, entity_id):
        self.entity_id = entity_id

class Spell(object):

    def __init__(self, entity_id):
        self.entity_id = entity_id


class Land(object):

    def __init__(self, entity_id):
        self.entity_id = entity_id


class Owner(object):

    def __init__(self, entity_id, player_id):
        self.entity_id = entity_id
        self.player_id = player_id
