#include "game.h"

void handle_input(Player *player) {
    SDL_Event e;
    while (SDL_PollEvent(&e) != 0) {
        if (e.type == SDL_QUIT) game_running = 0;
        if (e.type == SDL_KEYDOWN) {
            if (e.key.keysym.sym == SDLK_LEFT) player->angle -= 0.1;
            if (e.key.keysym.sym == SDLK_RIGHT) player->angle += 0.1;
        }
    }
}
