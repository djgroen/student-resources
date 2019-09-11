from PIL import Image, ImageDraw

class Ball:
  def __init__(self, x ,y , vx, vy):
    self.x = x
    self.y = y
    self.vx = vy
    self.vy = vy
    self.radius = 10

class Physics:
  def __init__(self):
    self.e = 1.0 # energy loss in bounce.
    self.g = -9.81 # Gravitational force (G=-9.81 [m/s2])

def step(ball, physics):
  ball.x = ball.x + 1*ball.vx 
  ball.y = ball.y + 1*ball.vy
  ball.vy -= physics.g
  if  ball.y < ball.radius:
    ball.vy = -ball.vy*physics.e
    ball.y = ball.radius

def draw_system(d, ball):
  """
  Draws a game of life grid.
  """
  x1 = ball.x - ball.radius
  x2 = ball.x + ball.radius
  y1 = ball.y - ball.radius
  y2 = ball.y + ball.radius
  d.ellipse([x1,y1,x2,y2],fill="#fff")



if __name__ == "__main__":

  steps = 10

  # make a blank image for the text, initialized to transparent text color
  base = Image.new('RGBA', (640,640), (0,0,0,0))

  b = [base]
  d = [ImageDraw.Draw(base)]

  ball = Ball(50.0, 50.0, 10.0, 10.0)
  physics = Physics()

  for i in range(0, steps):
    draw_system(d[-1], ball)
    b[-1].save("test{}.png".format(i))
      
    b.append(Image.new('RGBA', (640,640), (0,0,0,0)))
    d.append(ImageDraw.Draw(b[-1]))

    step(ball, physics)

  b[0].save("test.gif", save_all=True, append_images=b[1:], duration=100, loop=0)