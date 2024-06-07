import customtkinter as ctk

# Initialize the main window
root = ctk.CTk()

# Set the window title
root.title("CustomTkinter Customized Button")

# Set the window size
root.geometry("400x300")

# Create a customized button
custom_button = ctk.CTkButton(
    master=root, 
    text="Custom Button",
    fg_color="#FF6347",     # Button color
    text_color="#FFFFFF",   # Text color
    hover_color="#FF4500"   # Hover color
)

# Place the button in the window
custom_button.pack(pady=20)

# Start the main event loop
root.mainloop()
