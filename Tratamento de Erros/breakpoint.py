"""
Podemos usar a função breakpoint() para parar a execução do código e utilizar o Python Debugger

Versão 3.7+: função integrada breakpoint()
Versão 3.7-: é necessário importar pdb e utilizar a função pdb.set_trace()

1. continue (c):

    This is the most common command to resume normal script execution.
    When you type c at the (Pdb) prompt, the debugger will exit, and your program will continue running from the point where it was stopped.
    It will continue running until it reaches another breakpoint (if set) or finishes execution.

2. next (n):

    This command executes only the next line of code in the current function and then stops again at the beginning of the next line.
    It's useful for stepping through your code line by line.

3. step (s):

    Similar to next, but step will step into any function calls encountered on the current line.
    This allows you to debug code within called functions as well.

4. return (r):

    This command resumes execution and exits the current function immediately, returning control to the calling function.
    It's helpful for skipping the remaining code within the current function.

5. jump (j):

    This command allows you to jump to a specific line number in your code and resume execution from there.
    You can specify the line number as an argument to the jump command, for example: j 42.
"""
#import pdb

#pdb.set_trace()

breakpoint()
a = 10

b = 20

def soma():
    c = a+b
    return c

print(soma())
