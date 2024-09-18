import openai
import tkinter as tk
from tkinter import messagebox, scrolledtext

# GPT-3.5/4 API-Schlüssel einfügen
openai.api_key = 'sk-obiqqXB7QyHIKKbQPpdJk_lHX7lQ9n72JdNszT6o6rT3BlbkFJd7FG3TRYjPnuziszPeCPGdG1OogM6DsBMtsmDXxiAA'

# Funktion, die GPT-4-Anfragen durchführt
def gpt_request(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # oder "gpt-4", wenn du Zugriff hast
            messages=[{"role": "system", "content": "Du bist ein hilfreicher Assistent."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Fehler bei der Anfrage: {e}"

# Hauptfenster und UI-Elemente erstellen
class GPTApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GPT-3 Assistent")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # Begrüßungstext
        self.label = tk.Label(root, text="Hallo! Möchtest du programmieren, Bewerbungen schreiben oder hast du allgemeine Fragen?",
                              font=("Arial", 14), bg="#f0f0f0")
        self.label.pack(pady=10)

        # Dropdown-Menü für die Auswahl
        self.options = ["Programmieren", "Bewerbung schreiben", "Allgemeine Fragen"]
        self.selected_option = tk.StringVar(root)
        self.selected_option.set(self.options[0])
        self.option_menu = tk.OptionMenu(root, self.selected_option, *self.options)
        self.option_menu.config(width=20)
        self.option_menu.pack(pady=10)

        # Eingabefeld für den Benutzer
        self.entry_label = tk.Label(root, text="Gib hier dein Anliegen ein:", bg="#f0f0f0")
        self.entry_label.pack(pady=5)
        self.entry_field = tk.Entry(root, width=50)
        self.entry_field.pack(pady=5)

        # Ausgabe-Bereich für die Antwort von GPT-4
        self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=10, bg="#ffffff", state='disabled')
        self.output_text.pack(pady=10)

        # Senden-Button
        self.send_button = tk.Button(root, text="Senden", command=self.send_request, bg="#4CAF50", fg="white", padx=20, pady=10)
        self.send_button.pack(pady=10)

    # Methode, um die Anfrage zu senden und die Antwort zu empfangen
    def send_request(self):
        user_input = self.entry_field.get()
        category = self.selected_option.get()

        if not user_input:
            messagebox.showwarning("Leeres Feld", "Bitte gib ein Anliegen ein.")
            return

        prompt = f"Ich möchte {category.lower()}. {user_input}"
        response = gpt_request(prompt)

        # Antwort anzeigen
        self.output_text.config(state='normal')
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.INSERT, response)
        self.output_text.config(state='disabled')

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = GPTApp(root)
    root.mainloop()
