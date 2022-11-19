start=int(input('start: '))
end=int(input('end: '))
grid=[
['', '', '', '', '', '', ''], 
['', '', '', '', '', '', ''], 
['', '', '', '', '', '', ''], 
['', '', '', '', '', '', ''], 
['', '', '', '', '', '', ''], 
['', '', '', '', '', '', ''], 
['', '', '', '', '', '', '']
]
x, y = 3, 3
direction='down'
for c in range(end-start+1):
    c=c+start
    grid[x][y]=c
    if direction == 'down':
        x, y = x+1, y
        if grid[x][y+1]=='':
            direction='right'
    elif direction == 'right':
        x, y = x, y+1
        if grid[x-1][y]=='':
            direction='up'
    elif direction == 'up':
        x, y = x-1, y
        if grid[x][y-1]=='':
            direction='left'
    elif direction == 'left':
        x, y = x, y-1
        if grid[x+1][y]=='':
            direction='down'
for x in range(len(grid)):
    print(grid[x])
