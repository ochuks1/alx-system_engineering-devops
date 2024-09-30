#include "raycasting.h"

// Calculates the angle of the current ray
float calculate_ray_angle(int ray, Player player) {
    return player.angle - (FOV / 2) + (ray / (float)WIN_WIDTH) * FOV;
}
