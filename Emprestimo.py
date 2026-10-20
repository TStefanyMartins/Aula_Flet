import flet as ft


def main(page: ft.Page):
    page.title = "Sistema de Empréstimo de Laboratório"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text(
        "Sistema de Empréstimo de Laboratório",
        size=30,
        weight="bold",
        text_align=ft.TextAlign.CENTER,
    )

    alunos = []

    equipamento = ft.Dropdown(
        label="Selecione o equipamento",
        opacity=0.5,
        width=300,
        options=[
            ft.DropdownOption(key="Notebook"),
            ft.DropdownOption(key="Projetor"),
            ft.DropdownOption(key="Multímetro"),
        ],
    )

    quantidade = ft.TextField(label="Quantidade", opacity=0.5, width=300)
    nome = ft.TextField(label="Nome do aluno", opacity=0.5, width=300)
    lista_itens = ft.Column(controls=[])

    def emprestimo(equipamento_selecionado):
        if not nome.value or not quantidade.value or not equipamento_selecionado.value:
            return

        cadastro = {
            "Nome": nome.value,
            "Quantidade": int(quantidade.value),
            "Tipo de equipamento": equipamento_selecionado.value,
        }
        alunos.append(cadastro)

        lista_itens.controls.append(
            ft.Text(
                f"Empréstimo realizado com sucesso para {nome.value} - {quantidade.value} {equipamento_selecionado.value}"
            )
        )
        page.update()

    def limpar_lista(_):
        lista_itens.controls.clear()
        page.update()

    botao_emprestimo = ft.Button(
        "Realizar Empréstimo", on_click=lambda e: emprestimo(equipamento)
    )
    botao_limpar = ft.Button("Limpar", on_click=limpar_lista)

    coluna = ft.Column(
        controls=[
            nome,
            equipamento,
            quantidade,
            ft.Row(
                controls=[botao_emprestimo, botao_limpar],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            lista_itens,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        scroll=ft.ScrollMode.AUTO,
        spacing=10,
        width=350,
    )

    page.add(
        ft.Column(
            controls=[titulo, coluna],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20,
        )
    )


ft.run(main)
