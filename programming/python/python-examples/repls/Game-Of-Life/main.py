from PIL import Image, ImageDraw
import numpy as np
from scipy.signal import convolve2d

def step(life_grid):
  # Count the number of neighbours for each cell.
  kernel = np.array([[1,1,1],[1,0,1],[1,1,1]])
  neigh_counts = convolve2d(life_grid,kernel,'same')

  print(neigh_counts)
  for x in range(0, life_grid.shape[0]):
    for y in range(0, life_grid.shape[1]):

      # Cell is alive
      if life_grid[x][y] == 1:
        if neigh_counts[x][y] == 2:
          pass
        elif neigh_counts[x][y] == 3:
          pass 
        else:
          life_grid[x][y] = 0
      
      # Cell is dead
      else:
        if neigh_counts[x][y] == 3:
          life_grid[x][y] = 1

def draw_grid(d, life_grid):
    """
    Draws a game of life grid.
    """

    for x in range(0, life_grid.shape[0]):
        for y in range(0, life_grid.shape[1]):
            if life_grid[x][y] == 1:
                d.ellipse([x*50,y*50,(x+1)*50,(y+1)*50],fill="#fff")
            else:
                d.ellipse([x*50,y*50,(x+1)*50,(y+1)*50],fill="#888")


if __name__ == "__main__":

  xsize = 10
  ysize = 10
  steps = 5

  # make a blank image for the text, initialized to transparent text color
  base = Image.new('RGBA', (xsize*50+10,ysize*50+10), (0,0,0,0))

  b = [base]
  d = [ImageDraw.Draw(base)]

  life_grid = np.zeros((xsize, ysize), dtype=int)

  #put an example block
  life_grid[5][5] = 1
  life_grid[5][6] = 1
  life_grid[5][7] = 1

  for i in range(0, steps):
      draw_grid(d[-1], life_grid)
      
      b.append(Image.new('RGBA', (1024,1024), (0,0,0,0)))
      d.append(ImageDraw.Draw(b[-1]))

      step(life_grid)

  b[0].save("test.gif", save_all=True, append_images=b[1:], duration=1000, loop=0)