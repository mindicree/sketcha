class PlayerNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class CharacterNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class PlayerCharacterNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ItemNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class EnemyNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)