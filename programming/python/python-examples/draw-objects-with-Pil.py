from PIL import Image, ImageDraw, ImageFont




def round_rectangle(d, x, y, size, r, color="white"):
  """
  Draw a rounded rectangle:
  r = radius
  """
  w, h = size
  d.arc([x, y, x+r, y+r], 180, 270, color) #NW
  d.arc([x+w-r, y, x+w, y+r], 270, 0, color) #NE
  d.arc([x+w-r, y+h-r, x+w, y+h], 0, 90, color) #SE
  d.arc([x, y+h-r, x+r, y+h], 90, 180, color) #SW

  hr = r/2

  d.line([x+hr,y,x+w-hr,y],color) #N
  d.line([x+w,y+hr,x+w,y+h-hr],color) #E
  d.line([x+hr,y+h,x+w-hr,y+h],color) #S
  d.line([x,y+hr,x,y+h-hr],color) #W

  return d

def draw_arrow(d, x, y, length, orientation="N", color="white"):
  rw = 12
  rh = 20
  x2 = -1
  y2 = -1

  if orientation == "N":
    x2 = x
    y2 = y-length
    poly_coords = [x2, y2, x2+rw, y2+rh, x2-rw, y2+rh]

  if orientation == "E":
    x2 = x+length
    y2 = y
    poly_coords = [x2, y2, x2-rh, y2+rw, x2-rh, y2-rw]

  if orientation == "S":
    x2 = x
    y2 = y+length
    poly_coords = [x2, y2, x2+rw, y2-rh, x2-rw, y2-rh]

  if orientation == "W":
    x2 = x-length
    y2 = y
    poly_coords = [x2, y2, x2+rh, y2+rw, x2+rh, y2-rw]

  d.line([x, y, x2, y2], width=3, fill=color)
  d.polygon(poly_coords, fill=color)
  return d



def draw_dials(d, x,y, c,a,s,e):
  d = round_rectangle(d, x, y, (100, 100), 20)
  if c:
    d = draw_arrow(d, x+50, y+50, 50, "N", "#f70")
  if a:
    d = draw_arrow(d, x+50, y+50, 50, "E", "#ff0")
  if s:
    d = draw_arrow(d, x+50, y+50, 50, "S", "#0d0")
  if e:
    d = draw_arrow(d, x+50, y+50, 50, "W", "#88f")





if __name__ == "__main__":

  # get an image
  #base = Image.open('test.png').convert('RGBA')

  # make a blank image for the text, initialized to transparent text color
  base = Image.new('RGBA', (1024,1024), (0,0,0,0))

  # get a font
  fnt = ImageFont.truetype('Pillow/Tests/fonts/FreeMono.ttf', 40)
  # get a drawing context
  d = ImageDraw.Draw(base)

  # draw text, half opacity
  d.text((10,10), "Hello", font=fnt, fill=(255,255,255,128))
  # draw text, full opacity
  d.text((10,60), "World", font=fnt, fill=(255,255,255,255))

  d = draw_dials(d, 400, 50, True, True, True, True)

  #out = Image.alpha_composite(base, txt)

  #[(x0, y0), (x1, y1)]

  base.show()


