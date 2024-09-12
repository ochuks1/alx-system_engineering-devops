#include "game.h"
#include "raycasting.h"

void draw_wall(int x, int wall_height, int color) {
    SDL_SetRenderDrawColor(renderer, color, color, color, 255);
    SDL_RenderDrawLine(renderer, x, (WIN_HEIGHT - wall_height) / 2,
            x, (WIN_HEIGHT + wall_height) / 2);
}

void render_scene(Player player) {
    SDL_SetRenderDrawColor(renderer, 135, 206, 235, 255);  // Sky color
    SDL_RenderClear(renderer);
    cast_rays(player);
    SDL_RenderPresent(renderer);
}
