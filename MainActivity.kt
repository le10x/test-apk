package com.ejemplo.miapp

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun Bundle?() {
        super.onCreate(savedInstanceState)
        setContent {
            // Aplicar el tema visual de Android (Material 3)
            MaterialTheme {
                Surface(
                    modifier = Modifier.fillMaxSize(),
                    color = MaterialTheme.colorScheme.background
                ) {
                    ScreenPrincipal()
                }
            }
        }
    }
}

@Composable
fun ScreenPrincipal() {
    // Variable de estado que recuerda el texto (equivalente al estado en Python)
    var textoLabel by remember { mutableStateOf("¡Hola desde Kotlin Nativo!") }

    // Contenedor vertical centrado
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(20.dp),
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        // Etiqueta de texto
        Text(
            text = textoLabel,
            style = MaterialTheme.typography.headlineMedium
        )
        
        // Espacio de separación entre el texto y el botón
        Spacer(modifier = Modifier.height(20.dp))

        // Botón interactivo
        Button(onClick = { 
            // Acción que se ejecuta al presionar el botón
            textoLabel = "¡El APK nativo funciona volando!" 
        }) {
            Text(text = "Presióname")
        }
    }
}
