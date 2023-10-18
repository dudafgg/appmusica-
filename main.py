import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import Listbox, Scrollbar, ttk

# Inicializa o Pygame.
pygame.init()

# Cria uma janela.
janela = tk.Tk()
janela.title("Player de Música")

# Cria uma lista para armazenar as músicas.
lista_de_reproducao = []

# Variável para rastrear o estado da música (tocando ou pausada).
tocando = False

# Variável para rastrear o índice da música atual na lista de reprodução.
indice_musica_atual = 0

# Função para carregar uma música.
def carregar_musica():
    caminho_do_arquivo = filedialog.askopenfilename(title="Selecione uma música", filetypes=[("Arquivos de áudio", "*.mp3")])
    if caminho_do_arquivo:
        lista_de_reproducao.append(caminho_do_arquivo)
        lista_musicas.insert(tk.END, caminho_do_arquivo)

# Função para tocar a música selecionada na lista.
def tocar_musica():
    global tocando, indice_musica_atual
    if not tocando and lista_de_reproducao:
        pygame.mixer.music.load(lista_de_reproducao[indice_musica_atual])
        pygame.mixer.music.play()
        tocando = True

# Função para parar a música.
def parar_musica():
    global tocando
    if tocando:
        pygame.mixer.music.stop()
        tocando = False

# Função para avançar para a próxima música.
def proxima_musica():
    global tocando, indice_musica_atual
    if tocando:
        parar_musica()
        indice_musica_atual = (indice_musica_atual + 1) % len(lista_de_reproducao)
        tocar_musica()

# Função para voltar para a música anterior.
def musica_anterior():
    global tocando, indice_musica_atual
    if tocando:
        parar_musica()
        indice_musica_atual = (indice_musica_atual - 1) % len(lista_de_reproducao)
        tocar_musica()

# Cria uma lista de reprodução (Listbox) para mostrar as músicas.
lista_musicas = Listbox(janela, selectmode=tk.SINGLE, width=50)
lista_musicas.pack(padx=10, pady=10, side=tk.LEFT)

# Adiciona uma barra de rolagem à lista de reprodução.
scrollbar = Scrollbar(janela)
scrollbar.pack(fill=tk.Y, side=tk.RIGHT)
lista_musicas.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_musicas.yview)

# Cria botões estilizados para carregar, tocar, parar, avançar e voltar músicas.
botao_carregar = ttk.Button(janela, text="Carregar Música", command=carregar_musica)
botao_tocar = ttk.Button(janela, text="Tocar", command=tocar_musica)
botao_parar = ttk.Button(janela, text="Parar", command=parar_musica)
botao_avancar = ttk.Button(janela, text="Avançar", command=proxima_musica)
botao_voltar = ttk.Button(janela, text="Voltar", command=musica_anterior)

# Estiliza os botões.
estilo = ttk.Style()
estilo.configure("TButton", foreground="blue", background="white", font=("Helvetica", 12))
estilo.map("TButton",
          foreground=[("pressed", "red"), ("active", "blue")],
          background=[("pressed", "!disabled", "black"), ("active", "white")]
          )

# Coloca os botões na janela.
botao_carregar.pack()
botao_tocar.pack()
botao_parar.pack()
botao_avancar.pack()
botao_voltar.pack()

# Inicia o loop principal do Pygame.
janela.mainloop()
