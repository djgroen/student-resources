# Image Projection onto Sphere
# Image from: https://en.wikipedia.org/wiki/Equirectangular_projection
#(By Strebe - Own work, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=16115228)

# This is a modified version of the recipe found at:
# http://code.activestate.com/recipes/580695-image-projection-onto-sphere/

import math
from PIL import Image

def render_world(xyr, xzr, yzr, imgxOutput, imgyOutput):
  pi2 = math.pi * 2
  # 3D Sphere Rotation Angles (arbitrary)
  xy = -pi2 * xyr
  xz = -pi2 * xzr
  yz = -pi2 * yzr
  sxy = math.sin(xy); cxy = math.cos(xy)
  sxz = math.sin(xz); cxz = math.cos(xz)
  #syz = math.sin(yz); cyz = math.cos(yz)
  imageInput = Image.open("Equirectangular_projection_SW.png")
  (imgxInput, imgyInput) = imageInput.size
  pixelsInput = imageInput.load()
  imageOutput = Image.new("RGB", (imgxOutput, imgyOutput))
  pixelsOutput = imageOutput.load()
  # define a sphere behind the screen
  xc = (imgxOutput - 1.0) / 2
  yc = (imgyOutput - 1.0) / 2
  zc = min((imgxOutput - 1.0), (imgyOutput - 1.0)) / 2
  r = min((imgxOutput - 1.0), (imgyOutput - 1.0)) / 2
  # define camera view point
  xo = (imgxOutput - 1.0) / 2
  yo = (imgyOutput - 1.0) / 2
  zo = -min((imgxOutput - 1.0), (imgyOutput - 1.0))
  xoc = xo - xc
  yoc = yo - yc
  zoc = zo - zc
  doc2 = xoc * xoc + yoc * yoc + zoc * zoc
  for yi in range(imgyOutput):
    for xi in range(imgxOutput):
      xio = xi - xo
      yio = yi - yo
      zio = 0.0 - zo
      dio = math.sqrt(xio * xio + yio * yio + zio * zio)
      xl = xio / dio
      yl = yio / dio
      zl = zio / dio
      dot = xl * xoc + yl * yoc + zl * zoc
      val = dot * dot - doc2 + r * r
      if val >= 0: # if there is line-sphere intersection
        if val == 0: # 1 intersection point
          d = -dot
        else: # 2 intersection points => choose the closest
          d = min(-dot + math.sqrt(val), -dot - math.sqrt(val))
          xd = xo + xl * d
          yd = yo + yl * d
          zd = zo + zl * d
          x = (xd - xc) / r
          y = (yd - yc) / r
          z = (zd - zc) / r
          x0=x*cxy-y*sxy;y=x*sxy+y*cxy;x=x0 # xy-plane rotation
          x0=x*cxz-z*sxz;z=x*sxz+z*cxz;x=x0 # xz-plane rotation 
          lng = (math.atan2(y, x) + pi2 + yz) % pi2
          lat = math.acos(z)
          ix = int((imgxInput - 1) * lng / pi2 + 0.5)
          iy = int((imgyInput - 1) * lat / math.pi + 0.5)
          try:
            pixelsOutput[xi, yi] = pixelsInput[ix, iy]
          except:
            pass
  return imageOutput

if __name__ == "__main__":

  imageOutput = render_world(0.25,0.25,0.0,384,384)
  imageOutput.save("World.png", "PNG")

  xsize = 384
  ysize = 384
  steps = 10

  b = [render_world(0.25,0.25,0.0,xsize,ysize)]

  for i in range(0, steps):
      
      b.append(render_world(0.25, 0.25, (0.0+float(i)/float(steps))%1.0,xsize,ysize))

  b[0].save("test.gif", save_all=True, append_images=b[1:], duration=100, loop=0)