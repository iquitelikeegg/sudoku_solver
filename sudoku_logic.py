""" This is the logic component for the sudoku solver """

def calculate(values):
    #print values

    validate(values)




def validate(values):
    #Must be a number
    #No more than one character
    errors = []
    count = 0
    for grid in values:
        count = count + 1
        print "count %d" % count
        print grid

        for item in grid:
            print item

            if item != "":

                try:
                    if int(item) >9 or int(item) <0:
                        errors.append("Number must be between 1 and 9")
                except ValueError:
                    print "This is an invalid input!"
