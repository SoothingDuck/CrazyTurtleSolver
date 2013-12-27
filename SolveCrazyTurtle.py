from Grid import Grid

if __name__ == "__main__":

    g = Grid()
    g.init_crazy_turtle_game()

    c = g.get_cardset()

    first_card = c[0]

    g.set_card(first_card, 1, 1)

    input = [g]

    for i in range(3):
        output = []

        print "Debut iteration : %d, nombre grilles input = %d" % (i+1, len(input))

        for grid in input:
            output += grid.next_step()

        input = output

        print "Fin   iteration : %d, nombre grilles output = %d" % (i+1, len(input))

        print output[0]
        print output[0].get_cardset()
