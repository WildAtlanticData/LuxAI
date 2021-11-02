from utils import *

DIRECTIONS = Constants.DIRECTIONS
game_state = None


def agent(observation, configuration):
    global game_state

    ### Do not edit ###
    if observation["step"] == 0:
        game_state = Game()
        game_state._initialize(observation["updates"])
        game_state._update(observation["updates"][2:])
        game_state.id = observation.player
    else:
        game_state._update(observation["updates"])
    
    actions = []

    ### AI Code goes down here! ### 
    player = game_state.players[observation.player]
    opponent = game_state.players[(observation.player + 1) % 2]
    width, height = game_state.map.width, game_state.map.height

    # determine the tiles that have resources
    resource_tiles = find_resources(game_state)
    empty_tiles = find_empty_space(game_state)
    empty_tiles_pos = [val.pos for val in empty_tiles]

    # we iterate over all our units and do something with them
    for unit in player.units:

        if unit.is_worker() and unit.can_act():

            closest_resource_tile = None
            
            all_ok = True

            for c in player.cities.values():
                if c.fuel < 300:
                    all_ok = False
                    break

            if all_ok and unit.pos in empty_tiles_pos:
                actions.append(unit.build_city())

            elif all_ok:
                # get closest citytile
                # find the closest empty tile to that city tile
                # move there
                # build city
                closest_empty_tile = find_closest_emtpy_space(unit.pos, empty_tiles)
                actions.append(unit.move(unit.pos.direction_to(closest_empty_tile.pos)))

            #elif unit.pos in empty_tiles:
            #    action = unit.build_city()
            #    actions.append(action)

            elif unit.get_cargo_space_left() > 0:

                closest_resource_tile = find_closest_resources(unit.pos, player, resource_tiles)

                if closest_resource_tile is not None:

                    actions.append(unit.move(unit.pos.direction_to(closest_resource_tile.pos)))
            else:
                # if unit is a worker and there is no cargo space left, and we have cities, lets return to them
                closest_city_tile = find_closest_city_tile(unit.pos, player)
                if closest_city_tile is not None:
                    move_dir = unit.pos.direction_to(closest_city_tile.pos)
                    actions.append(unit.move(move_dir))

    return actions
