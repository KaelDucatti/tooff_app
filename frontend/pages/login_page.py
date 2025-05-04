import flet as ft

def login_page(page: ft.Page):
    page.title = "Tela de Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment CENTER

    # Campos de entrada
    email_input = ft.TextField(label="Email", width=300)
    pwd_input = ft.TextField(label="Senha", password=True, can_reveal_password=True, width=300)

    def authenticator(e):
        email = email_input.value
        pwd = pwd_input.value

        if email == "usuario@exemplo.com" and pwd == "pwd123":
            page.dialog = ft.AlertDialog(title=ft.Text("Login bem-sucedido!"))
        else:
            page.dialog = ft.AlertDialog(title=ft.Text("Email ou senha incorretos."))

        page.dialog.open = True
        page.update()

    botao_login = ft.ElevatedButton(text="Entrar", on_click=authenticator)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Bem-vindo! Faça seu login abaixo.", size=20),
                email_input,
                pwd_input,
                botao_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )