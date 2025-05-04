import flet as ft
import time
import threading


def login_view(page: ft.Page):
    page.title = "Tela de Login"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    email_input = ft.TextField(label="Email", width=300)
    senha_input = ft.TextField(
        label="Senha", password=True, can_reveal_password=True, width=300
    )
    mensagem = ft.Text("", size=16, color=ft.colors.GREEN)

    def autenticar(e):
        email = email_input.value
        senha = senha_input.value

        if email == "usuario@exemplo.com" and senha == "senha123":
            mensagem.value = "Login confirmado! Entrando em 3, 2, 1..."
            page.update()

            def redirecionar():
                time.sleep(3)
                page.go("/home")

            threading.Thread(target=redirecionar).start()
        else:
            mensagem.value = "Email ou senha incorretos."
            mensagem.color = ft.colors.RED
            page.update()

    botao_login = ft.ElevatedButton(text="Entrar", on_click=autenticar)

    page.add(
        ft.Column(
            controls=[
                ft.Text("Bem-vindo! Faça seu login abaixo.", size=20),
                email_input,
                senha_input,
                botao_login,
                mensagem,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )
