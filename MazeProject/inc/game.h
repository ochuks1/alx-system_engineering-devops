#ifndef GAME_H
#define GAME_H

#include <SDL2/SDL.h>

// Screen dimensions
#define WIN_WIDTH 800
#define WIN_HEIGHT 600

// Field of View
#define FOV 60.0

// Map dimensions
#define MAP_WIDTH 5
#define MAP_HEIGHT 5

// Player structure definition
typedef struct {
    float x;       // Player's x position
    float y;       // Player's y position
    float angle;   // Player's view angle
    float speed;   // Player's movement speed
} Player;

// Function prototypes
void init_sdl(SDL_Window **window, SDL_Renderer **renderer);
void handle_input(Player *player, SDL_Event *event);
void clean_up(SDL_Window *window, SDL_Renderer *renderer);

#endif // GAME_H
