#include "game.h"

void init_ray_vars(Player player, float *ray_dir_x, float *ray_dir_y, 
                    int *map_x, int *map_y, float ray_angle) {
    *ray_dir_x = cos(ray_angle);
    *ray_dir_y = sin(ray_angle);
    *map_x = (int)player.x;
    *map_y = (int)player.y;
}

void init_step_side_dist(float ray_dir_x, float ray_dir_y, Player player,
                         int *step_x, int *step_y, float *side_dist_x, 
                         float *side_dist_y, float *delta_dist_x, 
                         float *delta_dist_y) {
    *delta_dist_x = fabs(1 / ray_dir_x);
    *delta_dist_y = fabs(1 / ray_dir_y);

    if (ray_dir_x < 0) {
        *step_x = -1;
        *side_dist_x = (player.x - (int)player.x) * (*delta_dist_x);
    } else {
        *step_x = 1;
        *side_dist_x = ((int)player.x + 1.0 - player.x) * (*delta_dist_x);
    }
    if (ray_dir_y < 0) {
        *step_y = -1;
        *side_dist_y = (player.y - (int)player.y) * (*delta_dist_y);
    } else {
        *step_y = 1;
        *side_dist_y = ((int)player.y + 1.0 - player.y) * (*delta_dist_y);
    }
}

float perform_dda(int map[MAP_WIDTH][MAP_HEIGHT], int *map_x, 
                  int *map_y, int step_x, int step_y, 
                  float *side_dist_x, float *side_dist_y, 
                  float delta_dist_x, float delta_dist_y, 
                  int *hit_side) {
    int hit = 0;
    while (!hit) {
        if (*side_dist_x < *side_dist_y) {
            *side_dist_x += delta_dist_x;
            *map_x += step_x;
            *hit_side = 0;
        } else {
            *side_dist_y += delta_dist_y;
            *map_y += step_y;
            *hit_side = 1;
        }
        if (map[*map_x][*map_y] == 1) hit = 1;
    }
    return (*hit_side == 0) ? 
           (*map_x - (float)*map_x + (1 - step_x) / 2) / delta_dist_x :
           (*map_y - (float)*map_y + (1 - step_y) / 2) / delta_dist_y;
}
