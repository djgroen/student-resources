# A simple example on how you can track a variable through a Python stack using particularly trivial print statements.

def z(parameter, parameter_I_want_to_debug=""):
  print("Function z: parameter_I_want_to_debug = %s" % (parameter_I_want_to_debug))

def u(parameter, parameter_I_want_to_debug=""):
  print("Function u: parameter_I_want_to_debug = %s" % (parameter_I_want_to_debug))
  z(parameter, parameter_I_want_to_debug)

def a(parameter, parameter_I_want_to_debug=""):
  print("Function a: parameter_I_want_to_debug = %s" % (parameter_I_want_to_debug))
  u(parameter, parameter_I_want_to_debug)
  
if __name__ == "__main__":
  a(1, "we want to debug this")
