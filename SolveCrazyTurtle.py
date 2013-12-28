import sys
from Grid import Grid

def iter_for_card(grid, card, verbose=True):
    
    grid.set_card(card, 1, 1)

    input = [grid]

    for i in range(8):
        mid_step = []

        if verbose:
            print "Debut iteration : %d, nombre grilles input = %d" % (i+1, len(input))

        for grid in input:
            mid_step += grid.next_step()

        if verbose:
            print "Mid   iteration : %d, nombre grilles mid_step = %d" % (i+1, len(mid_step))

        ## cleaning step
        output = []
        for grid in mid_step:
            if grid.exist_valid_card_for_all_next_places():
                output.append(grid)

        input = output

        if verbose:
            print "Fin   iteration : %d, nombre grilles output = %d" % (i+1, len(input))

        if len(input) == 0:
            return []

        if verbose:
            print output[0]
            print output[0].get_cardset()
            print "Nombre de cartes restantes : %d" % (len(output[0].get_cardset()))

    return input

if __name__ == "__main__":

    verbose = True

    g = Grid()
    g.init_crazy_turtle_game()

    all_card = g.get_cardset()


    for card in all_card:
        g = Grid()
        g.init_crazy_turtle_game()

        result = iter_for_card(g, card)

        if len(result) > 0:
            for grid in result:
                print grid

            sys.exit(0)
