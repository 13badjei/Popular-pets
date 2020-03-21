import pygal

piechart = pygal.Pie()
piechart.title =  'Favourite Pets'
piechart.add('Dog', 6)
piechart.add('Cat', 4)
piechart.add('Hamster', 3)
piechart.add('Fish', 2)
piechart.add('Snake', 1)
#piechart.render()

piechart2 = pygal.Pie()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
  if line:
    label, value = line.split(' ')
    piechart2.add(label, int(value))
  
file.close()

piechart2.render()