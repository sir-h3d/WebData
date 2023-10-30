import flet as ft
import json
import random 

COLECCIONES = ['anchobandadia', 'anchobandadiafecha', 'anchobandahora', 'anchobandames', 'anchobandamesfecha', 'diaSeleccionado', 'horaSeleccionada', 'host', 'hostconectados', 'ip', 'ipSeleccionada', 'mesSeleccionado', 'puertosactivos', 'totalpuertosactivos']

from flet import (
    Container,
    Icon,
    Page,
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
    colors,
    icons,
    margin
)

def main():
    def random_color():
        while True:
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)
            # Evita el color blanco
            if (r, g, b) != (255, 255, 255):
                return "#{:02x}{:02x}{:02x}".format(r,g,b)

    
    def generateContainer(text):
        containerWidth = 300
        containerHeight = 200
        containerg= ft.Container(
                    content=ft.Text(text, size=25, color="White", italic=True),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.top_left,
                    bgcolor=random_color(),
                    width=containerWidth,
                    height=containerHeight,
                    border_radius=30,
                )
        return containerg
        
    def main(page: Page):
        page.title = "RecursosTI"
        page.padding = 0
        page.bgcolor = colors.BLACK
        page.vertical_alignment = ft.MainAxisAlignment.CENTER
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        appbar = AppBar(
            leading=Icon(icons.GRID_GOLDENRATIO_ROUNDED),
            leading_width=100,
            title=Text("RecursosTI",size=32, text_align="start"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.GREEN_300,
        )
        page.appbar = appbar
        new_task = ft.TextField(hint_text="Ingrese su busqueda",text_size=20,icon=ft.icons.SEARCH)
        page.add(new_task)
        page.scroll = "always"
        # Datos
        ip = "192.168.1.1"
        hora_conexion = "Sun Oct 29 23:39:07 EDT 2023"
        puertos_usados = "21/tcp, 22/tcp, 23/tcp, 53/tcp, 80/tcp, 139/tcp, 445/tcp, 8899/tcp, 17998/tcp, 37443/tcp, 37444/tcp"
        numeros_de_host = "3"
        consumo_del_dia = "10 GB"
        # Crear el texto con formato
        texto1 = f"IP: {ip:20}\nHora de conexión: {hora_conexion:20}\nPuertos usados: {puertos_usados:20}\nNúmeros de host: {numeros_de_host:20}\nConsumo del día: {consumo_del_dia:20}"
        for x in range(10):
            page.add(ft.ResponsiveRow([generateContainer(texto1),]))
            ft.Divider()
            page.update()
    ft.app(target=main,view=ft.WEB_BROWSER)

main()
#ip, hora de conexion, puertos usados, numeros de host, consumo del dia,
