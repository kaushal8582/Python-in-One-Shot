def dubg(func):
  def wrapper(*args,**kwargs):
      args_value = ', '.join(str(arg) for arg in args)
      kwargs_value = ', '.join( f"{k}={v}" for k,v in kwargs.items())
      print(f"Calling : {func.__name__} with args {args_value} and kwargs {kwargs_value}")
      return func(*args,**kwargs)
  return wrapper

@dubg
def greet(name,greeting="Hello"):
  print(f"{greeting} , {name}")
  
@dubg
def hello():
  print("Hello")


hello()
greet("chai",greeting="kaushal")
