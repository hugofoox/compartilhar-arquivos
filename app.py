import ttkbootstrap as tb
import http.server
import socketserver
import os
import threading

DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))
os.chdir(f"{DIRETORIO_ATUAL}/pasta")
Handler = http.server.SimpleHTTPRequestHandler

# Criar a janela principal
root = tb.Window(themename="solar")

root.title("SERVIDOR")
root.geometry("300x150")

label = tb.Label(root, text="PORTA:", bootstyle="primary")
label.pack(pady=2)

entry = tb.Entry(root, bootstyle="info")
entry.pack(pady=2)

label_padrao = tb.Label(root, text="(PADRÃO É 80)", bootstyle="primary")
label_padrao.pack(pady=2)

status_label = tb.Label(root, text="", bootstyle="primary")
status_label.pack(pady=2)

# Função para iniciar o servidor em segundo plano
def iniciar_servidor(porta):
    try:
        with socketserver.TCPServer(("0.0.0.0", porta), Handler) as httpd:
            print(f"🚀 Servidor rodando em http://127.0.0.1:{porta}")
            status_label.config(text=f"Servidor iniciado na porta {porta}", bootstyle="success")
            httpd.serve_forever()
    except Exception as e:
        status_label.config(text=f"Erro: {e}", bootstyle="danger")

# Função para o botão
def mostrar_texto():
    try:
        if entry.get() == "":
            porta = 80
        else:
            porta = int(entry.get())
    except ValueError:
        status_label.config(text="Porta inválida", bootstyle="danger")
        return

    thread = threading.Thread(target=iniciar_servidor, args=(porta,))
    thread.daemon = True  # Fecha a thread junto com o programa principal
    thread.start()

# Criar um botão estilizado
botao = tb.Button(root, text="Confirmar", bootstyle="success", command=mostrar_texto)
botao.pack(pady=5)

# Rodar a aplicação
root.mainloop()
