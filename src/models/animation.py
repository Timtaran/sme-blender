from dataclasses import dataclass
from enum import Enum
from typing import Optional

from mathutils import Vector


class ActionTypes(str, Enum):
    MODEL = "model"
    EXTENSION = "extension"


@dataclass
class Action:
    type: ActionTypes
    umid: str  # unique model id
    object_name: str
    bone_name: str
    coords: Vector
    rotations: Vector = Vector([0, 0, 0, 1])


@dataclass
class Keyframe:
    frame: int
    actions: list[Action]


@dataclass
class Scene:
    name: str
    models: dict[str, str]  # umid: object_name
    keyframes: list[Keyframe]
