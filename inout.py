import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Dados dos produtos
dados = {
    "Nome": ["Lápis", "Canetões", "Resmas de folha A4", "Giz de cera", "Borrachas"],
    "Quantidade": [7, 5, 2, 8, 3]
}

# Criando o DataFrame
Df = pd.DataFrame(dados)

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Registro de Produtos")
        self.master.geometry("800x600")  # Aumenta o tamanho da tela
        self.master.config(bg="#f0f0f0")  # Cor de fundo

        # Armazenar o progresso dos produtos
        self.progresso = {nome: [] for nome in Df["Nome"].tolist()}

        # Página de Seleção de Produtos
        self.selecao_frame = tk.Frame(self.master, bg="#f0f0f0")

        self.criar_home()  # Chama a função para criar a página inicial

        # Página de Inserção de IDs
        self.id_frame = None
        self.quantidade_restante = 0

    def criar_home(self):
        # Cria a página inicial
        self.home_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.home_frame.pack(padx=20, pady=20, fill="both", expand=True)

        tk.Label(self.home_frame, text="Bem-vindo ao Sistema de Registro de Produtos", 
                 font=("Helvetica", 22, "bold"), bg="#f0f0f0").pack(pady=20)

        # Substituindo a imagem pelo texto "In Out"
        tk.Label(self.home_frame, text="In Out", font=("Helvetica", 48, "bold"), bg="#f0f0f0").pack(pady=50)

        tk.Button(self.home_frame, text="Iniciar Registro de Produtos", 
                  command=self.criar_selecao_frame, font=("Helvetica", 16), bg="#4CAF50", fg="white").pack(pady=20)

    def criar_selecao_frame(self):
        """Muda para a página de seleção de produtos."""
        self.home_frame.pack_forget()  # Esconde a página inicial
        self.selecao_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Mostra a seleção de produtos

        # Combobox para seleção de produtos
        self.produto_var = tk.StringVar()
        self.produto_combobox = ttk.Combobox(self.selecao_frame, textvariable=self.produto_var, 
                                              values=Df["Nome"].tolist(), font=("Helvetica", 14))
        self.produto_combobox.pack(pady=10, padx=20, fill="x")
        self.produto_combobox.bind("<<ComboboxSelected>>", self.abrir_id_frame)  # Bind para seleção

    def abrir_id_frame(self, event):
        produto_selecionado = self.produto_var.get()
        if not produto_selecionado:
            return  # Se nenhum produto for selecionado, não faz nada

        if self.id_frame:
            self.id_frame.destroy()

        # Criando a nova página para inserir IDs
        self.id_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.id_frame.pack(padx=20, pady=20, fill="both", expand=True)
        
        tk.Label(self.id_frame, text=f"Inserir IDs para {produto_selecionado}:", font=("Helvetica", 18, "bold"), bg="#f0f0f0").pack(pady=10)
        
        self.quantidade_restante = Df.loc[Df["Nome"] == produto_selecionado, "Quantidade"].values[0] - len(self.progresso[produto_selecionado])

        # Caixa de entrada para ID
        self.id_entry = tk.Entry(self.id_frame, font=("Helvetica", 14))
        self.id_entry.pack(pady=10, padx=20)

        # Bind para a tecla Enter
        self.id_entry.bind("<Return>", lambda event: self.confirmar_id())

        # Label para mostrar quantos itens faltam
        self.status_label = tk.Label(self.id_frame, text=f"Faltando: {self.quantidade_restante} IDs", font=("Helvetica", 14), bg="#f0f0f0")
        self.status_label.pack(pady=5)

        # Label para mostrar o status
        self.completion_status = tk.Label(self.id_frame, text="Status: Pendente", font=("Helvetica", 14), bg="#f0f0f0")
        self.completion_status.pack(pady=5)

        # Botão para confirmar o ID
        tk.Button(self.id_frame, text="Confirmar", command=self.confirmar_id, font=("Helvetica", 14), bg="#4CAF50", fg="white").pack(pady=10)

    def confirmar_id(self):
        id_input = self.id_entry.get()
        if id_input:
            try:
                id_input = int(id_input)
                self.progresso[self.produto_var.get()].append(id_input)  # Adiciona ao progresso
                self.id_entry.delete(0, tk.END)  # Limpa a entrada atual
                self.quantidade_restante -= 1  # Atualiza o contador

                # Verifica se ainda faltam IDs
                if self.quantidade_restante > 0:
                    self.status_label.config(text=f"Faltando: {self.quantidade_restante} IDs")
                    self.completion_status.config(text="Status: Pendente")  # Atualiza o status
                else:
                    # Todos os IDs foram registrados
                    messagebox.showinfo("Sucesso", "Todos os IDs registrados com sucesso!")
                    self.completion_status.config(text="Status: Completo")  # Atualiza o status final
                    print("IDs etiquetados:", self.progresso[self.produto_var.get()])  # Aqui você pode fazer o que quiser com os IDs
                    self.id_frame.destroy()  # Fecha a tela de IDs

            except ValueError:
                messagebox.showwarning("Aviso", "Por favor, insira apenas números.")

# Executa a função principal
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
