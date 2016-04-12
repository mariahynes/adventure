from data import locations

directions={
    "west": (-1,0),
    "east": (1,0),
    "north": (0, -1),
    "south": (0,1),
}

position = (0,0)

while True:
    location = locations[position]
    print "You are at the %s" % location

    valid_directions = {}

    for k,v in directions.iteritems():
        possible_position = (position[0] + v[0], position[1] + v[1])
        possible_location = locations.get(possible_position)
        if possible_location:
            print "to the %s is a %s" %(k, possible_location)
            valid_directions[k] = possible_position

    chosen_direction = None
    while chosen_direction == None:
        direction = raw_input("Which direction do you want to go?\n")
        chosen_direction = valid_directions.get(direction)

        if chosen_direction == None:
            print "Please choose a valid direction!"
        else:
            position = valid_directions[direction]