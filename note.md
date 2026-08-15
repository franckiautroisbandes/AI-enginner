Day 1 notes
Python manages variables using scopes, which determine where a variable can be seen or accessed in your code

[ L ] Local     -> Defined inside the current function
   [ E ] Enclosing -> Inside an outer function (nested functions)
     [ G ] Global    -> Top level of the script or module
       [ B ] Built-in  -> Python's native names (e.g., len, print, dict)


You can read a global variable from inside a function automatically . However, if you try to modify it directly, Python creates a brand-new local variable with the same name instead of updating the global one 


In Python, every variable points to an object in your computer's memory. Whether you can change that object after creation depends on its data type

Examples: Lists (list), Dictionaries (dict), Sets (set)

Objects that completely forbid modifications once they are created

Examples: Strings (str), Tuples (tuple), Numbers (int, float), Booleans (bool)


The challenge I faced was with the match, the bubble sort mostly the algorith part and the datastructure part.
----------------------------------------------------------------------------------------------------------

Day 2 notes
LIST
"I have a collection of things."
        ↓
Position matters
Duplicates are allowed
I expect to modify it


TUPLE
"I have a fixed group of things."
        ↓
Position matters
Duplicates are allowed
I don't want the collection modified


SET
"I care about unique things."
        ↓
Duplicates disappear
Membership is important
Fast lookup is important


DICT
"I need to associate one thing with another."
        ↓
key → value
Fast lookup by key
Data has named attributes

A linked list is like a chain where each link, or node, holds two things: its data and a pointer to the next link. The list itself only knows where the very first link—the head—is located. Because of this, you can't jump straight to a specific item like you can in a regular Python list; you have to start at the beginning and follow the chain one link at a time. That is why finding something takes O(n) time instead of a Python list's instant O(1) lookup."

For the two_sum the result shows that Set runs exponentially faster than Brute force.
Brute force:
Result: True
Time: 0.051751899998635054 seconds

Set:
Result: True
Time: 5.909998435527086e-05 seconds
