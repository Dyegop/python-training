from inspect import Signature, Parameter

class Shape:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

class Circle(Shape):
    def __init__(self, radius: float, **kwargs):
        super().__init__(**kwargs)
        self.radius = radius

    # __signature__ attribute is a typing.Signature object that describes the arguments that the class expects.
    __signature__ = Signature(
        parameters=[
            Parameter('radius', Parameter.POSITIONAL_OR_KEYWORD, annotation=float),
            Parameter('x', Parameter.POSITIONAL_OR_KEYWORD, annotation=float),
            Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, annotation=float),
        ]
    )


c = Circle(3)