from enum import Enum, auto

class Direction(Enum):
    right = auto()
    left = auto()
    up = auto()
    down = auto()

def mover(direction):
    if not isinstance(direction, Direction):
        raise ValueError("Essa opção de direção não existe!")
    return f'Moving {direction.name}' # Como padrão para o enum, o name retorna o nome dos objetos criados 


if __name__ == "__main__":
    print(mover(Direction.right))
    print(mover(Direction.left))
    print(mover(Direction.up))
    print(mover(Direction.down))