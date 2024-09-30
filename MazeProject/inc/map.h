#ifndef MAP_H
#define MAP_H

#include "game.h"

// Function prototypes
void draw_map(SDL_Renderer *renderer, int map[MAP_WIDTH][MAP_HEIGHT]);
void load_map(const char *filename, int map[MAP_WIDTH][MAP_HEIGHT]);

#endif // MAP_H
