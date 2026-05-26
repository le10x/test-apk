#include "SDL.h"

int main(int argc, char *argv[]) {
    SDL_Init(SDL_INIT_VIDEO);

    // Crear la ventana al tamaño completo de la pantalla del celular
    SDL_Window *window = SDL_CreateWindow(
        "App C++ en Android",
        SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED,
        1024, 768,
        SDL_WINDOW_SHOWN | SDL_WINDOW_FULLSCREEN
    );

    SDL_Renderer *renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    bool corriendo = true;
    SDL_Event evento;
    bool pantallaAzul = false;

    // Bucle principal de la aplicación
    while (corriendo) {
        while (SDL_PollEvent(&evento)) {
            if (evento.type == SDL_QUIT) {
                corriendo = false;
            }
            // Si el usuario toca la pantalla del celular
            if (evento.type == SDL_FINGERDOWN || evento.type == SDL_MOUSEBUTTONDOWN) {
                pantallaAzul = !pantallaAzul;
            }
        }

        // Cambiar el color de fondo según el estado
        if (pantallaAzul) {
            SDL_SetRenderDrawColor(renderer, 0, 0, 255, 255); // Azul
        } else {
            SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255); // Rojo
        }
        
        SDL_RenderClear(renderer);
        SDL_RenderPresent(renderer);
    }

    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();
    return 0;
}
