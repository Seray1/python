# to create an emty set
cars = set()

# add elements to a set
cars.add("benz")
cars.add("toyota")
cars.add("acura")
cars.add("lambo")

print(cars)

#notice by the output, set are not in order because naturaly set are not in order

#in the example below, we added another benz to the set, but it will not reflect
#in the output because datas in set are unique
cars.add("benz")
cars.add("toyota")
cars.add("acura")
cars.add("lambo")
cars.add("benz")
print(cars)

#we can remove data from the set using the remove method
cars.add("benz")
cars.add("toyota")
cars.add("acura")
cars.add("lambo")

cars.remove("toyota")

print(cars)


#NOte; in 
