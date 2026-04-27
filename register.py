import customtkinter as ctk
from tkinter import messagebox

# UI Theme သတ်မှတ်ခြင်း
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class RegisterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Mini Register")
        self.geometry("420x500")

        self.label = ctk.CTkLabel(self, text="Register System", font=("Arial", 24, "bold"))
        self.label.pack(pady=30)

        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username ကိုရိုက်ပါ", width=280)
        self.username_entry.pack(pady=10)

        self.email_entry = ctk.CTkEntry(self, placeholder_text="Email ကိုရိုက်ပါ", width=280)
        self.email_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password ကိုရိုက်ပါ", show="*", width=280)
        self.password_entry.pack(pady=10)

        self.confirm_entry = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=280)
        self.confirm_entry.pack(pady=10)

        self.register_button = ctk.CTkButton(self, text="Register", command=self.register_event, fg_color="green")
        self.register_button.pack(pady=20)

        self.clear_button = ctk.CTkButton(self, text="Clear", command=self.clear_fields, fg_color="red")
        self.clear_button.pack(pady=8)

        self.help_button = ctk.CTkButton(self, text="Help", command=self.show_help, fg_color="gray")
        self.help_button.pack(pady=8)

    def register_event(self):
        user = self.username_entry.get().strip()
        email = self.email_entry.get().strip()
        pw = self.password_entry.get().strip()
        cpw = self.confirm_entry.get().strip()

        if not user or not email or not pw or not cpw:
            messagebox.showwarning("အချက်အလက်မလုံလောက်ပါ", "အချက်အလက် အားလုံးကို ဖြည့်ပါ။")
            return

        if "@" not in email or "." not in email:
            messagebox.showerror("Email မှားနေပါသည်", "ခိုင်မာသော Email ကို ဖြည့်ပါ။")
            return

        if pw != cpw:
            messagebox.showerror("Password မကိုက်ပါ", "Password နှင့် Confirm Password မကိုက်ပါ။")
            return

        messagebox.showinfo("အောင်မြင်ပါသည်", f"{user} အတွက် Register အောင်မြင်ပါတယ်။")
        self.clear_fields()

    def show_help(self):
        messagebox.showinfo("Help", "Fill all fields and click Register. Example: user1, user1@example.com, 1234")

    def clear_fields(self):
        self.username_entry.delete(0, 'end')
        self.email_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.confirm_entry.delete(0, 'end')

if __name__ == "__main__":
    app = RegisterApp()
    app.mainloop()