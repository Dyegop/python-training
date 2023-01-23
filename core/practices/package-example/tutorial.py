# Without __init__.py file
# from resources.module_one import One
# from resources.module_two import Two

# o1 = One()
# o2 = Two()

# With __init__.py file
import resources

o1 = resources.One()
o2 = resources.Two()

# If we delete the lines "from module_one import One" and "from module_two import Two" from the __init__.py file,
# we will not be able to access One() and Two() class directly from resources