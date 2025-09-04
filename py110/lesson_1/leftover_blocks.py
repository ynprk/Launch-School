"""
Leftover Blocks
You have a number of building blocks that can be used to build a valid structure. 
There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.
Write a program that, given the number of available blocks, 
calculates the number of blocks left over after building the tallest possible valid structure.

Tasks
You are provided with the problem description above. Your tasks for this step are:

Make notes of your mental model for the problem, including:
inputs and outputs.
explicit and implicit rules.
Write a list of clarifying questions for anything that isn't clear.

input: integer - number of building blocks
output: integer - number of blocks left over after building the tallest possible structure
explicit: 
    - building blocks are cubes
    - top layer is a single block
    - structure is built in layers
    - block in an upper layer must be supported by four blocks in a lower layer
    - block in a lower layer can support more than one block in an upper layer

implicit:
    - second from the top layer must contain at least 4 blocks
    - layer number correlates with blocks in a layer
        - the number of blocks in a layer is layer number * layer number
        - where top layer has layer number 1, second from the top has 2...

questions:
    - does the block in an upper layer need to be supported by exactly four blocks? yes
    - are the blocks equal sizes? yes
    - how to handle 0 => output 0
    - and negative integer inputs 
    - non-integer or empty inputs
    - what does "gaps between blocks" mean?
    - will there always be blocks left over? => no, 0 is valid output

data structure:
- list
    - index represents nth layer from the top (1st row is top row)
    - element at the index represents the number of blocks at that layer
    - [0, 1, 4, 9, 16...]

algorithm:
input: integer - number of building blocks
output: integer - number of blocks left over after building the tallest possible structure

1) given the number of building blocks, blocks
2) sum all cubes of natural numbers that are less than blocks, and set it to the variable sum
    e.g. if blocks = 20, sum = 1 + 4 + 9 + 16 = 30
    2a) start with cubed, then increment
    2b) add to sum
    loop this until sum >= blocks
3) compute and return left over blocks: sum - blocks

"""
def calculate_leftover_blocks(blocks):
    current_layer = 1
    blocks_remaining = blocks
    blocks_required = current_layer * current_layer

    while blocks_remaining >= blocks_required:
        blocks_remaining -= blocks_required
        current_layer += 1
        blocks_required = current_layer * current_layer
    
    return blocks_remaining
        
print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5)== 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True