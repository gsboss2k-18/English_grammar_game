import customtkinter as ctk
import subprocess
import sys # Needed to correctly reference the python executable

# Set the appearance mode and default color theme
ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 

class DifficultyApp(ctk.CTk):
    """
    A CustomTkinter application for selecting difficulty levels, 
    launching specific Python files based on the selection.
    """
    def __init__(self):
        super().__init__()

        # --- Basic Window Setup ---
        self.title("Difficulty Selector - Future AI Quiz")
        self.geometry("600x400") 
        self.resizable(False, False) 

        # Configure grid layout for the main window to center content
        self.grid_rowconfigure((0, 4), weight=1) 
        self.grid_columnconfigure((0, 2), weight=1) 

        # --- Frame to hold the buttons and labels ---
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(row=1, column=1, rowspan=3, sticky="nsew", padx=20, pady=20)
        
        # Configure content_frame grid
        self.content_frame.grid_columnconfigure(0, weight=1) 
        self.content_frame.grid_columnconfigure(1, weight=1) 
        self.content_frame.grid_rowconfigure((0, 1, 2), weight=1) 


        # --- EASY Button and Label ---
        self.easy_button = ctk.CTkButton(self.content_frame, text="EASY",
                                         font=ctk.CTkFont(size=18, weight="bold"),
                                         command=self.easy_selected, # Linked to new function
                                         width=120, height=40,
                                         fg_color="#2ECC71", 
                                         hover_color="#27AE60") 
        self.easy_button.grid(row=0, column=0, padx=(0, 20), pady=15, sticky="e") 

        self.easy_label = ctk.CTkLabel(self.content_frame, text="IDENTIFY IMAGES",
                                       font=ctk.CTkFont(size=16, weight="bold"))
        self.easy_label.grid(row=0, column=1, padx=(20, 0), pady=15, sticky="w") 

        # --- MEDIUM Button and Label ---
        self.medium_button = ctk.CTkButton(self.content_frame, text="MEDIUM",
                                           font=ctk.CTkFont(size=18, weight="bold"),
                                           command=self.medium_selected, # Linked to new function
                                           width=120, height=40,
                                           fg_color="#3498DB", 
                                           hover_color="#2980B9") 
        self.medium_button.grid(row=1, column=0, padx=(0, 20), pady=15, sticky="e")

        self.medium_label = ctk.CTkLabel(self.content_frame, text="IDENTIFY FROM QUOTES",
                                        font=ctk.CTkFont(size=16, weight="bold"))
        self.medium_label.grid(row=1, column=1, padx=(20, 0), pady=15, sticky="w")

        # --- HARD Button and Label ---
        self.hard_button = ctk.CTkButton(self.content_frame, text="HARD",
                                         font=ctk.CTkFont(size=18, weight="bold"),
                                         command=self.hard_selected, # Linked to new function
                                         width=120, height=40,
                                         fg_color="#E74C3C", 
                                         hover_color="#C0392B") 
        self.hard_button.grid(row=2, column=0, padx=(0, 20), pady=15, sticky="e")

        self.hard_label = ctk.CTkLabel(self.content_frame, text="IDENTIFY FROM NAME",
                                       font=ctk.CTkFont(size=16, weight="bold"))
        self.hard_label.grid(row=2, column=1, padx=(20, 0), pady=15, sticky="w")

    # --- Button Command Functions to Launch Files ---
    
    def launch_script(self, script_name):
        """Helper function to run an external Python script."""
        try:
            # sys.executable gets the path to the Python interpreter currently running the main script
            # This is the most reliable way to execute another Python file
            subprocess.Popen([sys.executable, script_name])
            
            # Optional: Hide the main window if you want the new script to take over
            # self.withdraw() 
            
            print(f"Successfully launched {script_name}")
        except FileNotFoundError:
            print(f"Error: Could not find or launch {script_name}. Make sure it is in the same folder.")
        except Exception as e:
            print(f"An unexpected error occurred while launching {script_name}: {e}")


    def easy_selected(self):
        """Function called when EASY button is clicked."""
        self.launch_script("easy_p.py")

    def medium_selected(self):
        """Function called when MEDIUM button is clicked."""
        self.launch_script("medium_p.py")

    def hard_selected(self):
        """Function called when HARD button is clicked."""
        self.launch_script("hard_p.py")

# --- Run the App ---
if __name__ == "__main__":
    app = DifficultyApp()
    app.mainloop()
