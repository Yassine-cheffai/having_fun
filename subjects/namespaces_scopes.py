# https://realpython.com/python-namespaces-scope/

"""
A namespace is a collection of currently defined symbolic names along with information about the object that each name references. You can think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. Each key-value pair maps a name to its corresponding object.

there are four types of namespaces:
    - Built-In
    - Global
    - Enclosing
    - Local

The scope of a name is the region of a program in which that name has meaning. The interpreter determines this at runtime based on where the name definition occurs and where in the code the name is referenced.

 LEGB rule: The interpreter searches for a name from the inside out, looking in the local, enclosing, global, and finally the built-in scope
If the interpreter doesn’t find the name in any of these locations, then Python raises a NameError exception.


Earlier in this tutorial, when namespaces were first introduced, you were encouraged to think of a namespace as a dictionary in which the keys are the object names and the values are the objects themselves. In fact, for global and local namespaces, that’s precisely what they are! Python really does implement these namespaces as dictionaries.

Note: The built-in namespace doesn’t behave like a dictionary. Python implements it as a module.


>>> globals()["__builtins__"].round(12.9)
>>> 13

>>> globals()['y'] = 3.14159
>>> y
3.14159

>>> x = 20
>>> def f():
...     global x
...     x = 40
...     print(x)



To modify x in the enclosing scope from inside g(), you need the analogous keyword nonlocal. Names specified after the nonlocal keyword refer to variables in the nearest enclosing scope:

>>> def f():
...     x = 20
...
...     def g():
...         nonlocal x
...         x = 40
...
...     g()
...     print(x)
...

>>> f()
40


Best Practices
Even though Python provides the global and nonlocal keywords, it’s not always advisable to use them.

When a function modifies data outside the local scope, either with the global or nonlocal keyword or by directly modifying a mutable type in place, it’s a kind of side effect similar to when a function modifies one of its arguments. Widespread modification of global variables is generally considered unwise, not only in Python but also in other programming languages.

As with many things, this is somewhat a matter of style and preference. There are times when judicious use of global variable modification can reduce program complexity.

In Python, using the global keyword at least makes it explicit that the function is modifying a global variable. In many languages, a function can modify a global variable just by assignment, without announcing it in any way. This can make it very difficult to track down where global data is being modified.

All in all, modifying variables outside the local scope usually isn’t necessary. There’s almost always a better way, usually with function return values.
"""
