import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from tokenRecognizer import getHTMLTokens, tokens_name


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        with open(file_path, 'r') as file:
            html_code = file.read()
            return html_code
    else:
        return ""


def popup_message(title, message, icon="info"):
    messagebox.showinfo(title, message, icon=icon)


def deleteText(text_component):
    text_component.configure(state='normal')
    text_component.delete('1.0', tk.END)
    text_component.configure(state='disabled')


def insertText(text_component, text_to_add):
    text_component.configure(state='normal')
    text_component.insert(tk.END, text_to_add)
    text_component.configure(state='disabled')


def show_code():
    try:
        html_code = open_file()
        valid_html_tokens, tokens_and_type = getHTMLTokens(html_code)

        deleteText(text1)
        deleteText(text2)

        if html_code == "":
            popup_message("HTML Tokens", "Nenhum arquivo foi selecionado ou o arquivo está vazio.", "warning")
        else:
            insertText(text1, html_code)

            formatTokensCollected(valid_html_tokens, tokens_and_type)
    except Exception as err:
        popup_message("Error", "Não foi possível abrir o arquivo selecionado.", "warning")
        print(err)


def formatTokensCollected(valid_html_tokens, tokens_and_type):
    for token in tokens_and_type:
        tokens_by_type = ''
        if tokens_name[token['type']]["name"] == 'TEXT' and token["text"] in valid_html_tokens:
            tokens_by_type = f'{"ValidHtmlTag"}: {token["text"]}\n\n'
        else:
            tokens_by_type = f'{tokens_name[token["type"]]["name"]}: {token["text"]}\n\n'

        insertText(text2, tokens_by_type)


def change_cursor(event):
    open_button.configure(cursor="hand2")


root = tk.Tk()
root.title("Visualizador de Código HTML")

root.geometry("800x600")
root.state("zoomed")
root.configure(bg="#1a1a1a")

frame = tk.Frame(root, bg="#1a1a1a")
frame.pack(pady=50)

open_button = tk.Button(
        frame,
        text="Abrir Arquivo",
        font=("Arial", 14),
        bg="#4682B4",
        fg="white",
        relief="flat",
        padx=20,
        pady=10, command=show_code)
open_button.pack(side=tk.BOTTOM)
open_button.bind("<Enter>", change_cursor)

frame_divisao = tk.Frame(root, bg="#1a1a1a")
frame_divisao.pack(fill="both", expand=True)

text1_frame = tk.Frame(frame_divisao, bg="#1a1a1a")
text1_frame.pack(side=tk.LEFT, fill="both", expand=True)

text1_label = tk.Label(text1_frame, text="Texto adicionado", bg="#1a1a1a", fg="white")
text1_label.pack()

text1 = tk.Text(text1_frame, bg="#1a1a1a", fg="white", state='disabled')
text1.pack(side=tk.LEFT, fill="both", expand=True)

text2_frame = tk.Frame(frame_divisao, bg="#1a1a1a")
text2_frame.pack(side=tk.LEFT, fill="both", expand=True)

text2_label = tk.Label(text2_frame, text="Tokens Reconhecidos", bg="#1a1a1a", fg="white")
text2_label.pack()

text2 = tk.Text(text2_frame, bg="#1a1a1a", fg="white", state='disabled')
text2.pack(side=tk.LEFT, fill="both", expand=True)

root.mainloop()
