import random
import sys
import os
import math
import wave
import struct
import customtkinter as ctk
from PIL import Image, ImageTk

# --- SOUND UTILITIES (Copied from eng gra.py) ---
SAMPLE_RATE = 44100

def write_wav(filename, samples, sample_rate=SAMPLE_RATE):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        frames = b''.join(struct.pack('<h', max(-32768, min(32767, int(s * 32767)))) for s in samples)
        wf.writeframes(frames)

def tone(duration_sec=0.20, freq=440.0, amplitude=0.5):
    n = int(SAMPLE_RATE * duration_sec)
    for i in range(n):
        t = i / SAMPLE_RATE
        env = 1.0 - (i / n)
        yield amplitude * env * math.sin(2.0 * math.pi * freq * t)

def clap_like(duration_sec=0.25, amplitude=0.6):
    import random as _r
    n = int(SAMPLE_RATE * duration_sec)
    for i in range(n):
        env = (1.0 - i / n) ** 2
        yield amplitude * env * (_r.random() * 2 - 1)

def ensure_wavs():
    made = []
    if not os.path.exists("beep.wav"):
        write_wav("beep.wav", tone(0.22, 520.0, 0.55))
        made.append("beep.wav")
    if not os.path.exists("clap.wav"):
        write_wav("clap.wav", clap_like(0.28, 0.65))
        made.append("clap.wav")
    return made

made_files = ensure_wavs()

# --- SOUND PLAYBACK (Copied from eng gra.py) ---
if sys.platform.startswith("win"):
    import winsound
    import threading

    def play_correct():
        def worker():
            winsound.PlaySound("clap.wav", winsound.SND_FILENAME)
        threading.Thread(target=worker, daemon=True).start()

    def play_wrong():
        def worker():
            winsound.PlaySound("beep.wav", winsound.SND_FILENAME)
        threading.Thread(target=worker, daemon=True).start()
else:
    def play_correct(): pass
    def play_wrong(): pass

# -------------------- PYTHON QUESTION BANK (30 English/World Authors) --------------------
IMAGE_QUESTIONS = [
    # --- British/English Literature ---
    {
        "image_path": "shakespeare.jpg",
        "question_text": "Identify this famous English playwright and poet.",
        "options": ["William Shakespeare", "John Milton", "Oscar Wilde", "Jane Austen"],
        "correct_answer": "William Shakespeare"
    },
    {
        "image_path": "austen.jpg",
        "question_text": "Which author wrote 'Pride and Prejudice'?",
        "options": ["Jane Austen", "Emily Brontë", "Louisa May Alcott", "Virginia Woolf"],
        "correct_answer": "Jane Austen"
    },
    {
        "image_path": "dickens.jpg",
        "question_text": "Identify the writer of 'A Tale of Two Cities' and 'Oliver Twist'.",
        "options": ["Charles Dickens", "George Eliot", "Thomas Hardy", "Arthur Conan Doyle"],
        "correct_answer": "Charles Dickens"
    },
    {
        "image_path": "wordsworth.jpg",
        "question_text": "Which Romantic poet is famous for 'I Wandered Lonely as a Cloud'?",
        "options": ["William Wordsworth", "Lord Byron", "P. B. Shelley", "John Keats"],
        "correct_answer": "William Wordsworth"
    },
    {
        "image_path": "keats.jpg",
        "question_text": "Identify the author of the poem 'Ode to a Nightingale'.",
        "options": ["John Keats", "S. T. Coleridge", "William Blake", "Alfred Tennyson"],
        "correct_answer": "John Keats"
    },
    {
        "image_path": "shelley.jpg",
        "question_text": "Identify the writer of 'Frankenstein'.",
        "options": ["Mary Shelley", "P. B. Shelley", "Jane Austen", "Charles Dickens"],
        "correct_answer": "Mary Shelley"
    },
    {
        "image_path": "tennyson.jpg",
        "question_text": "Identify this major Victorian poet, author of 'Ulysses'.",
        "options": ["Alfred Tennyson", "Robert Browning", "Matthew Arnold", "Thomas Hardy"],
        "correct_answer": "Alfred Tennyson"
    },
    {
        "image_path": "eliot.jpg",
        "question_text": "Identify the poet who wrote 'The Love Song of J. Alfred Prufrock'.",
        "options": ["T. S. Eliot", "Robert Frost", "W. B. Yeats", "Ezra Pound"],
        "correct_answer": "T. S. Eliot"
    },
    {
        "image_path": "shaw.jpg",
        "question_text": "Identify this Nobel Prize-winning Irish playwright who wrote 'Pygmalion'.",
        "options": ["George Bernard Shaw", "Oscar Wilde", "James Joyce", "Samuel Beckett"],
        "correct_answer": "George Bernard Shaw"
    },
    {
        "image_path": "christie.jpg",
        "question_text": "Identify the 'Queen of Crime', creator of Hercule Poirot.",
        "options": ["Agatha Christie", "P. D. James", "Dorothy L. Sayers", "Patricia Highsmith"],
        "correct_answer": "Agatha Christie"
    },
    {
        "image_path": "orwell.jpg",
        "question_text": "Identify the author of 'Animal Farm' and 'Nineteen Eighty-Four'.",
        "options": ["George Orwell", "Aldous Huxley", "H. G. Wells", "Evelyn Waugh"],
        "correct_answer": "George Orwell"
    },
    {
        "image_path": "woolf.jpg",
        "question_text": "Identify this modernist writer, famous for 'Mrs. Dalloway'.",
        "options": ["Virginia Woolf", "E. M. Forster", "D. H. Lawrence", "Joseph Conrad"],
        "correct_answer": "Virginia Woolf"
    },
    {
        "image_path": "conan_doyle.jpg",
        "question_text": "Identify the author and creator of Sherlock Holmes.",
        "options": ["Arthur Conan Doyle", "Robert Louis Stevenson", "Charles Dickens", "Edgar Allan Poe"],
        "correct_answer": "Arthur Conan Doyle"
    },
    {
        "image_path": "bronte.jpg",
        "question_text": "Which author wrote the novel 'Wuthering Heights'?",
        "options": ["Emily Brontë", "Charlotte Brontë", "Anne Brontë", "Jane Austen"],
        "correct_answer": "Emily Brontë"
    },
    {
        "image_path": "tolkien.jpg",
        "question_text": "Identify the writer of 'The Lord of the Rings' trilogy.",
        "options": ["J. R. R. Tolkien", "C. S. Lewis", "J. K. Rowling", "George R. R. Martin"],
        "correct_answer": "J. R. R. Tolkien"
    },

    # --- American Literature ---
    {
        "image_path": "poe.jpg",
        "question_text": "Which American author wrote the macabre poem 'The Raven'?",
        "options": ["Edgar Allan Poe", "Nathaniel Hawthorne", "Herman Melville", "Walt Whitman"],
        "correct_answer": "Edgar Allan Poe"
    },
    {
        "image_path": "twain.jpg",
        "question_text": "Identify the author of 'The Adventures of Tom Sawyer'.",
        "options": ["Mark Twain", "Jules Verne", "Robert Louis Stevenson", "Ernest Hemingway"],
        "correct_answer": "Mark Twain"
    },
    {
        "image_path": "robert_frost.jpg",
        "question_text": "Identify the American poet who wrote 'Stopping by Woods on a Snowy Evening'.",
        "options": ["Robert Frost", "Carl Sandburg", "Walt Whitman", "Emily Dickinson"],
        "correct_answer": "Robert Frost"
    },
    {
        "image_path": "hemingway.jpg",
        "question_text": "Identify this Nobel Prize winner, author of 'The Old Man and the Sea'.",
        "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"],
        "correct_answer": "Ernest Hemingway"
    },
    {
        "image_path": "fitzgerald.jpg",
        "question_text": "Identify the American novelist who wrote 'The Great Gatsby'.",
        "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "John Steinbeck", "J. D. Salinger"],
        "correct_answer": "F. Scott Fitzgerald"
    },
    {
        "image_path": "rowling.jpg",
        "question_text": "Identify the author of the 'Harry Potter' series.",
        "options": ["J.K. Rowling", "Stephen King", "Roald Dahl", "C. S. Lewis"],
        "correct_answer": "J.K. Rowling"
    },

    # --- Russian/World Authors (writing in English or translated) ---
    {
        "image_path": "chekhov.jpg",
        "question_text": "Identify this famous Russian short-story writer and playwright.",
        "options": ["Anton Chekhov", "Leo Tolstoy", "Fyodor Dostoevsky", "Maxim Gorky"],
        "correct_answer": "Anton Chekhov"
    },
    {
        "image_path": "tolstoy.jpg",
        "question_text": "Identify this Russian author of the epic novel 'War and Peace'.",
        "options": ["Leo Tolstoy", "Ivan Turgenev", "Nikolai Gogol", "Boris Pasternak"],
        "correct_answer": "Leo Tolstoy"
    },

    # --- Indian Authors in English ---
    {
        "image_path": "tagore.jpg",
        "question_text": "Identify this Nobel laureate, author of 'Gitanjali'.",
        "options": ["Rabindranath Tagore", "Sarojini Naidu", "Premchand", "Mulk Raj Anand"],
        "correct_answer": "Rabindranath Tagore"
    },
    {
        "image_path": "kalam.jpg",
        "question_text": "Identify this Indian President and author of the popular book 'Wings of Fire'.",
        "options": ["A. P. J. Abdul Kalam", "C. V. Raman", "Homi Bhabha", "Jawaharlal Nehru"],
        "correct_answer": "A. P. J. Abdul Kalam"
    },
    {
        "image_path": "r_k_narayan.jpg",
        "question_text": "Identify the creator of the fictional South Indian town of Malgudi.",
        "options": ["R. K. Narayan", "Arundhati Roy", "Vikram Seth", "Amitav Ghosh"],
        "correct_answer": "R. K. Narayan"
    },
    {
        "image_path": "sarojini_naidu.jpg",
        "question_text": "Identify this 'Nightingale of India' and Indian English poetess.",
        "options": ["Sarojini Naidu", "Kamala Das", "Mahadevi Varma", "Amrita Pritam"],
        "correct_answer": "Sarojini Naidu"
    },
    {
        "image_path": "kamala_das.jpg",
        "question_text": "Identify this major Indian English poet, also known as Madhavikutty.",
        "options": ["Kamala Das", "Arundhati Roy", "Anita Desai", "Shashi Deshpande"],
        "correct_answer": "Kamala Das"
    },
    {
        "image_path": "ruskin_bond.jpg",
        "question_text": "Identify this popular Indian author, known for stories set in the Himalayas.",
        "options": ["Ruskin Bond", "Chetan Bhagat", "Khushwant Singh", "Mulk Raj Anand"],
        "correct_answer": "Ruskin Bond"
    },
    {
        "image_path": "arundhati.jpg",
        "question_text": "Identify the Booker Prize winner for 'The God of Small Things'.",
        "options": ["Arundhati Roy", "Kiran Desai", "Anita Desai", "Jhumpa Lahiri"],
        "correct_answer": "Arundhati Roy"
    },
# --- New Questions (10 Total) ---
    {
        "image_path": "yeats.jpg", # (You'll need a yeats.jpg image)
        "question_text": "Identify this Nobel Prize-winning Irish poet who wrote 'The Second Coming'.",
        "options": ["W. B. Yeats", "Seamus Heaney", "James Joyce", "Samuel Beckett"],
        "correct_answer": "W. B. Yeats"
    },
    {
        "image_path": "eliot_george.jpg", # (You'll need an eliot_george.jpg image)
        "question_text": "Identify the author of 'Middlemarch', whose real name was Mary Ann Evans.",
        "options": ["George Eliot", "Charlotte Brontë", "Elizabeth Gaskell", "Edith Wharton"],
        "correct_answer": "George Eliot"
    },
    {
        "image_path": "lawrence.jpg", # (You'll need a lawrence.jpg image)
        "question_text": "Identify the English novelist who wrote 'Sons and Lovers'.",
        "options": ["D. H. Lawrence", "E. M. Forster", "Aldous Huxley", "Joseph Conrad"],
        "correct_answer": "D. H. Lawrence"
    },
    ]
SESSION_QUESTION_COUNT = 10 
if len(IMAGE_QUESTIONS) < SESSION_QUESTION_COUNT:
    SESSION_QUESTION_COUNT = len(IMAGE_QUESTIONS)

# -------------------- APP --------------------
# (The rest of the class definition and functions remain the same)

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class EasyQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🖼️ EASY Mode: English and World Authors")
        self.geometry("900x650") 
        
        self.grid_rowconfigure(1, weight=1)   
        self.grid_columnconfigure(0, weight=1) 

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, columnspan=2, pady=(15, 5), padx=20, sticky="ew")
        self.header_frame.grid_columnconfigure((0, 2), weight=1) 
        
        self.stats = ctk.CTkLabel(self.header_frame, text="Score: 0 / 0", font=("Segoe UI", 16, "bold"))
        self.stats.grid(row=0, column=0, sticky="w")
        
        self.title_label = ctk.CTkLabel(self.header_frame, text="EASY QUIZ: ENGLISH AND WORLD AUTHORS", 
                                        font=("Segoe UI", 24, "bold"))
        self.title_label.grid(row=0, column=1)

        self.play_btn = ctk.CTkButton(self.header_frame, text="Start Quiz ▶", command=self.start_session)
        self.play_btn.grid(row=0, column=2, sticky="e")
        
        # --- Main Content Area (Side-by-Side) ---
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")
        
        self.content_frame.grid_columnconfigure(0, weight=3) 
        self.content_frame.grid_columnconfigure(1, weight=2) 
        self.content_frame.grid_rowconfigure(0, weight=1)

        # --- Left Panel: Image ---
        self.image_panel = ctk.CTkFrame(self.content_frame, fg_color="gray15")
        self.image_panel.grid(row=0, column=0, padx=(0, 10), sticky="nsew")
        self.image_panel.grid_columnconfigure(0, weight=1)
        self.image_panel.grid_rowconfigure(1, weight=1) 

        self.q_label = ctk.CTkLabel(self.image_panel, text="Press 'Start Quiz' to begin!", 
                                    font=("Segoe UI", 18), wraplength=350, justify="center")
        self.q_label.grid(row=0, column=0, pady=15)

        self.image_label = ctk.CTkLabel(self.image_panel, text="IMAGE AREA", font=("Segoe UI", 24, "bold"), text_color="gray")
        self.image_label.grid(row=1, column=0, sticky="nsew", padx=10, pady=(0, 10))

        # --- Right Panel: Options ---
        self.options_panel = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.options_panel.grid(row=0, column=1, padx=(10, 0), sticky="nsew")
        self.options_panel.grid_columnconfigure(0, weight=1)
        self.options_panel.grid_rowconfigure((0, 1, 2, 3), weight=1) 

        self.option_buttons = []
        option_letters = ["A", "B", "C", "D"]
        for i in range(4):
            b = ctk.CTkButton(self.options_panel, text=f"{option_letters[i]}. Option Text", height=60,
                              font=("Segoe UI", 16, "bold"),
                              command=lambda i=i: self.check_answer(i),
                              fg_color="#3498DB", hover_color="#2980B9", state="disabled") 
            b.grid(row=i, column=0, pady=10, padx=10, sticky="ew")
            self.option_buttons.append(b)

        self.feedback = ctk.CTkLabel(self.options_panel, text="", font=("Segoe UI", 18))
        self.feedback.grid(row=4, column=0, pady=10)

        # state
        self.score = 0
        self.q_index = 0
        self.session_questions = []
        self.current_q_data = None


    # --- Quiz Logic Functions ---

    def start_session(self):
        if not IMAGE_QUESTIONS:
            self.q_label.configure(text="No questions loaded.", text_color="red")
            return

        self.score = 0
        self.q_index = 0
        self.feedback.configure(text="")
        # Use random.sample to pick a new set of 10 questions each time
        self.session_questions = random.sample(IMAGE_QUESTIONS, SESSION_QUESTION_COUNT) 
        self.update_stats()
        self.show_question()
        self.play_btn.grid_forget()

    def update_stats(self):
        self.stats.configure(text=f"Score: {self.score} / {self.q_index}")

    def show_question(self):
        if self.q_index >= SESSION_QUESTION_COUNT:
            self.show_results()
            return
            
        qobj = self.session_questions[self.q_index]
        self.current_q_data = qobj
        
        # 1. Load and display the image (Uses "images" folder)
        try:
            image_filename = qobj['image_path']
            # Join the folder name "images" with the image filename
            full_path = os.path.join("images", image_filename) 
            
            pil_image = Image.open(full_path).resize((400, 400), Image.Resampling.LANCZOS)
            self.quiz_image = ImageTk.PhotoImage(pil_image)
            self.image_label.configure(image=self.quiz_image, text="")
        except FileNotFoundError:
            self.image_label.configure(image=None, text=f"Image Not Found:\nimages/{qobj['image_path']}\nCheck 'images' folder!", text_color="red")
        except Exception as e:
            self.image_label.configure(image=None, text=f"Image Load Error: {e}", text_color="red")
            
        # 2. Configure question and options
        self.q_label.configure(text=f"Q{self.q_index + 1}. {qobj['question_text']}")
        
        opts = qobj["options"][:]
        random.shuffle(opts)
        self.current_opts = opts
        
        option_letters = ["A", "B", "C", "D"]
        for i, b in enumerate(self.option_buttons):
            b.configure(text=f"{option_letters[i]}. {opts[i]}", state="normal", fg_color="#3498DB")
        self.feedback.configure(text="")

    def check_answer(self, idx):
        chosen = self.current_opts[idx]
        correct = self.current_q_data["correct_answer"]
        
        for b in self.option_buttons:
            b.configure(state="disabled")

        if chosen == correct:
            self.score += 1
            self.feedback.configure(text="✅ Correct! Excellent knowledge!", text_color="green")
            play_correct()
            self.option_buttons[idx].configure(fg_color="#2ECC71")
        else:
            self.feedback.configure(text=f"❌ Wrong! The answer was: {correct}", text_color="red")
            play_wrong()
            self.option_buttons[idx].configure(fg_color="#E74C3C")
            for i, opt in enumerate(self.current_opts):
                if opt == correct:
                    self.option_buttons[i].configure(fg_color="#2ECC71")

        self.update_stats()
        self.play_btn.grid(row=0, column=2, sticky="e") 
        self.play_btn.configure(text="Next Question ⏭", command=self.next_question)

    def next_question(self):
        self.play_btn.grid_forget()
        self.q_index += 1
        if self.q_index < SESSION_QUESTION_COUNT:
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        pct = int(round((self.score / SESSION_QUESTION_COUNT) * 100))
        self.q_label.configure(text=f"🎉 Quiz Complete! Score: {self.score}/{SESSION_QUESTION_COUNT} ({pct}%).", text_color="yellow")
        self.image_label.configure(image=None, text=f"Great job! Your English studies are looking good. Keep aiming for that 10th centum!", text_color="white")
        self.feedback.configure(text="Click 'Start Quiz' to try another session.")
        self.play_btn.grid(row=0, column=2, sticky="e") 
        self.play_btn.configure(text="Start Quiz ▶", command=self.start_session)
        for b in self.option_buttons:
            b.configure(text="Option", state="disabled", fg_color="#3498DB")


# --- Run the App ---
if __name__ == "__main__":
    if not IMAGE_QUESTIONS:
        print("ERROR: Question bank is empty. Please check the IMAGE_QUESTIONS list.")
        sys.exit(1)
    app = EasyQuizApp()
    app.mainloop()
