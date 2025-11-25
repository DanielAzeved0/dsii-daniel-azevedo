import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

class SistemaCadastro:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro - Python")
        self.root.geometry("600x550")
        self.root.resizable(False, False)
        
        # Configurar cores e estilo
        self.configurar_estilo()
        
        # Arquivo para armazenar os dados - corrigindo o caminho
        self.arquivo_dados = os.path.join(os.path.dirname(os.path.dirname(__file__)), "cadastros.json")
        
        # Lista para armazenar os cadastros
        self.cadastros = self.carregar_dados()
        
        self.criar_interface()
    
    def configurar_estilo(self):
        """Configura o estilo visual da aplicação"""
        # Cores da aplicação
        self.cores = {
            'primary': '#2E86AB',      # Azul principal
            'secondary': '#A23B72',    # Rosa/roxo secundário
            'accent': '#F18F01',       # Laranja de destaque
            'background': '#F5F5F5',   # Cinza claro de fundo
            'card': '#FFFFFF',         # Branco para cards
            'text': '#2C3E50',         # Azul escuro para texto
            'success': '#27AE60',      # Verde para sucesso
            'error': '#E74C3C'         # Vermelho para erro
        }
        
        # Configurar o fundo da janela principal
        self.root.configure(bg=self.cores['background'])
        
        # Configurar estilo dos widgets ttk
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar estilos personalizados
        style.configure('Title.TLabel', 
                       font=('Segoe UI', 20, 'bold'),
                       foreground=self.cores['primary'],
                       background=self.cores['background'])
        
        style.configure('Subtitle.TLabel',
                       font=('Segoe UI', 11, 'bold'),
                       foreground=self.cores['text'],
                       background=self.cores['card'])
        
        style.configure('Field.TLabel',
                       font=('Segoe UI', 10),
                       foreground=self.cores['text'],
                       background=self.cores['card'])
        
        style.configure('Custom.TEntry',
                       fieldbackground='white',
                       borderwidth=1,
                       focuscolor=self.cores['primary'],
                       font=('Segoe UI', 10))
        
        style.configure('Primary.TButton',
                       font=('Segoe UI', 10, 'bold'),
                       foreground='white',
                       background=self.cores['primary'],
                       borderwidth=0,
                       focuscolor='none')
        
        style.map('Primary.TButton',
                 background=[('active', '#1F5F8B')])
        
        style.configure('Secondary.TButton',
                       font=('Segoe UI', 10, 'bold'),
                       foreground='white',
                       background=self.cores['secondary'],
                       borderwidth=0,
                       focuscolor='none')
        
        style.map('Secondary.TButton',
                 background=[('active', '#7A2D5C')])
        
        style.configure('Accent.TButton',
                       font=('Segoe UI', 10, 'bold'),
                       foreground='white',
                       background=self.cores['accent'],
                       borderwidth=0,
                       focuscolor='none')
        
        style.map('Accent.TButton',
                 background=[('active', '#D17A01')])
    
    def criar_interface(self):
        # Frame principal com padding
        main_frame = tk.Frame(self.root, bg=self.cores['background'])
        main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=20)
        
        # Card principal
        card_frame = tk.Frame(main_frame, bg=self.cores['card'], relief='flat', bd=1)
        card_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Adicionar sombra visual ao card
        shadow_frame = tk.Frame(main_frame, bg='#E0E0E0', height=2)
        shadow_frame.place(x=12, y=12, relwidth=1, width=-22)
        
        # Container interno do card
        inner_frame = tk.Frame(card_frame, bg=self.cores['card'])
        inner_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=25)
        
        # Título principal
        titulo = ttk.Label(inner_frame, text="Sistema de Cadastro", 
                          style='Title.TLabel')
        titulo.pack(pady=(0, 30))
        
        # Subtitle
        subtitle = ttk.Label(inner_frame, text="Cadastro de Pessoas", 
                           style='Subtitle.TLabel')
        subtitle.pack(pady=(0, 25))
        
        # Frame para os campos de entrada
        fields_frame = tk.Frame(inner_frame, bg=self.cores['card'])
        fields_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Configurar grid para campos
        fields_frame.columnconfigure(1, weight=1)
        
        # Campo Nome
        nome_label = ttk.Label(fields_frame, text="Nome:", style='Field.TLabel')
        nome_label.grid(row=0, column=0, sticky=tk.W, pady=8, padx=(0, 15))
        self.entry_nome = ttk.Entry(fields_frame, font=('Segoe UI', 11), 
                                   style='Custom.TEntry', width=35)
        self.entry_nome.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=8)
        
        # Campo Sobrenome
        sobrenome_label = ttk.Label(fields_frame, text="Sobrenome:", style='Field.TLabel')
        sobrenome_label.grid(row=1, column=0, sticky=tk.W, pady=8, padx=(0, 15))
        self.entry_sobrenome = ttk.Entry(fields_frame, font=('Segoe UI', 11), 
                                        style='Custom.TEntry', width=35)
        self.entry_sobrenome.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=8)
        
        # Campo Idade
        idade_label = ttk.Label(fields_frame, text="Idade:", style='Field.TLabel')
        idade_label.grid(row=2, column=0, sticky=tk.W, pady=8, padx=(0, 15))
        self.entry_idade = ttk.Entry(fields_frame, font=('Segoe UI', 11), 
                                    style='Custom.TEntry', width=35)
        self.entry_idade.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=8)
        
        # Campo Sexo
        sexo_label = ttk.Label(fields_frame, text="Sexo:", style='Field.TLabel')
        sexo_label.grid(row=3, column=0, sticky=tk.W, pady=8, padx=(0, 15))
        self.combo_sexo = ttk.Combobox(fields_frame, values=["Masculino", "Feminino", "Outro"], 
                                      state="readonly", font=('Segoe UI', 11), width=32)
        self.combo_sexo.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=8)
        
        # Frame para botões com layout mais elegante
        buttons_frame = tk.Frame(inner_frame, bg=self.cores['card'])
        buttons_frame.pack(pady=(20, 25))
        
        # Botões com estilos diferentes
        btn_cadastrar = ttk.Button(buttons_frame, text="✓ Cadastrar", 
                                  command=self.cadastrar_pessoa, 
                                  style='Primary.TButton', width=12)
        btn_cadastrar.pack(side=tk.LEFT, padx=8)
        
        btn_limpar = ttk.Button(buttons_frame, text="🗑 Limpar", 
                               command=self.limpar_campos,
                               style='Secondary.TButton', width=12)
        btn_limpar.pack(side=tk.LEFT, padx=8)
        
        btn_listar = ttk.Button(buttons_frame, text="📋 Listar", 
                               command=self.listar_cadastros,
                               style='Accent.TButton', width=12)
        btn_listar.pack(side=tk.LEFT, padx=8)
        
        # Separador visual
        separator = ttk.Separator(inner_frame, orient='horizontal')
        separator.pack(fill=tk.X, pady=15)
        
        # Área de exibição com título
        lista_title = ttk.Label(inner_frame, text="📊 Cadastros Realizados", 
                               style='Subtitle.TLabel')
        lista_title.pack(anchor=tk.W, pady=(10, 8))
        
        # Frame para listbox com scrollbar
        list_container = tk.Frame(inner_frame, bg=self.cores['card'])
        list_container.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbar e Listbox com estilo melhorado
        scrollbar = ttk.Scrollbar(list_container)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.listbox = tk.Listbox(list_container, 
                                 height=8, 
                                 yscrollcommand=scrollbar.set,
                                 font=('Segoe UI', 10),
                                 bg='white',
                                 fg=self.cores['text'],
                                 selectbackground=self.cores['primary'],
                                 selectforeground='white',
                                 borderwidth=1,
                                 relief='solid',
                                 highlightthickness=0)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.listbox.yview)
        
        # Atualizar lista na inicialização
        self.atualizar_lista()
        
        # Focar no primeiro campo
        self.entry_nome.focus()
    
    def validar_dados(self, nome, sobrenome, idade, sexo):
        """Valida os dados de entrada"""
        if not nome.strip():
            messagebox.showerror("❌ Erro", "O campo Nome é obrigatório!", 
                               icon='error')
            return False
            
        if not sobrenome.strip():
            messagebox.showerror("❌ Erro", "O campo Sobrenome é obrigatório!", 
                               icon='error')
            return False
            
        if not idade.strip():
            messagebox.showerror("❌ Erro", "O campo Idade é obrigatório!", 
                               icon='error')
            return False
            
        try:
            idade_int = int(idade)
            if idade_int < 0 or idade_int > 150:
                messagebox.showerror("❌ Erro", "Idade deve estar entre 0 e 150 anos!", 
                                   icon='error')
                return False
        except ValueError:
            messagebox.showerror("❌ Erro", "Idade deve ser um número válido!", 
                               icon='error')
            return False
            
        if not sexo:
            messagebox.showerror("❌ Erro", "O campo Sexo deve ser selecionado!", 
                               icon='error')
            return False
            
        return True
    
    def cadastrar_pessoa(self):
        """Cadastra uma nova pessoa"""
        nome = self.entry_nome.get()
        sobrenome = self.entry_sobrenome.get()
        idade = self.entry_idade.get()
        sexo = self.combo_sexo.get()
        
        if not self.validar_dados(nome, sobrenome, idade, sexo):
            return
        
        # Criar dicionário com os dados
        pessoa = {
            "id": len(self.cadastros) + 1,
            "nome": nome.strip().title(),
            "sobrenome": sobrenome.strip().title(),
            "idade": int(idade),
            "sexo": sexo,
            "data_cadastro": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        }
        
        # Adicionar à lista
        self.cadastros.append(pessoa)
        
        # Salvar dados
        self.salvar_dados()
        
        # Atualizar lista
        self.atualizar_lista()
        
        # Limpar campos
        self.limpar_campos()
        
        messagebox.showinfo("✅ Sucesso", 
                          f"Pessoa {nome} {sobrenome} cadastrada com sucesso!", 
                          icon='info')
    
    def limpar_campos(self):
        """Limpa todos os campos de entrada"""
        self.entry_nome.delete(0, tk.END)
        self.entry_sobrenome.delete(0, tk.END)
        self.entry_idade.delete(0, tk.END)
        self.combo_sexo.set("")
        self.entry_nome.focus()
    
    def atualizar_lista(self):
        """Atualiza a lista de cadastros exibida"""
        self.listbox.delete(0, tk.END)
        for pessoa in self.cadastros:
            info = f"🆔 {pessoa['id']:02d} | 👤 {pessoa['nome']} {pessoa['sobrenome']} | 🎂 {pessoa['idade']} anos | {'👨' if pessoa['sexo'] == 'Masculino' else '👩' if pessoa['sexo'] == 'Feminino' else '👤'} {pessoa['sexo']}"
            self.listbox.insert(tk.END, info)
    
    def listar_cadastros(self):
        """Exibe janela com todos os cadastros detalhados"""
        if not self.cadastros:
            messagebox.showinfo("ℹ️ Info", "Nenhum cadastro encontrado!", 
                              icon='info')
            return
        
        # Criar nova janela com estilo melhorado
        janela_lista = tk.Toplevel(self.root)
        janela_lista.title("📊 Lista Completa de Cadastros")
        janela_lista.geometry("700x500")
        janela_lista.configure(bg=self.cores['background'])
        
        # Centralizar janela
        janela_lista.transient(self.root)
        janela_lista.grab_set()
        
        # Frame principal da janela
        main_frame = tk.Frame(janela_lista, bg=self.cores['card'], relief='flat', bd=1)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Título da janela
        titulo_janela = tk.Label(main_frame, text="📊 Relatório Completo de Cadastros", 
                                font=('Segoe UI', 16, 'bold'),
                                fg=self.cores['primary'], bg=self.cores['card'])
        titulo_janela.pack(pady=(20, 15))
        
        # Frame para texto com scrollbar
        text_frame = tk.Frame(main_frame, bg=self.cores['card'])
        text_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=(0, 20))
        
        scrollbar_text = ttk.Scrollbar(text_frame)
        scrollbar_text.pack(side=tk.RIGHT, fill=tk.Y)
        
        texto = tk.Text(text_frame, wrap=tk.WORD, yscrollcommand=scrollbar_text.set,
                       font=('Consolas', 11), bg='white', fg=self.cores['text'],
                       borderwidth=1, relief='solid', highlightthickness=0)
        texto.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar_text.config(command=texto.yview)
        
        # Inserir dados com formatação melhorada
        conteudo = f"📊 RELATÓRIO DE CADASTROS - {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        conteudo += "═" * 70 + "\n\n"
        
        for i, pessoa in enumerate(self.cadastros, 1):
            conteudo += f"┌─ CADASTRO #{pessoa['id']:02d} ──────────────────────────────────\n"
            conteudo += f"│ 👤 Nome Completo: {pessoa['nome']} {pessoa['sobrenome']}\n"
            conteudo += f"│ 🎂 Idade: {pessoa['idade']} anos\n"
            conteudo += f"│ {'👨' if pessoa['sexo'] == 'Masculino' else '👩' if pessoa['sexo'] == 'Feminino' else '👤'} Sexo: {pessoa['sexo']}\n"
            conteudo += f"│ 📅 Data do Cadastro: {pessoa['data_cadastro']}\n"
            conteudo += "└" + "─" * 45 + "\n\n"
        
        conteudo += f"📈 RESUMO: Total de {len(self.cadastros)} cadastro(s) realizado(s)"
        
        texto.insert(tk.END, conteudo)
        texto.config(state=tk.DISABLED)
    
    def carregar_dados(self):
        """Carrega dados do arquivo JSON"""
        if os.path.exists(self.arquivo_dados):
            try:
                with open(self.arquivo_dados, 'r', encoding='utf-8') as arquivo:
                    return json.load(arquivo)
            except (json.JSONDecodeError, FileNotFoundError):
                return []
        return []
    
    def salvar_dados(self):
        """Salva dados no arquivo JSON"""
        try:
            with open(self.arquivo_dados, 'w', encoding='utf-8') as arquivo:
                json.dump(self.cadastros, arquivo, ensure_ascii=False, indent=2)
        except Exception as e:
            messagebox.showerror("❌ Erro", f"Erro ao salvar dados: {str(e)}")

def main():
    """Função principal do programa"""
    root = tk.Tk()
    app = SistemaCadastro(root)
    root.mainloop()

if __name__ == "__main__":
    main()