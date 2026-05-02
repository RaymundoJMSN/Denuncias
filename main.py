import flet as ft


EMERGENCIAS = [
    {"titulo": "Polícia Militar", "telefone": "190", "icone": ft.Icons.LOCAL_POLICE,
     "descricao": "Emergência policial imediata.", "cor": ft.Colors.RED_700},
    {"titulo": "SAMU", "telefone": "192", "icone": ft.Icons.MEDICAL_SERVICES,
     "descricao": "Emergência médica e atendimento pré-hospitalar.", "cor": ft.Colors.RED_600},
    {"titulo": "Bombeiros", "telefone": "193", "icone": ft.Icons.FIRE_TRUCK,
     "descricao": "Incêndios, resgates e situações de risco.", "cor": ft.Colors.DEEP_ORANGE_700},
    {"titulo": "Polícia Rodoviária Federal", "telefone": "191", "icone": ft.Icons.DIRECTIONS_CAR,
     "descricao": "Emergências em rodovias federais.", "cor": ft.Colors.BLUE_800},
    {"titulo": "Polícia Civil", "telefone": "197", "icone": ft.Icons.BADGE,
     "descricao": "Ocorrências, investigações e atendimento policial civil.", "cor": ft.Colors.INDIGO_700},
    {"titulo": "Defesa Civil", "telefone": "199", "icone": ft.Icons.WARNING,
     "descricao": "Desastres, enchentes, deslizamentos e riscos estruturais.", "cor": ft.Colors.AMBER_800},
    {"titulo": "Guarda Municipal", "telefone": "153", "icone": ft.Icons.SECURITY,
     "descricao": "Atendimento da Guarda Municipal, quando disponível na cidade.", "cor": ft.Colors.GREEN_800},
    {"titulo": "Central de Atendimento à Mulher", "telefone": "180", "icone": ft.Icons.WOMAN,
     "descricao": "Orientação e denúncias de violência contra a mulher.", "cor": ft.Colors.PINK_700},
    {"titulo": "Disque Direitos Humanos", "telefone": "100", "icone": ft.Icons.REPORT,
     "descricao": "Denúncias de violações de direitos humanos.", "cor": ft.Colors.PURPLE_700},
    {"titulo": "Disque Denúncia", "telefone": "181", "icone": ft.Icons.REPORT_PROBLEM,
     "descricao": "Denúncia anônima, quando disponível no estado.", "cor": ft.Colors.BLUE_GREY_700},
    {"titulo": "CVV", "telefone": "188", "icone": ft.Icons.SUPPORT_AGENT,
     "descricao": "Apoio emocional gratuito e sigiloso.", "cor": ft.Colors.TEAL_700},
]


DENUNCIAS_ONLINE = [
    {"titulo": "Disque 100 - Direitos Humanos",
     "url": "https://www.gov.br/pt-br/servicos/denunciar-violacao-de-direitos-humanos",
     "icone": ft.Icons.PUBLIC,
     "descricao": "Canal online para denúncias de violações de direitos humanos.",
     "cor": ft.Colors.PURPLE_700},
    {"titulo": "Ligue 180 - Violência contra a mulher",
     "url": "https://www.gov.br/mdh/pt-br/campanha/direitoshumanosparatodos/disque-100-e-ligue-180",
     "icone": ft.Icons.PUBLIC,
     "descricao": "Canal de denúncia e orientação para mulheres.",
     "cor": ft.Colors.PINK_700},
    {"titulo": "Comunica PF",
     "url": "https://www.gov.br/pf/pt-br/canais_atendimento/comunicacao-de-crimes",
     "icone": ft.Icons.COMPUTER,
     "descricao": "Comunicação online de crimes de atribuição da Polícia Federal.",
     "cor": ft.Colors.BLUE_800},
    {"titulo": "Delegacia Virtual",
     "url": "https://www.gov.br/pt-br/servicos/registrar-ocorrencia-policial-online",
     "icone": ft.Icons.DESCRIPTION,
     "descricao": "Registro online de ocorrência policial, conforme disponibilidade do estado.",
     "cor": ft.Colors.INDIGO_700},
    {"titulo": "Chat do CVV", "url": "https://cvv.org.br/chat/",
     "icone": ft.Icons.CHAT,
     "descricao": "Atendimento online do CVV por chat.",
     "cor": ft.Colors.TEAL_700},
]


def main(page: ft.Page):
    page.title = "Disque Denúncia"
    page.theme_mode = ft.ThemeMode.SYSTEM
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.bgcolor = ft.Colors.GREY_100

    page.locale_configuration = ft.LocaleConfiguration(
        supported_locales=[ft.Locale("pt", "BR")],
        current_locale=ft.Locale("pt", "BR"),
    )

    page.theme = ft.Theme(font_family="Roboto",
                          visual_density=ft.VisualDensity.COMFORTABLE,
                          use_material3=True)
    page.dark_theme = ft.Theme(font_family="Roboto",
                               visual_density=ft.VisualDensity.COMFORTABLE,
                               use_material3=True)

    status_text = ft.Text("Pronto para usar.", size=14,
                          color=ft.Colors.GREY_800, expand=True,
                          semantics_label="Status do aplicativo: pronto para usar.")

    url_launcher = ft.UrlLauncher()
    page.services.append(url_launcher)

    async def abrir_discador(telefone):
        await url_launcher.launch_url(f"tel:{telefone}")

    async def abrir_site(url):
        await url_launcher.launch_url(url)

    def mostrar_status(mensagem):
        status_text.value = mensagem
        page.update()

    def criar_topo():
        return ft.Semantics(
            label="Disque Denúncia. Emergência e denúncia em um só lugar.",
            header=True,
            content=ft.Container(
                padding=ft.Padding.only(left=16, right=16, top=14, bottom=14),
                bgcolor=ft.Colors.RED_700,
                content=ft.Row(
                    spacing=12,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(
                            width=46, height=46, border_radius=14,
                            bgcolor=ft.Colors.WHITE,
                            alignment=ft.Alignment(0, 0),
                            content=ft.Icon(ft.Icons.SHIELD, size=30,
                                            color=ft.Colors.RED_700,
                                            semantics_label="Escudo do aplicativo"),
                        ),
                        ft.Column(spacing=0, expand=True, controls=[
                            ft.Text("Disque Denúncia", size=24,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.WHITE),
                            ft.Text("Emergência e denúncia em um só lugar",
                                    size=13, color=ft.Colors.WHITE),
                        ]),
                    ],
                ),
            ),
        )

    def criar_aviso_compacto():
        return ft.Container(
            margin=ft.Margin.only(left=14, right=14, top=12, bottom=4),
            padding=ft.Padding.symmetric(horizontal=12, vertical=10),
            border_radius=14, bgcolor=ft.Colors.WHITE,
            content=ft.Row(spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon(ft.Icons.INFO_OUTLINE, size=22, color=ft.Colors.RED_700),
                    ft.Text("Em casos urgentes, informe sua localização com clareza.",
                            size=13, color=ft.Colors.GREY_900, expand=True),
                ]),
        )

    def criar_titulo_secao(titulo, subtitulo, icone):
        return ft.Semantics(
            label=f"{titulo}. {subtitulo}", header=True,
            content=ft.Container(
                padding=ft.Padding.only(left=16, right=16, top=14, bottom=6),
                content=ft.Row(spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Icon(icone, size=24, color=ft.Colors.RED_700),
                        ft.Column(spacing=0, expand=True, controls=[
                            ft.Text(titulo, size=19,
                                    weight=ft.FontWeight.BOLD,
                                    color=ft.Colors.GREY_900),
                            ft.Text(subtitulo, size=13, color=ft.Colors.GREY_700),
                        ]),
                    ]),
            ),
        )

    def criar_card_ligacao(item):
        telefone, cor = item["telefone"], item["cor"]
        titulo, descricao = item["titulo"], item["descricao"]

        async def ao_clicar_ligar(e):
            mostrar_status(f"Abrindo discador para {titulo}, número {telefone}.")
            await abrir_discador(telefone)

        rotulo = (f"{titulo}. {descricao} Telefone {telefone}. "
                  "Toque para abrir o discador.")

        return ft.Semantics(
            label=rotulo, button=True,
            content=ft.Container(
                margin=ft.Margin.only(left=12, right=12, bottom=8),
                content=ft.Card(elevation=1, bgcolor=ft.Colors.WHITE,
                    content=ft.Container(padding=14, border_radius=14,
                        content=ft.Column(spacing=12, controls=[
                            ft.Row(spacing=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(width=48, height=48, border_radius=14,
                                        bgcolor=ft.Colors.with_opacity(0.15, cor),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Icon(item["icone"], size=28,
                                                        color=cor, semantics_label=titulo)),
                                    ft.Column(spacing=2, expand=True, controls=[
                                        ft.Text(titulo, size=17,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.GREY_900),
                                        ft.Text(descricao, size=13,
                                                color=ft.Colors.GREY_700),
                                    ]),
                                ]),
                            ft.Row(spacing=10,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(
                                        padding=ft.Padding.symmetric(horizontal=12, vertical=8),
                                        border_radius=100, bgcolor=ft.Colors.GREY_200,
                                        content=ft.Text(telefone, size=16,
                                                        weight=ft.FontWeight.BOLD,
                                                        color=ft.Colors.GREY_900,
                                                        semantics_label=f"Número {telefone}")),
                                    ft.Button(content="Abrir discador",
                                        icon=ft.Icons.PHONE,
                                        on_click=ao_clicar_ligar,
                                        expand=True, height=48,
                                        tooltip=f"Ligar para {titulo} ({telefone})",
                                        style=ft.ButtonStyle(bgcolor=cor,
                                            color=ft.Colors.WHITE,
                                            shape=ft.RoundedRectangleBorder(radius=12))),
                                ]),
                        ]))),
            ),
        )

    def criar_card_site(item):
        url, cor = item["url"], item["cor"]
        titulo, descricao = item["titulo"], item["descricao"]

        async def ao_clicar_site(e):
            mostrar_status(f"Abrindo {titulo} no navegador.")
            await abrir_site(url)

        rotulo = (f"{titulo}. {descricao} "
                  "Toque para abrir o canal online no navegador.")

        return ft.Semantics(
            label=rotulo, button=True, link=True,
            content=ft.Container(
                margin=ft.Margin.only(left=12, right=12, bottom=8),
                content=ft.Card(elevation=1, bgcolor=ft.Colors.WHITE,
                    content=ft.Container(padding=14, border_radius=14,
                        content=ft.Column(spacing=12, controls=[
                            ft.Row(spacing=12,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[
                                    ft.Container(width=48, height=48, border_radius=14,
                                        bgcolor=ft.Colors.with_opacity(0.15, cor),
                                        alignment=ft.Alignment(0, 0),
                                        content=ft.Icon(item["icone"], size=28,
                                                        color=cor, semantics_label=titulo)),
                                    ft.Column(spacing=2, expand=True, controls=[
                                        ft.Text(titulo, size=17,
                                                weight=ft.FontWeight.BOLD,
                                                color=ft.Colors.GREY_900),
                                        ft.Text(descricao, size=13,
                                                color=ft.Colors.GREY_700),
                                    ]),
                                ]),
                            ft.Button(content="Abrir denúncia online",
                                icon=ft.Icons.OPEN_IN_BROWSER,
                                on_click=ao_clicar_site, height=48,
                                tooltip=f"Abrir {titulo} no navegador",
                                style=ft.ButtonStyle(bgcolor=cor,
                                    color=ft.Colors.WHITE,
                                    shape=ft.RoundedRectangleBorder(radius=12))),
                        ]))),
            ),
        )

    def criar_rodape():
        return ft.Container(
            padding=ft.Padding.only(left=16, right=16, top=8, bottom=24),
            content=ft.Column(spacing=6,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Divider(height=16),
                    ft.Text("Este aplicativo apenas facilita o acesso aos canais oficiais.",
                            size=12, color=ft.Colors.GREY_700,
                            text_align=ft.TextAlign.CENTER),
                    ft.Text("Confira sempre se o número ou site está disponível na sua região.",
                            size=12, color=ft.Colors.GREY_700,
                            text_align=ft.TextAlign.CENTER),
                ]),
        )

    page.add(ft.Column(spacing=0, controls=[
        criar_topo(),
        criar_aviso_compacto(),
        criar_titulo_secao("Telefones de emergência",
                           "Toque para abrir o discador do celular",
                           ft.Icons.PHONE_IN_TALK),
        ft.Column(spacing=0,
                  controls=[criar_card_ligacao(i) for i in EMERGENCIAS]),
        criar_titulo_secao("Denúncias online",
                           "Acesse canais oficiais pelo navegador",
                           ft.Icons.LANGUAGE),
        ft.Column(spacing=0,
                  controls=[criar_card_site(i) for i in DENUNCIAS_ONLINE]),
        criar_rodape(),
    ]))


ft.run(main)
