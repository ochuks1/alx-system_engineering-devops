#include "raycast.h"
#include <math.h>

// Define constants
#define MAP_WIDTH 10
#define MAP_HEIGHT 10
#define TILE_SIZE 64

// Map representation
int map[MAP_WIDTH][MAP_HEIGHT] = {
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 1, 1, 1, 0, 1, 0, 0, 1},
    {1, 0, 0, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 1, 1, 1, 0, 1, 0, 0, 1},
    {1, 0, 1, 0, 0, 0, 0, 0, 0, 1},
    {1, 0, 1, 0, 1, 0, 1, 0, 0, 1},
    {1, 0, 0, 0, 1, 0, 1, 0, 0, 1},
    {1, 0, 1, 1, 1, 0, 1, 0, 0, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
};

// Raycasting function
void cast_rays(SDL_Renderer *renderer, double camera_x, double camera_y, double angle) {
    int num_rays = 120;
    double fov = M_PI / 3.0; // 60 degrees
    double step = fov / num_rays;
    double ray_angle = angle - fov / 2.0;

    for (int i = 0; i < num_rays; i++) {
        double ray_x = camera_x;
        double ray_y = camera_y;
        double ray_dx = cos(ray_angle);
        double ray_dy = sin(ray_angle);
        int depth = 0;

        while (depth < 100) {
            ray_x += ray_dx * TILE_SIZE;
            ray_y += ray_dy * TILE_SIZE;

            int map_x = (int)(ray_x / TILE_SIZE);
            int map_y = (int)(ray_y / TILE_SIZE);

            if (map_x >= 0 && map_x < MAP_WIDTH && map_y >= 0 && map_y < MAP_HEIGHT) {
                if (map[map_x][map_y] == 1) {
                    // Draw wall
                    int wall_height = (int)(TILE_SIZE / (depth + 0.1));
                    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
                    SDL_RenderDrawLine(renderer, i * 10, HEIGHT / 2 - wall_height / 2, i * 10, HEIGHT / 2 + wall_height / 2);
                    break;
                }
            }

            depth++;
        }

        ray_angle += step;
    }
}
