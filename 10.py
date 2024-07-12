'Friends''Names'

['Kelvin', 'Desmond', 'Percy', 'Eric', 'Philip', 'Gabriel']

List-of-tuples
[('Kelvin',6), ('Desmond',7), ('Percy',5), ('Eric',4), ('Philip',6), ('Gabriel',)]

friends = ['Kelvin', 'Desmond', 'Percy', 'Eric', 'Philip', 'Gabriel']
name_lengths = [(name, len(name)) for name in friends]
print(name_lengths)
