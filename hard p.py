import random
import sys
import os
import math
import wave
import struct
import customtkinter as ctk

# -------------------- SOUND UTILITIES --------------------
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

# --- SOUND PLAYBACK ---
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

# -------------------- PYTHON QUESTION BANK (50 Hard Literary Facts) --------------------
HARD_QUESTIONS = [
    # --- Literary Terms and Devices (25) ---
    {
        "question_text": "What is the term for a 14-line poem with a specific rhyme scheme, traditionally divided into an octave and a sestet?",
        "options": ["Sonnet", "Ode", "Ballad", "Epic"],
        "correct_answer": "Sonnet"
    },
    {
        "question_text": "What narrative style presents a character's thoughts and feelings as they occur, often disjointed and illogical?",
        "options": ["Stream of Consciousness", "Existentialism", "Realism", "Gothic Fiction"],
        "correct_answer": "Stream of Consciousness"
    },
    {
        "question_text": "A figure of speech where a part is used to represent the whole (e.g., 'all hands on deck').",
        "options": ["Synecdoche", "Metonymy", "Apostrophe", "Hyperbole"],
        "correct_answer": "Synecdoche"
    },
    {
        "question_text": "What is the term for poetry written without a regular meter or rhyme scheme?",
        "options": ["Free Verse", "Blank Verse", "Epic Poetry", "Pastoral"],
        "correct_answer": "Free Verse"
    },
    {
        "question_text": "What is the name for the rhythm created by the patterns of stressed and unstressed syllables?",
        "options": ["Meter", "Scansion", "Enjambment", "Rhythm Scheme"],
        "correct_answer": "Meter"
    },
    {
        "question_text": "A speech given by a character alone on stage, revealing their thoughts to the audience.",
        "options": ["Soliloquy", "Monologue", "Aside", "Dialogue"],
        "correct_answer": "Soliloquy"
    },
    {
        "question_text": "The use of hints or clues to suggest events that will occur later in a story.",
        "options": ["Foreshadowing", "Flashback", "Juxtaposition", "Allusion"],
        "correct_answer": "Foreshadowing"
    },
    {
        "question_text": "What is the term for a seemingly contradictory statement that may nonetheles be true?",
        "options": ["Paradox", "Oxymoron", "Aphorism", "Euphemism"],
        "correct_answer": "Paradox"
    },
    {
        "question_text": "A humorous imitation of a serious work, used to mock or satirize the original.",
        "options": ["Parody", "Allegory", "Satire", "Burlesque"],
        "correct_answer": "Parody"
    },
    {
        "question_text": "What is the literary term for a sudden realization or flash of insight, popularized by James Joyce?",
        "options": ["Epiphany", "Catharsis", "Denouement", "Climax"],
        "correct_answer": "Epiphany"
    },
    {
        "question_text": "What is the literary term for the tragic flaw of a hero, leading to their downfall?",
        "options": ["Hamartia", "Hubris", "Pathos", "Peripeteia"],
        "correct_answer": "Hamartia"
    },
    {
        "question_text": "The repetition of consonant sounds at the beginning of words (e.g., 'Peter Piper picked...').",
        "options": ["Alliteration", "Assonance", "Consonance", "Cacophony"],
        "correct_answer": "Alliteration"
    },
    {
        "question_text": "A narrative written in the form of letters, diary entries, or documents.",
        "options": ["Epistolary", "Chronicle", "Picaresque", "Bildungsroman"],
        "correct_answer": "Epistolary"
    },
    {
        "question_text": "What is the term for a long, highly structured lyric poem written in praise of a person or object?",
        "options": ["Ode", "Elegy", "Sonnet", "Limerick"],
        "correct_answer": "Ode"
    },
    {
        "question_text": "What is *Blank Verse*?",
        "options": ["Unrhymed Iambic Pentameter", "Unrhymed Couplets", "Rhymed Tetrameter", "Stanza of Four Lines"],
        "correct_answer": "Unrhymed Iambic Pentameter"
    },
    {
        "question_text": "What is the rhyming pattern of a Shakespearean (English) sonnet?",
        "options": ["ABAB CDCD EFEF GG", "ABBA ABBA CDE CDE", "AABBA", "AABB"],
        "correct_answer": "ABAB CDCD EFEF GG"
    },
    {
        "question_text": "The use of an object or idea to represent something else (e.g., a dove for peace).",
        "options": ["Symbolism", "Imagery", "Metaphor", "Motif"],
        "correct_answer": "Symbolism"
    },
    {
        "question_text": "What is the term for a word whose sound suggests its meaning (e.g., *buzz*, *hiss*)?",
        "options": ["Onomatopoeia", "Alliteration", "Euphony", "Cacophony"],
        "correct_answer": "Onomatopoeia"
    },
    {
        "question_text": "A subtle, often gentle form of sarcasm or mockery is called...",
        "options": ["Irony", "Sarcasm", "Lampoon", "Burlesque"],
        "correct_answer": "Irony"
    },
    {
        "question_text": "A reference to a person, place, event, or another work of literature.",
        "options": ["Allusion", "Illusion", "Innuendo", "Anecdote"],
        "correct_answer": "Allusion"
    },
    {
        "question_text": "The emotional atmosphere or feeling created by the text.",
        "options": ["Mood", "Tone", "Theme", "Atmosphere"],
        "correct_answer": "Mood"
    },
    {
        "question_text": "What is the term for a story within a story (e.g., in *Frankenstein* or *Canterbury Tales*)?",
        "options": ["Frame Story", "Subplot", "Allegory", "Flashback"],
        "correct_answer": "Frame Story"
    },
    {
        "question_text": "What is *Metonymy*?",
        "options": ["Substitution of a word for an idea (e.g., 'the Crown' for royalty)", "A figure of speech where a part represents the whole", "An extended comparison", "A contradiction in terms"],
        "correct_answer": "Substitution of a word for an idea (e.g., 'the Crown' for royalty)"
    },
    {
        "question_text": "The use of exaggerated claims or statements not meant to be taken literally.",
        "options": ["Hyperbole", "Understatement", "Litotes", "Parody"],
        "correct_answer": "Hyperbole"
    },
    {
        "question_text": "The narrative voice that knows everything about all characters, thoughts, and events.",
        "options": ["Omniscient", "First-Person", "Limited", "Objective"],
        "correct_answer": "Omniscient"
    },

    # --- Periods, Authors & Facts (25) ---
    {
        "question_text": "Which literary period emphasized emotion, nature, and the individual, starting in the late 18th century?",
        "options": ["Romanticism", "Neoclassicism", "Modernism", "Victorianism"],
        "correct_answer": "Romanticism"
    },
    {
        "question_text": "The group of poets including Wilfred Owen and Siegfried Sassoon is primarily associated with which historical event?",
        "options": ["World War I", "World War II", "Victorian Era", "English Civil War"],
        "correct_answer": "World War I"
    },
    {
        "question_text": "The novel 'The Catcher in the Rye' is known for its protagonist, the cynical teenager:",
        "options": ["Holden Caulfield", "Jay Gatsby", "Humbert Humbert", "Meursault"],
        "correct_answer": "Holden Caulfield"
    },
    {
        "question_text": "The term *Existentialism* is strongly linked to which author who wrote 'The Stranger'?",
        "options": ["Albert Camus", "Jean-Paul Sartre", "Franz Kafka", "Fyodor Dostoevsky"],
        "correct_answer": "Albert Camus"
    },
    {
        "question_text": "Which collection of tales, written by Geoffrey Chaucer, features pilgrims telling stories on their journey?",
        "options": ["The Canterbury Tales", "The Decameron", "Fables of Aesop", "Gesta Romanorum"],
        "correct_answer": "The Canterbury Tales"
    },
    {
        "question_text": "Which genre is Mary Shelley's *Frankenstein* typically considered to be one of the earliest examples of?",
        "options": ["Gothic/Science Fiction", "Romance", "Realism", "Satire"],
        "correct_answer": "Gothic/Science Fiction"
    },
    {
        "question_text": "The literary movement of *Realism* focused on describing life *exactly* as it is, primarily as a reaction against:",
        "options": ["Romanticism", "Modernism", "Neoclassicism", "Victorianism"],
        "correct_answer": "Romanticism"
    },
    {
        "question_text": "Which famous work by John Bunyan is an allegory of a Christian's journey through life?",
        "options": ["Pilgrim's Progress", "Paradise Lost", "The Faerie Queene", "Canterbury Tales"],
        "correct_answer": "Pilgrim's Progress"
    },
    {
        "question_text": "The novel *Things Fall Apart* is a key work of literature from which country?",
        "options": ["Nigeria", "India", "South Africa", "Kenya"],
        "correct_answer": "Nigeria"
    },
    {
        "question_text": "Which American poet is famous for his experimental long poem 'Leaves of Grass'?",
        "options": ["Walt Whitman", "Emily Dickinson", "Robert Frost", "T. S. Eliot"],
        "correct_answer": "Walt Whitman"
    },
    {
        "question_text": "Which Indian author wrote the 2006 Booker Prize-winning novel *The Inheritance of Loss*?",
        "options": ["Kiran Desai", "Arundhati Roy", "Jhumpa Lahiri", "Vikram Seth"],
        "correct_answer": "Kiran Desai"
    },
    {
        "question_text": "Which collection of poems, written with Wordsworth, is considered to have launched the Romantic Age in England?",
        "options": ["Lyrical Ballads (Coleridge/Wordsworth)", "Songs of Innocence (Blake)", "Childe Harold's Pilgrimage (Byron)", "Odes (Keats)"],
        "correct_answer": "Lyrical Ballads (Coleridge/Wordsworth)"
    },
    {
        "question_text": "What is the main characteristic of the *Victorian Era* in British literature?",
        "options": ["Emphasis on social class, morality, and industrialization", "Focus on reason and classical forms", "Exploration of the subconscious mind", "Simple, direct language"],
        "correct_answer": "Emphasis on social class, morality, and industrialization"
    },
    {
        "question_text": "Which author is credited with writing the first novel in English, *Pamela* (1740)?",
        "options": ["Samuel Richardson", "Henry Fielding", "Daniel Defoe", "Laurence Sterne"],
        "correct_answer": "Samuel Richardson"
    },
    {
        "question_text": "The literary movement that emphasized concise, direct language and clear imagery, led by Ezra Pound.",
        "options": ["Imagism", "Futurism", "Vorticism", "Dadaism"],
        "correct_answer": "Imagism"
    },
    {
        "question_text": "Which Ancient Greek philosopher, through his student Plato, wrote down concepts like the 'Allegory of the Cave'?",
        "options": ["Socrates", "Aristotle", "Homer", "Euripides"],
        "correct_answer": "Socrates"
    },
    {
        "question_text": "What is *Neoclassicism* in literature?",
        "options": ["Emphasis on reason, form, and classical models (18th Century)", "Focus on Medieval chivalry", "Exploration of dark emotions", "Celebration of democracy"],
        "correct_answer": "Emphasis on reason, form, and classical models (18th Century)"
    },
    {
        "question_text": "The novel *One Hundred Years of Solitude* is a prime example of which Latin American genre?",
        "options": ["Magical Realism", "Social Realism", "Postmodernism", "Naturalism"],
        "correct_answer": "Magical Realism"
    },
    {
        "question_text": "Which poet is known for creating the *Dramatic Monologue* form, exemplified in 'My Last Duchess'?",
        "options": ["Robert Browning", "Alfred Tennyson", "Matthew Arnold", "Elizabeth Barrett Browning"],
        "correct_answer": "Robert Browning"
    },
    {
        "question_text": "The term for a group of writers who promoted 'Art for Art's Sake' in the late 19th century.",
        "options": ["Aestheticism", "Pre-Raphaelites", "Decadence", "Modernism"],
        "correct_answer": "Aestheticism"
    },
    {
        "question_text": "Which Indian author wrote the controversial novel *The Satanic Verses*?",
        "options": ["Salman Rushdie", "Arundhati Roy", "V. S. Naipaul", "Amitav Ghosh"],
        "correct_answer": "Salman Rushdie"
    },
    {
        "question_text": "Which play features the famous tragic protagonist, **Willy Loman**?",
        "options": ["Death of a Salesman (Arthur Miller)", "The Glass Menagerie (Tennessee Williams)", "A Streetcar Named Desire (Tennessee Williams)", "Long Day's Journey into Night (Eugene O'Neill)"],
        "correct_answer": "Death of a Salesman (Arthur Miller)"
    },
    {
        "question_text": "The Greek concept of *Catharsis* in tragedy means:",
        "options": ["Purging or cleansing of emotions", "The tragic flaw of the hero", "A sudden reversal of fortune", "The moral of the story"],
        "correct_answer": "Purging or cleansing of emotions"
    },
    {
        "question_text": "The 'Dark Lady' is a recurring figure in the sonnets of which famous playwright and poet?",
        "options": ["William Shakespeare", "John Milton", "Edmund Spenser", "Philip Sidney"],
        "correct_answer": "William Shakespeare"
    },
    {
        "question_text": "Which author is considered the father of the English Essay?",
        "options": ["Francis Bacon", "Joseph Addison", "Richard Steele", "Charles Lamb"],
        "correct_answer": "Francis Bacon"
    },
]

SESSION_QUESTION_COUNT = 10 
if len(HARD_QUESTIONS) < SESSION_QUESTION_COUNT:
    SESSION_QUESTION_COUNT = len(HARD_QUESTIONS)

# -------------------- APP --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class HardQuizApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🔥 HARD Mode: Literary Terms & Facts")
        self.geometry("800x550") 
        
        self.grid_rowconfigure(1, weight=1)   
        self.grid_columnconfigure(0, weight=1) 

        # --- Header ---
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, pady=(15, 5), padx=20, sticky="ew")
        self.header_frame.grid_columnconfigure((0, 2), weight=1) 
        
        self.stats = ctk.CTkLabel(self.header_frame, text="Score: 0 / 0", font=("Segoe UI", 16, "bold"))
        self.stats.grid(row=0, column=0, sticky="w")
        
        self.title_label = ctk.CTkLabel(self.header_frame, text="HARD QUIZ: LITERARY TERMS & FACTS", 
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
        self.q_label = ctk.CTkLabel(self.content_frame, text="Press 'Start Quiz' to begin!\n\n(This test covers advanced Literary Terms and Facts)", 
                                    font=("Segoe UI", 35, "bold"), wraplength=700, justify="center")
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
        if not HARD_QUESTIONS:
            self.q_label.configure(text="No questions loaded.", text_color="red")
            return

        self.score = 0
        self.q_index = 0
        self.feedback.configure(text="")
        # Use random.sample to pick a new set of 10 questions each time
        self.session_questions = random.sample(HARD_QUESTIONS, SESSION_QUESTION_COUNT) 
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
        
        # 1. Configure question text 
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
            self.feedback.configure(text="✅ Correct! You have deep literary knowledge!", text_color="green")
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
        self.feedback.configure(text=f"This is tough! Your score is {self.score}/10. Keep grinding for that centum! Click 'Start Quiz' to try another session.")
        self.play_btn.grid(row=0, column=2, sticky="e") 
        self.play_btn.configure(text="Start Quiz ▶", command=self.start_session)
        for b in self.option_buttons:
            b.configure(text="Option", state="disabled", fg_color="#3498DB")


# --- Run the App ---
if __name__ == "__main__":
    if not HARD_QUESTIONS:
        print("ERROR: Question bank is empty. Please check the HARD_QUESTIONS list.")
        sys.exit(1)
    app = HardQuizApp()
    app.mainloop()
