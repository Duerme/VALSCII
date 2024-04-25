import customtkinter
import tkinter

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        self.geometry("720x480")
        self.title("RIOTSCII")

        # Initializing TextBox
        title = customtkinter.CTkLabel(self, text="Type in your troll message (Make sure each word is no more than 5 characters)")
        title.pack(padx=10, pady=10)
        
        self.usr_var = tkinter.StringVar()
        usrInput = customtkinter.CTkEntry(self, width=350, height=40, textvariable=self.usr_var)
        usrInput.pack(pady=20)

        # Generate Button
        generate_button = customtkinter.CTkButton(self, text="Generate", command=self.generate_ascii_art)
        generate_button.pack(padx=10, pady=10)

        # Output Label
        self.output_label = customtkinter.CTkLabel(self, text="", fg_color="transparent", wraplength=650)
        self.output_label.pack(padx=10, pady=10)

        # Copy Button
        copy_button = customtkinter.CTkButton(self, text='Copy', command=self.copy)
        copy_button.pack(padx=10, pady=10)

    def map_characters_to_ascii(self):
        # Return a dictionary mapping each character to its multiline ASCII art equivalent.
        return {
            'A': ["░█▀█░", "░█▄█░", "░▀░▀░"], 
            'B': ["░█▀▄░", "░█▀█░", "░▀▀░░"],
            'C': ["░█▀▀░", "░█░░░", "░▀▀▀░"],
            'D': ["░█▀▄░", "░█░█░", "░▀▀░░"],
            'E': ["░█▀▀░", "░█▀▀░", "░▀▀▀░"],
            'F': ["░█▀▀░", "░█▀▀░", "░▀░░░"],
            'G': ["░█▀▀▀", "░█░▀█", "░▀▀▀▀"],
            'H': ["░█░█░", "░█▀█░", "░▀░▀░"],
            'I': ["░▀█▀░", "░░█░░", "░▀▀▀░"],
            'J': ["░▀█▀░", "░░█░░", "░▀▀░░"],
            'K': ["░█▄▀░", "░█▀▄░", "░▀░▀░"],
            'L': ["░█░░░", "░█░░░", "░▀▀▀░"],
            'M': ["░█▄░▄█░", "░█░█░█░", "░▀░░░▀░"],
            'N': ["░█▄░█░", "░█░▀█░", "░▀░░▀░"],
            'O': ["░█▀█░", "░█░█░", "░▀▀▀░"],
            'P': ["░█▀▄░", "░█▀░░", "░▀░░░"],
            'Q': ["░█▀█░", "░█░█░", "░░▀▀▄"],
            'R': ["░█▀▄░", "░█▀▄░", "░▀░▀░"],
            'S': ["░█▀▀░", "░▀▀█░", "░▀▀▀░"],
            'T': ["░▀█▀░", "░░█░░", "░░▀░░"],
            'U': ["░█░█░", "░█░█░", "░▀▀▀░"],
            'V': ["░█░█░", "░█░█░", "░░▀░░"],
            'W': ["░█▐▌█░", "░█▐▌█░", "░░▀▀░░"],
            'X': ["░█░█░", "░░█░░", "░█░█░"],
            'Y': ["░█░█░", "░░█░░", "░░▀░░"],
            'Z': ["░▀▀█░", "░▄▀░░", "░▀▀▀░"],
            # Add other letters as needed
        }

    def generate_ascii_art(self):
        ascii_map = self.map_characters_to_ascii()
        user_input = self.usr_var.get()
        all_art_lines = ['░' * 26]  # Top padding

        words = user_input.split()  # Split input into words

        for word_index, word in enumerate(words):
            art_lines = ['' for _ in range(3)]

            for char in word.upper():
                mapped_art = ascii_map.get(char, ['       '] * 3)
                for i in range(3):
                    art_lines[i] += mapped_art[i]

            for i in range(3):
                line_length = len(art_lines[i])
                if line_length < 26:
                    padding = (26 - line_length) // 2
                    extra = (26 - line_length) % 2
                    art_lines[i] = '░' * padding + art_lines[i] + '░' * (padding + extra)

            all_art_lines.extend(art_lines)
            if word_index != len(words) - 1:
                all_art_lines.append('░' * 26)

        all_art_lines.append('░' * 26)  # Bottom padding
        output = '\n'.join(all_art_lines)
        self.output_label.configure(text=output)

    def copy(self):
        # Copy the current label's content to the clipboard
        self.clipboard_clear()
        self.clipboard_append(self.output_label.cget("text"))
        self.update()  # Now it stays on the clipboard after the window is closed

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
