import random
import sys
import os
import math
import wave
import struct
import customtkinter as ctk

# -------------------- SOUND UTILITIES (From eng gra.py) --------------------
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

# --- SOUND PLAYBACK (From eng gra.py) ---
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

# -------------------- PYTHON QUESTION BANK (50 Quotes & Works) --------------------
QUOTE_QUESTIONS = [
    # --- Quotes (25) ---
    {
        "question_text": "Who wrote the famous line: 'All the world's a stage, and all the men and women merely players.'?",
        "options": ["William Shakespeare", "John Milton", "Charles Dickens", "Oscar Wilde"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question_text": "Identify the author of the quote: 'It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife.'",
        "options": ["Jane Austen", "Emily Brontë", "Louisa May Alcott", "Virginia Woolf"],
        "correct_answer": "Jane Austen"
    },
    {
        "question_text": "Who wrote: 'It was the best of times, it was the worst of times...'?",
        "options": ["Charles Dickens", "Thomas Hardy", "George Eliot", "George Orwell"],
        "correct_answer": "Charles Dickens"
    },
    {
        "question_text": "Which poet wrote: 'I wandered lonely as a cloud / That floats on high o'er vales and hills,'?",
        "options": ["William Wordsworth", "Lord Byron", "P. B. Shelley", "John Keats"],
        "correct_answer": "William Wordsworth"
    },
    {
        "question_text": "Identify the author: 'A thing of beauty is a joy for ever: / Its loveliness increases; it will never / Pass into nothingness.'",
        "options": ["John Keats", "S. T. Coleridge", "William Blake", "Alfred Tennyson"],
        "correct_answer": "John Keats"
    },
    {
        "question_text": "The poem 'The Raven' is famous for the refrain: 'Quoth the Raven, '______'.'",
        "options": ["Nevermore", "Forevermore", "Evermore", "Caw-caw"],
        "correct_answer": "Nevermore"
    },
    {
        "question_text": "Identify the American poet who wrote: 'Two roads diverged in a wood, and I— / I took the one less traveled by.'",
        "options": ["Robert Frost", "Walt Whitman", "Emily Dickinson", "T. S. Eliot"],
        "correct_answer": "Robert Frost"
    },
    {
        "question_text": "Identify the author of the dystopian quote: 'All animals are equal, but some animals are more equal than others.'",
        "options": ["George Orwell", "Aldous Huxley", "H. G. Wells", "Evelyn Waugh"],
        "correct_answer": "George Orwell"
    },
    {
        "question_text": "Which poet begins their famous modernist poem 'The Waste Land' with the line: 'April is the cruellest month...'?",
        "options": ["T. S. Eliot", "W. B. Yeats", "Ezra Pound", "Robert Frost"],
        "correct_answer": "T. S. Eliot"
    },
    {
        "question_text": "Which poet wrote the powerful final line of 'Ozymandias': 'Look on my Works, ye Mighty, and despair!'?",
        "options": ["P. B. Shelley", "Lord Byron", "John Keats", "S. T. Coleridge"],
        "correct_answer": "P. B. Shelley"
    },
    {
        "question_text": "Identify the writer who said: 'A man can be destroyed but not defeated.'",
        "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck", "William Faulkner"],
        "correct_answer": "Ernest Hemingway"
    },
    {
        "question_text": "Who wrote the line: 'Where the mind is without fear and the head is held high...' from 'Gitanjali'?",
        "options": ["Rabindranath Tagore", "Sarojini Naidu", "Kamala Das", "A. P. J. Abdul Kalam"],
        "correct_answer": "Rabindranath Tagore"
    },
    {
        "question_text": "Which Irish poet wrote the famous, dark lines: 'Things fall apart; the centre cannot hold...'?",
        "options": ["W. B. Yeats", "James Joyce", "Seamus Heaney", "Samuel Beckett"],
        "correct_answer": "W. B. Yeats"
    },
    {
        "question_text": "Who wrote the quote: 'War is peace. Freedom is slavery. Ignorance is strength.'?",
        "options": ["George Orwell", "Aldous Huxley", "Ayn Rand", "Ray Bradbury"],
        "correct_answer": "George Orwell"
    },
    {
        "question_text": "Which author is known for the line: 'Beauty is truth, truth beauty,—that is all / Ye know on earth, and all ye need to know.'?",
        "options": ["John Keats", "Lord Byron", "William Blake", "Alfred Tennyson"],
        "correct_answer": "John Keats"
    },
    {
        "question_text": "Which author is known for the quote: 'Life is a tale told by an idiot, full of sound and fury, signifying nothing.'?",
        "options": ["William Shakespeare", "John Milton", "T. S. Eliot", "Oscar Wilde"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question_text": "Who wrote the children's classic quote: 'All children, except one, grow up.'?",
        "options": ["J. M. Barrie (Peter Pan)", "A. A. Milne (Winnie the Pooh)", "Lewis Carroll (Alice in Wonderland)", "Roald Dahl (Matilda)"],
        "correct_answer": "J. M. Barrie (Peter Pan)"
    },
    {
        "question_text": "Which poet wrote the line: 'If Winter comes, can Spring be far behind?'?",
        "options": ["P. B. Shelley", "John Keats", "Lord Byron", "William Blake"],
        "correct_answer": "P. B. Shelley"
    },
    {
        "question_text": "Identify the American author: 'Every heart has its secret sorrows, which the world knows not.'",
        "options": ["Henry Wadsworth Longfellow", "Walt Whitman", "Herman Melville", "Mark Twain"],
        "correct_answer": "Henry Wadsworth Longfellow"
    },
    {
        "question_text": "Who wrote the line: 'Do not go gentle into that good night, / Rage, rage against the dying of the light.'?",
        "options": ["Dylan Thomas", "W. H. Auden", "Philip Larkin", "Seamus Heaney"],
        "correct_answer": "Dylan Thomas"
    },
    {
        "question_text": "Which author wrote the line: 'It is only with the heart that one can see rightly; what is essential is invisible to the eye.'?",
        "options": ["Antoine de Saint-Exupéry (The Little Prince)", "Lewis Carroll (Alice in Wonderland)", "E. B. White (Charlotte's Web)", "J. R. R. Tolkien (The Hobbit)"],
        "correct_answer": "Antoine de Saint-Exupéry (The Little Prince)"
    },
    {
        "question_text": "Who said: 'I am no bird; and no net ensnares me: I am a free human being with an independent will.'?",
        "options": ["Charlotte Brontë (Jane Eyre)", "Emily Brontë (Wuthering Heights)", "Jane Austen (Pride and Prejudice)", "Louisa May Alcott (Little Women)"],
        "correct_answer": "Charlotte Brontë (Jane Eyre)"
    },
    {
        "question_text": "Identify the author: 'Lift her like a flower in the wind, / She hangs like a star in the dew of our song.'",
        "options": ["Sarojini Naidu", "Kamala Das", "A. K. Ramanujan", "Nissim Ezekiel"],
        "correct_answer": "Sarojini Naidu"
    },
    {
        "question_text": "Which novelist wrote: 'The past is a foreign country: they do things differently there.'?",
        "options": ["L. P. Hartley", "Virginia Woolf", "George Orwell", "F. Scott Fitzgerald"],
        "correct_answer": "L. P. Hartley"
    },
    {
        "question_text": "Who wrote: 'When you play a part in a play, you say words that are not your own, but you have to feel them like they are your own.'?",
        "options": ["A. P. J. Abdul Kalam (Wings of Fire)", "R. K. Narayan (The Guide)", "Vikram Seth (A Suitable Boy)", "Salman Rushdie (Midnight's Children)"],
        "correct_answer": "A. P. J. Abdul Kalam (Wings of Fire)"
    },

    # --- Literary Works & Facts (25) ---
    {
        "question_text": "The famous detective Hercule Poirot was created by which author?",
        "options": ["Agatha Christie", "Arthur Conan Doyle", "Dorothy L. Sayers", "Ian Fleming"],
        "correct_answer": "Agatha Christie"
    },
    {
        "question_text": "Which novel features the destruction of the One Ring in the land of Mordor?",
        "options": ["The Lord of the Rings", "The Hobbit", "Narnia", "Game of Thrones"],
        "correct_answer": "The Lord of the Rings"
    },
    {
        "question_text": "Which Indian author created the fictional South Indian town of Malgudi?",
        "options": ["R. K. Narayan", "Arundhati Roy", "Vikram Seth", "Amitav Ghosh"],
        "correct_answer": "R. K. Narayan"
    },
    {
        "question_text": "The poem 'Kubla Khan' was written by which Romantic poet after an opium dream?",
        "options": ["S. T. Coleridge", "Lord Byron", "P. B. Shelley", "John Keats"],
        "correct_answer": "S. T. Coleridge"
    },
    {
        "question_text": "Which novel is about a man named Jay Gatsby and his obsessive pursuit of the past?",
        "options": ["The Great Gatsby", "Moby Dick", "The Sun Also Rises", "Of Mice and Men"],
        "correct_answer": "The Great Gatsby"
    },
    {
        "question_text": "The epic poem 'Paradise Lost', about the Fall of Man, was written by whom?",
        "options": ["John Milton", "William Shakespeare", "Geoffrey Chaucer", "Alfred Tennyson"],
        "correct_answer": "John Milton"
    },
    {
        "question_text": "Which author is known for the creation of the character **Sherlock Holmes**?",
        "options": ["Arthur Conan Doyle", "Agatha Christie", "Edgar Allan Poe", "Raymond Chandler"],
        "correct_answer": "Arthur Conan Doyle"
    },
    {
        "question_text": "The novel 'To Kill a Mockingbird' is about lawyer Atticus Finch and his children in which state?",
        "options": ["Alabama (USA)", "Mississippi (USA)", "Texas (USA)", "Georgia (USA)"],
        "correct_answer": "Alabama (USA)"
    },
    {
        "question_text": "Which novel features the famous character **Ebenezer Scrooge**?",
        "options": ["A Christmas Carol", "Oliver Twist", "David Copperfield", "Great Expectations"],
        "correct_answer": "A Christmas Carol"
    },
    {
        "question_text": "The play 'The Importance of Being Earnest' is a Victorian-era satire by which Irish author?",
        "options": ["Oscar Wilde", "George Bernard Shaw", "W. B. Yeats", "James Joyce"],
        "correct_answer": "Oscar Wilde"
    },
    {
        "question_text": "The famous tragic play 'Romeo and Juliet' is set in which Italian city?",
        "options": ["Verona", "Venice", "Rome", "Florence"],
        "correct_answer": "Verona"
    },
    {
        "question_text": "Which novel, set on a moor, tells the passionate and tragic story of Catherine and Heathcliff?",
        "options": ["Wuthering Heights", "Jane Eyre", "Villette", "Tess of the d'Urbervilles"],
        "correct_answer": "Wuthering Heights"
    },
    {
        "question_text": "Which novel follows the story of the March sisters: Meg, Jo, Beth, and Amy?",
        "options": ["Little Women", "The Secret Garden", "A Little Princess", "Heidi"],
        "correct_answer": "Little Women"
    },
    {
        "question_text": "Who is the Booker Prize-winning author of the novel **'The God of Small Things'**?",
        "options": ["Arundhati Roy", "Kiran Desai", "Anita Desai", "Jhumpa Lahiri"],
        "correct_answer": "Arundhati Roy"
    },
    {
        "question_text": "Which dystopian novel features the controlled, genetically stratified 'World State'?",
        "options": ["Brave New World", "Nineteen Eighty-Four", "Fahrenheit 451", "The Giver"],
        "correct_answer": "Brave New World"
    },
    {
        "question_text": "Which author wrote the satirical travel narrative **'Gulliver's Travels'**?",
        "options": ["Jonathan Swift", "Daniel Defoe", "Laurence Sterne", "Henry Fielding"],
        "correct_answer": "Jonathan Swift"
    },
    {
        "question_text": "The epic poem that starts with the invocation 'Sing, goddess, the anger of Peleus' son Achilles' is:",
        "options": ["The Iliad", "The Odyssey", "The Aeneid", "The Epic of Gilgamesh"],
        "correct_answer": "The Iliad"
    },
    {
        "question_text": "Which novel features the Indian character **Babu** and addresses the issue of untouchability?",
        "options": ["Untouchable (Mulk Raj Anand)", "The Guide (R. K. Narayan)", "A Passage to India (E. M. Forster)", "Coolie (Mulk Raj Anand)"],
        "correct_answer": "Untouchable (Mulk Raj Anand)"
    },
    {
        "question_text": "The famous tale 'Alice's Adventures in Wonderland' was written by which author?",
        "options": ["Lewis Carroll", "Beatrix Potter", "A. A. Milne", "J. M. Barrie"],
        "correct_answer": "Lewis Carroll"
    },
    {
        "question_text": "Which English essayist is famous for his gentle, humorous essays, collected in 'Essays of Elia'?",
        "options": ["Charles Lamb", "William Hazlitt", "Thomas De Quincey", "Samuel Johnson"],
        "correct_answer": "Charles Lamb"
    },
    {
        "question_text": "The historical figure **King Arthur** is central to the work 'Idylls of the King' by which poet?",
        "options": ["Alfred Tennyson", "Robert Browning", "William Wordsworth", "Lord Byron"],
        "correct_answer": "Alfred Tennyson"
    },
    {
        "question_text": "Which American author is known for the novel **'Moby Dick'** about the obsessive Captain Ahab?",
        "options": ["Herman Melville", "Nathaniel Hawthorne", "Edgar Allan Poe", "Mark Twain"],
        "correct_answer": "Herman Melville"
    },
    {
        "question_text": "The historical novel **'Ivanhoe'**, set in 12th century England, was written by whom?",
        "options": ["Sir Walter Scott", "Jane Austen", "Charles Dickens", "Thomas Hardy"],
        "correct_answer": "Sir Walter Scott"
    },
    {
        "question_text": "Which Russian author wrote the epic novel **'Crime and Punishment'**?",
        "options": ["Fyodor Dostoevsky", "Leo Tolstoy", "Anton Chekhov", "Maxim Gorky"],
        "correct_answer": "Fyodor Dostoevsky"
    },
    {
        "question_text": "The play **'The Glass Menagerie'** is a well-known work by which American playwright?",
        "options": ["Tennessee Williams", "Arthur Miller", "Eugene O'Neill", "Thornton Wilder"],
        "correct_answer": "Tennessee Williams"
    },
]

SESSION_QUESTION_COUNT = 10 
if len(QUOTE_QUESTIONS) < SESSION_QUESTION_COUNT:
    SESSION_QUESTION_COUNT = len(QUOTE_QUESTIONS)

# -------------------- APP --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class MediumQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🧠 MEDIUM Mode: Quotes and Works")
        self.geometry("800x550") 
        
        self.grid_rowconfigure(1, weight=1)   
        self.grid_columnconfigure(0, weight=1) 

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, pady=(15, 5), padx=20, sticky="ew")
        self.header_frame.grid_columnconfigure((0, 2), weight=1) 
        
        self.stats = ctk.CTkLabel(self.header_frame, text="Score: 0 / 0", font=("Segoe UI", 16, "bold"))
        self.stats.grid(row=0, column=0, sticky="w")
        
        self.title_label = ctk.CTkLabel(self.header_frame, text="MEDIUM QUIZ: QUOTES & WORKS", 
                                        font=("Segoe UI", 40, "bold"))
        self.title_label.grid(row=0, column=1)

        self.play_btn = ctk.CTkButton(self.header_frame, text="Start Quiz ▶", command=self.start_session)
        self.play_btn.grid(row=0, column=2, sticky="e")
        
        # --- Main Content Area ---
        self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.content_frame.grid(row=1, column=0, pady=10, padx=20, sticky="nsew")
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure((0, 1), weight=1)

        # --- Question Area (Top) ---
        self.q_label = ctk.CTkLabel(self.content_frame, text="Press 'Start Quiz' to begin!\n\n(This test is about Quotes and Literary Works)", 
                                    font=("Segoe UI", 30, "bold"), wraplength=700, justify="center")
        self.q_label.grid(row=0, column=0, pady=20, sticky="nsew")

        # --- Options Area (Bottom) ---
        self.options_panel = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        self.options_panel.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.options_panel.grid_columnconfigure((0, 1), weight=1)
        self.options_panel.grid_rowconfigure((0, 1), weight=1) 

        self.option_buttons = []
        option_letters = ["A", "B", "C", "D"]
        for i in range(4):
            r = i // 2
            c = i % 2
            b = ctk.CTkButton(self.options_panel, text=f"{option_letters[i]}. Option Text", height=70,
                              font=("Segoe UI", 16, "bold"),
                              command=lambda i=i: self.check_answer(i),
                              fg_color="#3498DB", hover_color="#2980B9", state="disabled") 
            b.grid(row=r, column=c, pady=10, padx=10, sticky="ew")
            self.option_buttons.append(b)

        self.feedback = ctk.CTkLabel(self.options_panel, text="", font=("Segoe UI", 18))
        self.feedback.grid(row=2, column=0, columnspan=2, pady=10)

        # state
        self.score = 0
        self.q_index = 0
        self.session_questions = []
        self.current_q_data = None


    # --- Quiz Logic Functions ---

    def start_session(self):
        if not QUOTE_QUESTIONS:
            self.q_label.configure(text="No questions loaded.", text_color="red")
            return

        self.score = 0
        self.q_index = 0
        self.feedback.configure(text="")
        # Use random.sample to pick a new set of 10 questions each time
        self.session_questions = random.sample(QUOTE_QUESTIONS, SESSION_QUESTION_COUNT) 
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
        
        # 1. Configure question text (No image needed)
        self.q_label.configure(text=f"Q{self.q_index + 1}. {qobj['question_text']}", text_color="white")
        
        # 2. Configure options
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
        
        # Disable all buttons immediately
        for b in self.option_buttons:
            b.configure(state="disabled")

        if chosen == correct:
            self.score += 1
            self.feedback.configure(text="✅ Correct! Fantastic recall!", text_color="green")
            play_correct()
            # Highlight correct answer
            self.option_buttons[idx].configure(fg_color="#2ECC71")
            
        else:
            self.feedback.configure(text=f"❌ Wrong! The correct answer was: {correct}", text_color="red")
            play_wrong()
            # Highlight wrong choice and correct choice
            self.option_buttons[idx].configure(fg_color="#E74C3C")
            for i, opt in enumerate(self.current_opts):
                if opt == correct:
                    self.option_buttons[i].configure(fg_color="#2ECC71") # Green highlight for correct

        self.update_stats()
        # Pause for 2 seconds before moving to the next question/results
        self.after(2000, self.next_question) 

    def next_question(self):
        self.q_index += 1
        if self.q_index < SESSION_QUESTION_COUNT:
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        pct = int(round((self.score / SESSION_QUESTION_COUNT) * 100))
        self.q_label.configure(text=f"🎉 Quiz Complete! Score: {self.score}/{SESSION_QUESTION_COUNT} ({pct}%).", text_color="yellow")
        self.feedback.configure(text=f"Your recall is excellent! Keep practicing for that centum! Click 'Start Quiz' to try another session.")
        self.play_btn.grid(row=0, column=2, sticky="e") 
        self.play_btn.configure(text="Start Quiz ▶", command=self.start_session)
        for b in self.option_buttons:
            b.configure(text="Option", state="disabled", fg_color="#3498DB")


# --- Run the App ---
if __name__ == "__main__":
    if not QUOTE_QUESTIONS:
        print("ERROR: Question bank is empty. Please check the QUOTE_QUESTIONS list.")
        sys.exit(1)
    app = MediumQuizApp()
    app.mainloop()
