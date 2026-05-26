from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class MiAplicacion(MDApp):
    def build(self):
        # Definir el tema visual (Colores estilo Android)
        self.theme_cls.primary_palette = "Purple"
        self.theme_cls.theme_style = "Dark"

        # Crear el contenedor principal centrado
        diseño = MDBoxLayout(orientation='vertical', padding=20, spacing=20, adaptive_size=True)
        diseño.pos_hint = {"center_x": .5, "center_y": .5}

        # Crear una etiqueta de texto
        self.etiqueta = MDLabel(
            text="¡Hola desde Python!", 
            halign="center", 
            font_style="H5"
        )

        # Crear un botón
        boton = MDRaisedButton(
            text="Presióname", 
            on_release=self.cambiar_texto
        )

        # Agregar los elementos al diseño
        diseño.add_widget(self.etiqueta)
        diseño.add_widget(boton)

        # Crear la pantalla y añadir el diseño
        pantalla = MDScreen()
        pantalla.add_widget(diseño)
        
        return pantalla

    def cambiar_texto(self, instancia):
        # Función que se ejecuta al presionar el botón
        self.etiqueta.text = "¡El APK funciona perfectamente!"

if __name__ == "__main__":
    MiAplicacion().run()
  
