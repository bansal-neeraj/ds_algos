"""
getattr(object, name[, default]) -> value

    Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y.
    When a default argument is given, it is returned when the attribute doesn't
    exist; without it, an exception is raised in that case.

"""
class MyCar:
    def __init__(self):
        self.x = 10
        self.y = 20


a = MyCar()

print(a.x)
print(a.y)
print(getattr(a,'z','abc123'))
print(getattr(a,'x','abc123'))
