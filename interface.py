import tkinter as tk
from tokenRecognizer import getHTMLTokens
from tkinter import filedialog
from tkinter import messagebox


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

def show_code():
    html_code = open_file()
    valid_html_tokens, all_tokens = getHTMLTokens(html_code)

    # text_widget.delete('1.0', tk.END)
    # text_widget.insert(tk.END, all_tokens)
    
    if html_code == "":
        popup_message("HTML Tokens", "Nenhum arquivo foi selecionado ou o arquivo está vazio.", "warning")
    else:
        popup_message("HTML Tokens", all_tokens)

    # print(valid_html_tokens, all_tokens)

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

# text_widget = tk.Text(root, width=80, height=30)
# text_widget.pack(pady=10)

root.mainloop()
