print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do:')
print('\n newLines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started*500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans,jars,crates

start_point = 10000
beans,jars,crates = secret_formula(start_point)

#This is another way of formatting a string
print("With a starting point of: {}".format(start_point))
# Its similar to a f"" string
print(f"We'd have {beans}, {jars}, and {crates} crates")

start_point = start_point / 10

print("We can also do that this way:")

formmula = secret_formula(start_point)
# this is an easy way to apply a list to a format starting
print("We'd have {} beans, {} jars, and {} crates.".format(*formmula))
