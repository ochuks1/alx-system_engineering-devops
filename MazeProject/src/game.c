#include "game.h"
#include <SDL2/SDL.h>

// Initializes SDL, creates window and renderer
void init_sdl(SDL_Window **window, SDL_Renderer **renderer) {
    SDL_Init(SDL_INIT_VIDEO);
    *window = SDL_CreateWindow("3D Maze Game", SDL_WINDOWPOS_CENTERED,
                               SDL_WINDOWPOS_CENTERED, WIN_WIDTH, WIN_HEIGHT,
                               SDL_WINDOW_SHOWN);
    *renderer = SDL_CreateRenderer(*window, -1, SDL_RENDERER_ACCELERATED);
}

// Handles player input to update position
void handle_input(Player *player, SDL_Event *event) {
    const Uint8 *state = SDL_GetKeyboardState(NULL);

    if (state[SDL_SCANCODE_W]) player->y -= player->speed;
    if (state[SDL_SCANCODE_S]) player->y += player->speed;
    if (state[SDL_SCANCODE_A]) player->x -= player->speed;
    if (state[SDL_SCANCODE_D]) player->x += player->speed;
}

// Cleans up SDL resources
void clean_up(SDL_Window *window, SDL_Renderer *renderer) {
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
}
