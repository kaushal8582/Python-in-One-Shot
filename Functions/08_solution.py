def print_kwargs(**kwargs):
  for key , value in kwargs.items():
    print(f"{key} : {value}")

print_kwargs(power="laser",name="shaktiman")
print_kwargs(name="shaktiman")
print_kwargs(power="laser",name="shaktiman",sex="male")