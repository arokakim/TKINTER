import tkinter as tk

# --- STEP 1: BRAINS (We'll fill this in later) ---
def save_syntax():
    print("Logic will go here tomorrow!")

# --- STEP 2: THE STAGE ---
root = tk.Tk()
root.title("My Syntax Vault")
root.geometry("400x500")

# --- STEP 3: THE BODY (The Skeleton) ---
# Label 1 & Entry 1
tk.Label(root, text="CONCEPT NAME:", font=("Arial", 10, "bold")).pack(pady=5)
title_entry = tk.Entry(root, width=40)
title_entry.pack(pady=5)

# Label 2 & Text Box (Text is bigger than Entry for multi-line code)
tk.Label(root, text="SYNTAX CODE:", font=("Arial", 10, "bold")).pack(pady=5)
code_text = tk.Text(root, width=40, height=10) # Text widget for long code
code_text.pack(pady=5)

# The Trigger
save_btn = tk.Button(root, text="SAVE TO VAULT", command=save_syntax, bg="green", fg="white")
save_btn.pack(pady=20)

root.mainloop()