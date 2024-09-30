#ifndef RAYCASTING_H
#define RAYCASTING_H

#include "game.h"

// Function prototypes
void cast_rays(Player player, SDL_Renderer *renderer);
float calculate_ray_angle(int ray, Player player);
void update_side_dist(float ray_angle, Player player, float *side_dist_x,
                      float *side_dist_y, int *step_x, int *step_y);
float perform_dda(int map[MAP_WIDTH][MAP_HEIGHT], int *map_x, int *map_y,
                   int step_x, int step_y, float *side_dist_x, float *side_dist_y,
                   float delta_dist_x, float delta_dist_y, int *hit_side);
void render_wall(SDL_Renderer *renderer, int ray, float wall_dist);

#endif // RAYCASTING_H
