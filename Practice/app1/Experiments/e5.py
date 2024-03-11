# using coffee function and returning new procedure
def coffee():
    procedure = "blend the beans and make a coffee using filter with machine"
    new_procedure = procedure.title()
    return new_procedure


bring_coffee = coffee()
print(bring_coffee)
