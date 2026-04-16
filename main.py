import flet as ft

def main(page: ft.Page):
    page.title = "Denúncia Já"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    def ligar(telefone):
        # Abre o discador do celular
        page.launch_url(f"tel:{telefone}")
    botao_ligar = ft.ElevatedButton(
        "Polícia Militar",
        icon="phone",
        on_click=ligar(190)
    )

    page.add(
        ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                botao_ligar,
            ],
        )
    )

ft.run(main)