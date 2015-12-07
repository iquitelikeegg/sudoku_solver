""" This is the logic component for the sudoku solver """

def calculate(values):
    #print values

    print validate(values)



def validate(values):
    #Must be a number
    #No more than one character
    errors = []
    count = 0
    for grid in values:
        count = count + 1
        print "count %d" % count
        gridErrors = []

        for square in grid:
            squareErrors = []
            print square

            if square != "":

                try:
                    if int(square) >9 or int(square) <0:
                        squareErrors.append("Number must be between 1 and 9")
                except ValueError:
                    squareErrors.append("This is an invalid input")
            gridErrors.append(squareErrors)
        errors.append(gridErrors)

    return errors

            # #if square == " ":
            #             try:
            #                 if int(square) >9 or int(square) <0:
            #                     errors.append("Number must be between 1 and 9")
            #             except ValueError:
            #                 print "This is an invalid input!"
