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