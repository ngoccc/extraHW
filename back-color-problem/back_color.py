from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes


def generate_quiz():
    return [
        shapes[randint(0, 3)]['text'],
        shapes[randint(0, 3)]['color'],
        randint(0, 1)  # 0 : meaning, 1: color
    ]


def mouse_press(x, y, text, color, quiz_type):
    for i in shapes:
        if i['rect'][0] <= x <= i['rect'][0] + i['rect'][2] and i['rect'][1] <= y <= i['rect'][1] + i['rect'][3]:
            if quiz_type == 0:
                return i['text'] == text
            elif quiz_type == 1:
                return i['color'] == color
