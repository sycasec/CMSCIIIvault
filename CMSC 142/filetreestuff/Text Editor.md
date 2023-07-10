# Making a Text Editor
## Main Idea
- a cursor splits the entire "file" (string, list elements, any) into:
	- before the cursor
	- after the cursor

## My idea
- each "character" is a list element (with the exception of `\n`)
- we know each line ends with `\n`
- we still have a cursor, and insert items right before the cursor (basically `list.insert()`)
- delete is just pop at cursor
- visual delete is still a thing i have to convene with the coding gods (think about for a while later)