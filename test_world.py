#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from npgameworld.world import World, WorldLogger


def main():
    world = World()
    world.init_hero()
    world.add_enemy_type()

    logger = WorldLogger(world)
    print(logger)

    logger.setLevel(logging.DEBUG)

    wg = world.world_gen()

    while True:
        wg.send(None)
        try:
            wg.send(1)
        except StopIteration:
            print('game over')


if __name__ == '__main__':
    main()
