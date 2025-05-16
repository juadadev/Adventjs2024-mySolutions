import collections

"""Los elfos 🧝🧝 de Santa Claus han encontrado un montón de botas mágicas
desordenadas en el taller.
Cada bota se describe por dos valores:

- type indica si es una bota izquierda (I) o derecha (R).
- size indica el tamaño de la bota.

Tu tarea es ayudar a los elfos a emparejar todas las botas del mismo tamaño
que tengan izquierda y derecha. Para ello, debes devolver una lista con los
pares disponibles después de emparejar las botas.

¡Ten en cuenta que puedes tener más de una zapatilla emparejada del mismo tamaño!
"""

"""
const shoes = [
  { type: 'I', size: 38 },
  { type: 'R', size: 38 },
  { type: 'R', size: 42 },
  { type: 'I', size: 41 },
  { type: 'I', size: 42 }
]

organizeShoes(shoes)
// [38, 42]

const shoes2 = [
  { type: 'I', size: 38 },
  { type: 'R', size: 38 },
  { type: 'I', size: 38 },
  { type: 'I', size: 38 },
  { type: 'R', size: 38 }
]
// [38, 38]

const shoes3 = [
  { type: 'I', size: 38 },
  { type: 'R', size: 36 },
  { type: 'R', size: 42 },
  { type: 'I', size: 41 },
  { type: 'I', size: 43 }
]

organizeShoes(shoes3)
// []
"""


def organizeShoes(shoes: list):
    left_boots = collections.Counter(
        [shoe["size"] for shoe in shoes if shoe["type"] == "I"]
    )
    right_boots = collections.Counter(
        [shoe["size"] for shoe in shoes if shoe["type"] == "R"]
    )

    pair_boots = []
    for size in left_boots:
        if size in right_boots:
            pair = min(left_boots[size], right_boots[size])
            pair_boots.extend([size] * pair)

    return pair_boots
