[app]
title = Mi App Cxx
package.name = miappcxx
package.domain = org.ejemplo
source.dir = .
source.include_exts = cpp,h
version = 0.1

# AQUÍ ESTÁ EL TRUCO: Le indicamos que use SDL2 para compilar C++
requirements = sdl2

orientation = portrait
fullscreen = 1
android.archs = armeabi-v7a, arm64-v8a
android.allow_backup = True
