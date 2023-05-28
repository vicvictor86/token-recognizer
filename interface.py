import tkinter as tk
from tkinter import filedialog
from tokenRecognizer import getHTMLTokens


def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("HTML Files", "*.html")])
    if file_path:
        with open(file_path, 'r') as file:
            html_code = file.read()
            return html_code
    else:
        return ""


def show_code():
    html_code = open_file()
    valid_html_tokens, all_tokens = getHTMLTokens(html_code)

    text_widget.delete('1.0', tk.END)
    text_widget.insert(tk.END, all_tokens)

    print(valid_html_tokens, all_tokens)


root = tk.Tk()
root.title("Visualizador de Código HTML")

frame = tk.Frame(root)
frame.pack(pady=20)

open_button = tk.Button(frame, text="Abrir Arquivo", command=show_code)
open_button.pack(side=tk.LEFT)

text_widget = tk.Text(root, width=80, height=30)
text_widget.pack(pady=10)

root.mainloop()
