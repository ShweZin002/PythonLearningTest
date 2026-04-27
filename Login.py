import customtkinter as ctk
from tkinter import messagebox
 
# UI Theme သတ်မှတ်ခြင်း
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
 
class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
 
        self.title("Mini Login & Dashboard")
        self.geometry("400x450")
 
        # --- ခေါင်းစဉ် ---
        self.label = ctk.CTkLabel(self, text="Login System", font=("Arial", 24, "bold"))
        self.label.pack(pady=30)
 
        # --- Username ရိုက်ရန်နေရာ ---
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username ကိုရိုက်ပါ", width=250)
        self.username_entry.pack(pady=10)
 
        # --- Password ရိုက်ရန်နေရာ ---
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password ကိုရိုက်ပါ", show="*", width=250)
        self.password_entry.pack(pady=10)
 
        # --- Login ခလုတ် ---
        self.login_button = ctk.CTkButton(self, text="Login ဝင်မည်", command=self.login_event, fg_color="green")
        self.login_button.pack(pady=20)
 
        # --- အခြား ခလုတ်များ (Extra Buttons) ---
        self.info_button = ctk.CTkButton(self, text="Help / အကူအညီ", command=self.show_info, fg_color="gray")
        self.info_button.pack(pady=5)
 
        self.clear_button = ctk.CTkButton(self, text="Clear / ဖျက်မည်", command=self.clear_fields, fg_color="red")
        self.clear_button.pack(pady=5)
 
    def login_event(self):
        user = self.username_entry.get()
        pw = self.password_entry.get()
 
        # ရိုးရှင်းသော Login စစ်ဆေးမှု (Username: admin, PW: 123)
        if user == "admin" and pw == "123":
            messagebox.showinfo("အောင်မြင်ပါသည်", "Login ဝင်ရောက်မှု အောင်မြင်ပါသည်!")
            self.label.configure(text=f"Welcome, {user}!", text_color="yellow")
        else:
            messagebox.showerror("မှားယွင်းနေပါသည်", "Username သို့မဟုတ် Password မှားနေပါသည်။")
 
    def show_info(self):
        messagebox.showinfo("Help", "Username: admin \nPassword: 123 \nဖြင့် စမ်းသပ်ကြည့်ပါ။")
 
    def clear_fields(self):
        self.username_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
 
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()