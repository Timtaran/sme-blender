import dataclasses
import json

from mathutils import Vector


class EnhancedJSONEncoder(json.JSONEncoder):
    """
    Usage: json.dumps(obj, cls=EnhancedJSONEncoder)
    """

    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        elif isinstance(o, Vector):
            try:
                return [o.x, o.y, o.z, o.w]
            except (TypeError, AttributeError):
                return [o.x, o.y, o.z]

        return super().default(o)
