# ladder_riding
A laddering game implemented in Python

## Usage

> from ladder_riding import ladder
> ladder = ladder()
> ladder.run(Peoples=int , HLadders=int) # set people and Horizontal ladder numbers
> ladder.winner
> ladder.prize
> ladder.map # ladder map
> ladder.route # winner route to prize
> print(ladder.outText) # output for console
> ladder.draw().save('result.png') # save output as image file

> ####### draw options #######
> ladder.draw(max_width=int, max_height=int, BG_COLOR=(r,g,b), DEFAULT_COLOR=(r,g,b), PICKED_COLOR=(r,g,b)).save(filepath)

![ladder_console](https://user-images.githubusercontent.com/13087172/196333718-d8204fee-e653-4b75-a824-a5ebd3e92759.png)

![result](https://user-images.githubusercontent.com/13087172/196333742-2c5880ba-43ca-4012-a2d8-bd2da159b6bd.png)