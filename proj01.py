# Brayan Jererz, October 27, 2018 PSIS 2105 Project number 01,Comments below.

# Asking the user for information about the  garden.
# step 1 insert the side of the square in feet.
# step 2 insert the space between plants in feet.
# step 3 insert depth of flowerbeds in feet.
# step 4 insert depth of garden fill in feet.

#Make Calculations
# step 5 calculate area of the garden.
# step 6 calculate radius of the circle flowerbed.
# step 7 calculate area of the circle flowerbed.
# step 8 calculate area of semicircle flowerbed.
# step 9 calculate total area of all flowerbeds.
# step 10 calculate area of garden fill.

# step 11 calculate number of flowers in circle flowerbed.
# step 12 calculate number of flowers in semicircle.
# step 13 calculate the total number of flowers.

# step 14 calculate volume of soil in the circle flowerbed.
# step 15 calculate cubic yards of soil in the circle flowerbed.
# step 16 calculate voulme of soil in one semicircle flowerbed.
# step 17 calculate cubic yards of soil in one semicircle flowerbed.
# step 18 calculate the total cubic yards of soil for the garden.

# step 19 calculate volume of garden fill of the garden.
# step 20 calculate the total cubic yards of fill material for the garden


import math

# Steps 1-4
side = float(input ("what is side measurment of this square garden in feet?"))  # Makes input to an integer
print ("The side of the garden will be",side,"feet")

spaceOfPlants = float(input ("what is the space between each plant in feet?"))  # Makes input to a decimal number
print ("The space between each plant will be",spaceOfPlants,"feet")

depth_flowerbeds = float(input ("what is the depth of all the flowerbeds in feet?"))  # Makes input to a decimal number
print ("The depth of all the flowerbeds will be",depth_flowerbeds,"feet")

depth_gardenFill = float(input ("what is the depth of the garden fill in feet?"))  # Makes input to a decimal number
print ("The depth of the the garden fill will be",depth_gardenFill,"feet")

# Steps 5-10
areaOfGarden = side * side                                      # Calculates area formula
radiusOfCircleFlowerbed = side/4                                # Calculates radius [R=L/4]
areaOfCircleFlowerbed = math.pi * radiusOfCircleFlowerbed **2   # Calculates area of circle [Pi*r^2]

# Calculates area of semicircle [circle /2 = area of one semicircle]
areaOfSemicircleFlowerbed = areaOfCircleFlowerbed/2

# Circle area + all semicircles  areas = total area
totalAreaOfFlowerbeds = areaOfCircleFlowerbed + areaOfSemicircleFlowerbed * 4
areaOfGardenFill = areaOfGarden - totalAreaOfFlowerbeds         # Garden area - area of flowerbeds = area of fill


##steps 11-13

# Circle area/plant spacing squared = number of flowers, rounded to the nearest tenths place
numberFlowersCircleFlowerbed = int(areaOfCircleFlowerbed/spaceOfPlants**2)
print ("There can be",numberFlowersCircleFlowerbed," flowers in the circle flowerbed")

# Semicircle area/plant spacing squared = number of flowers,round to the nearest whole number
numberFlowersSemicircleFlowerbed = int(areaOfSemicircleFlowerbed/spaceOfPlants**2)
print ("There can be",numberFlowersSemicircleFlowerbed,"flowers in a semicircle flowerbed")

# Circle flowers + the all semicircles flowers = total number of flowers, rounded to the nearest tenths place
totalNumberOfFlowers =  int(numberFlowersCircleFlowerbed + numberFlowersSemicircleFlowerbed * 4)
print ("Total number of flowers that is need for the garden is",totalNumberOfFlowers) 

#steps 14-18

# Area of circle * flowerbed depth = volume of circle
volumeOfSoilCircleFlowerbed = areaOfCircleFlowerbed * depth_flowerbeds

# Volume of circle/27 = soil cubic yards of circle(converting cubic feet to cubic yards)
cubicYardsSoilCircleFlowerbed = volumeOfSoilCircleFlowerbed/27

# Rounded to the nearest tenths place
print (round(cubicYardsSoilCircleFlowerbed,1),"cubic yards of soil can fit in the circle flowerbed")

volumeOfSoilSemicircleFlowerbed = volumeOfSoilCircleFlowerbed/2         # Volume of circle/2 = volume of semicircle

# Volume of semicircle/27 = soil cubic yards of semicircle(converting cubic feet to cubic yards)
cubicYardsSoilSemicircleFlowerbed = volumeOfSoilSemicircleFlowerbed/27

# Rounded to the nearest tenths place
print (round(cubicYardsSoilSemicircleFlowerbed,1),"cubic yards of soil can fit in the semicircle flowerbed")

# Cubic yards of circle + cubic yards of all semicircles = total cubic yards of soil
totalCubicYardsSoilGarden = cubicYardsSoilCircleFlowerbed + (cubicYardsSoilSemicircleFlowerbed * 4)

# Rounded to the nearest tenths place
print ("The total number of cubic yards of soil need for the garden is",round(totalCubicYardsSoilGarden,1))

#steps 19&20

# Area fill * depth = volume of fill
volumeOfGardenFill = areaOfGardenFill * depth_gardenFill

# Volume fill/27 = total cubic yards of fill (converting cubic feet to cubic yards)
totalCubicYardsOfFillGarden = volumeOfGardenFill/27

# Rounded to the nearest tenths place
print ("The total number of cubic yards of fill material need for the is",round(totalCubicYardsOfFillGarden,1))





