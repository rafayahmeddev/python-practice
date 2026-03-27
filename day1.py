# My first python program implementing a stack 

stack = [0 for i in range(5)]
pointer = 0


def push(n):
    global pointer, stack

    if pointer > 5:
        print("OverFlow occurred")

    else:
        stack[pointer] = n
        pointer += 1


def pull():
    global pointer, stack

    if pointer == 0:
        print("Underflow occurred")

    else:
        pointer -= 1 
        stack[pointer] = 0
        print(stack[pointer])

push(1)
push(12)
push(13)
pull()
print(stack)
print("hello")

