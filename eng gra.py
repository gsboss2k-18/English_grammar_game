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

# -------------------- SOUND PLAYBACK --------------------
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
    # Non-Windows: no sound
    def play_correct(): pass
    def play_wrong(): pass

# -------------------- QUESTION BANK (100 UNIQUE) --------------------
QUESTIONS = [
    {"q":"Choose the correct article: She bought ___ umbrella.","opts":["a","an","the","no article"],"ans":"an"},
    {"q":"Identify the verb: The children laughed loudly.","opts":["children","laughed","loudly","the"],"ans":"laughed"},
    {"q":"Pick the correct sentence.","opts":["He don’t like milk.","He doesn’t like milk.","He doesn’t likes milk.","He not like milk."],"ans":"He doesn’t like milk."},
    {"q":"Select the correct preposition: He is afraid ___ spiders.","opts":["of","for","at","by"],"ans":"of"},
    {"q":"Choose the correct tense: She ___ to school every day.","opts":["go","goes","gone","going"],"ans":"goes"},
    {"q":"Identify the adjective: The tall tree is old.","opts":["tall","tree","is","old"],"ans":"tall"},
    {"q":"Select the adverb: She sings beautifully.","opts":["She","sings","beautifully","songs"],"ans":"beautifully"},
    {"q":"Plural of 'child'.","opts":["childs","children","childes","childrens"],"ans":"children"},
    {"q":"Past tense of 'write'.","opts":["writed","wrote","written","writes"],"ans":"wrote"},
    {"q":"Correct spelling.","opts":["definately","definitely","definateley","definatly"],"ans":"definitely"},
    {"q":"Choose the article: I saw ___ elephant.","opts":["a","an","the","no article"],"ans":"an"},
    {"q":"Past participle of 'eat'.","opts":["ate","eaten","eated","eats"],"ans":"eaten"},
    {"q":"Comparative of 'good'.","opts":["gooder","more good","better","best"],"ans":"better"},
    {"q":"Superlative of 'bad'.","opts":["worse","worst","most bad","badder"],"ans":"worst"},
    {"q":"Which is an interjection?","opts":["Oh!","and","very","book"],"ans":"Oh!"},
    {"q":"Plural of 'mouse'.","opts":["mouses","mice","mouse","mices"],"ans":"mice"},
    {"q":"Tense of 'I will go tomorrow'.","opts":["simple past","present continuous","simple future","present perfect"],"ans":"simple future"},
    {"q":"He ____ finished his work.","opts":["have","has","had","is"],"ans":"has"},
    {"q":"Opposite of 'fast'.","opts":["rapid","quick","slow","swift"],"ans":"slow"},
    {"q":"Which is a pronoun? ____ is my friend.","opts":["She","Friend","Happy","School"],"ans":"She"},
    {"q":"They are ____ books.","opts":["there","their","they're","theirs"],"ans":"their"},
    {"q":"Past tense of 'go'.","opts":["gone","went","goed","going"],"ans":"went"},
    {"q":"'a, an, the' are ____.","opts":["prepositions","articles","conjunctions","interjections"],"ans":"articles"},
    {"q":"'quickly' is a ____.","opts":["adjective","adverb","noun","preposition"],"ans":"adverb"},
    {"q":"Preposition: He arrived ___ Monday.","opts":["in","on","at","to"],"ans":"on"},
    {"q":"Preposition: She lives ___ Chennai.","opts":["in","on","at","into"],"ans":"in"},
    {"q":"Preposition: Meet me ___ 6 PM.","opts":["in","on","by","at"],"ans":"at"},
    {"q":"Reported speech: He said, 'I am tired.' → He said that he ____ tired.","opts":["was","is","were","has been"],"ans":"was"},
    {"q":"Passive voice: She writes a letter. → A letter ____ by her.","opts":["is written","was written","is writing","has written"],"ans":"is written"},
    {"q":"Neither of the boys ____ here.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"Each of the players ____ ready.","opts":["are","is","were","be"],"ans":"is"},
    {"q":"Everyone must bring ____ own lunch.","opts":["his","her","their","its"],"ans":"their"},
    {"q":"Comparative of 'far' (distance).","opts":["farther","further","most far","more far"],"ans":"farther"},
    {"q":"Superlative of 'little' (amount).","opts":["less","least","littlest","minimum"],"ans":"least"},
    {"q":"I studied hard, ____ I passed.","opts":["but","so","although","because"],"ans":"so"},
    {"q":"One of the dogs ____ barking.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"Correct punctuation: Its raining →","opts":["Its raining.","It's raining.","Its' raining.","Its raining!"],"ans":"It's raining."},
    {"q":"Homophone: I ____ a song.","opts":["herd","heard","hurd","hard"],"ans":"heard"},
    {"q":"This is the man ____ helped me.","opts":["which","who","whom","whose"],"ans":"who"},
    {"q":"The book ____ I bought is new.","opts":["who","whom","that","whose"],"ans":"that"},
    {"q":"The girl to ____ you spoke is my sister.","opts":["who","whom","which","that"],"ans":"whom"},
    {"q":"'Less' is used with ____ nouns.","opts":["countable","uncountable","both","neither"],"ans":"uncountable"},
    {"q":"'Fewer' is used with ____ nouns.","opts":["uncountable","countable","both","neither"],"ans":"countable"},
    {"q":"Collective noun: a ____ of sheep.","opts":["herd","team","flock","swarm"],"ans":"flock"},
    {"q":"Gerund is a verb used as a ____.","opts":["noun","adjective","adverb","preposition"],"ans":"noun"},
    {"q":"Infinitive form is ____.","opts":["verb + ing","to + verb","verb + ed","had + verb"],"ans":"to + verb"},
    {"q":"Identify tense: 'She has finished.'","opts":["simple present","present continuous","present perfect","simple past"],"ans":"present perfect"},
    {"q":"Identify tense: 'They were playing.'","opts":["present continuous","past continuous","past perfect","future continuous"],"ans":"past continuous"},
    {"q":"Identify tense: 'He had eaten.'","opts":["present perfect","past perfect","simple past","past continuous"],"ans":"past perfect"},
    {"q":"If it rains, I ____ home.","opts":["would stay","will stay","stayed","stay"],"ans":"will stay"},
    {"q":"If I were you, I ____ study.","opts":["will","would","shall","must"],"ans":"would"},
    {"q":"The news ____ good.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"Mathematics ____ my favorite subject.","opts":["are","is","were","be"],"ans":"is"},
    {"q":"Tag question: You are ready, ____?","opts":["are you","aren't you","isn't you","weren't you"],"ans":"aren't you"},
    {"q":"He did not ____ the test.","opts":["passed","passing","pass","passes"],"ans":"pass"},
    {"q":"I prefer tea ____ coffee.","opts":["than","over","to","with"],"ans":"to"},
    {"q":"Phrasal verb 'look after' means ____.","opts":["search for","take care of","admire","ignore"],"ans":"take care of"},
    {"q":"Neither Riya nor her friends ____ coming.","opts":["is","are","was","be"],"ans":"are"},
    {"q":"Either the teacher or the students ____ here.","opts":["is","are","was","be"],"ans":"are"},
    {"q":"Past tense of 'teach'.","opts":["teached","taught","teach","teaches"],"ans":"taught"},
    {"q":"Past tense of 'bring'.","opts":["brang","brought","bringed","bring"],"ans":"brought"},
    {"q":"The police ____ investigating.","opts":["is","are","was","has"],"ans":"are"},
    {"q":"He is ____ honest man.","opts":["a","an","the","no article"],"ans":"an"},
    {"q":"He is good ____ math.","opts":["in","at","on","with"],"ans":"at"},
    {"q":"I am interested ____ music.","opts":["at","on","in","with"],"ans":"in"},
    {"q":"They will finish the work. → The work ____ by them.","opts":["will be finished","is finished","was finished","has finished"],"ans":"will be finished"},
    {"q":"He said, 'I can swim.' → He said that he ____ swim.","opts":["can","could","can be","would"],"ans":"could"},
    {"q":"He has lived here ____ 2010.","opts":["for","since","from","by"],"ans":"since"},
    {"q":"She has lived here ____ five years.","opts":["since","for","by","from"],"ans":"for"},
    {"q":"Part of speech: 'beauty'.","opts":["adjective","adverb","noun","verb"],"ans":"noun"},
    {"q":"Part of speech: 'beautiful'.","opts":["adjective","noun","verb","adverb"],"ans":"adjective"},
    {"q":"Between you and ____ , this is a secret.","opts":["I","me","myself","mine"],"ans":"me"},
    {"q":"It is I who ____ to blame.","opts":["is","are","am","be"],"ans":"am"},
    {"q":"Let Rahul and ____ go.","opts":["I","me","myself","mine"],"ans":"me"},
    {"q":"One should do ____ duty.","opts":["his","one’s","their","her"],"ans":"one’s"},
    {"q":"The committee ____ divided.","opts":["are","is","were","be"],"ans":"is"},
    {"q":"Correct spelling.","opts":["embarass","embarrass","embaras","embarrasss"],"ans":"embarrass"},
    {"q":"Correct spelling.","opts":["neccessary","necessary","necesary","neccesary"],"ans":"necessary"},
    {"q":"Correct spelling.","opts":["occurence","occurrance","occurrence","occurance"],"ans":"occurrence"},
    {"q":"Scissors ____ sharp.","opts":["is","are","was","has"],"ans":"are"},
    {"q":"Ten kilometers ____ a long distance.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"The number of students ____ increasing.","opts":["are","is","were","be"],"ans":"is"},
    {"q":"A number of students ____ absent.","opts":["is","are","was","be"],"ans":"are"},
    {"q":"By 2026, I ____ my course.","opts":["finish","will finish","will have finished","have finished"],"ans":"will have finished"},
    {"q":"Voice: 'The ball was thrown by John.'","opts":["active","passive","middle","none"],"ans":"passive"},
    {"q":"Word order: subject + verb + object is ____.","opts":["OSV","SOV","SVO","VSO"],"ans":"SVO"},
    {"q":"Punctuation: 'Where are you' →","opts":["Where are you?","Where are you.","Where are you!","Where are you,"],"ans":"Where are you?"},
    {"q":"Punctuation: 'Wow that’s great' →","opts":["Wow that’s great.","Wow, that’s great!","Wow; that’s great","Wow: that’s great"],"ans":"Wow, that’s great!"},
    {"q":"Use 'an' before ____.","opts":["university","one","hour","European"],"ans":"hour"},
    {"q":"I look forward ____ meeting you.","opts":["for","to","at","on"],"ans":"to"},
    {"q":"He is taller ____ me.","opts":["then","that","than","to"],"ans":"than"},
    {"q":"Order of adjectives: 'a cup of ___ tea'","opts":["hot delicious","delicious hot","deliciously hot","hotly delicious"],"ans":"delicious hot"},
    {"q":"Clause type: 'because it was raining'","opts":["main clause","subordinate clause","phrase","compound clause"],"ans":"subordinate clause"},
    {"q":"He insisted ____ paying the bill.","opts":["in","on","for","to"],"ans":"on"},
    {"q":"She is ____ European artist.","opts":["an","a","the","no article"],"ans":"a"},
    {"q":"This is the ____ book I have ever read.","opts":["better","good","best","most good"],"ans":"best"},
    {"q":"By the time we arrived, the movie ____.","opts":["started","had started","has started","was starting"],"ans":"had started"},
    {"q":"She prefers reading ____ watching TV.","opts":["than","over","to","against"],"ans":"to"},
    {"q":"Neither of the answers ____ correct.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"Everyone ____ invited.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"We have ____ sugar left.","opts":["few","a few","little","many"],"ans":"little"},
    {"q":"There are ____ students in the class.","opts":["much","many","little","a little"],"ans":"many"},
    {"q":"I have ____ books.","opts":["few","little","much","a little"],"ans":"few"},
    {"q":"He is the ____ of the two.","opts":["tall","taller","tallest","most tall"],"ans":"taller"},
    {"q":"This is ____ most interesting story.","opts":["a","an","the","no article"],"ans":"the"},
    {"q":"She is looking forward to ____ abroad.","opts":["study","studied","studying","to study"],"ans":"studying"},
    {"q":"I would rather ____ at home.","opts":["to stay","stayed","staying","stay"],"ans":"stay"},
    {"q":"Hardly had we reached ____ it started raining.","opts":["than","then","when","that"],"ans":"when"},
    {"q":"Scarcely had he left ____ I arrived.","opts":["than","when","then","that"],"ans":"when"},
    {"q":"Bread and butter ____ my breakfast.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"Either Ramesh or Suresh ____ to blame.","opts":["are","were","is","be"],"ans":"is"},
    {"q":"He has no intention ____ leaving.","opts":["to","for","of","in"],"ans":"of"},
    {"q":"I am not used ____ spicy food.","opts":["to","for","with","of"],"ans":"to"},
    {"q":"He congratulated me ____ my success.","opts":["for","about","on","at"],"ans":"on"},
    {"q":"I object ____ his behavior.","opts":["to","for","on","at"],"ans":"to"},
    {"q":"Please provide me ____ your address.","opts":["with","to","at","for"],"ans":"with"},
    {"q":"He is famous ____ his inventions.","opts":["for","about","of","at"],"ans":"for"},
    {"q":"She is afraid ____ dogs.","opts":["to","for","of","with"],"ans":"of"}
]


assert len(QUESTIONS) == 118, f"Expected 118 questions, found {len(QUESTIONS)}"

# -------------------- APP --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GeoParthyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("⚡ GeoParthy — English Grammar (10 Q Session)")
        self.geometry("850x600")

        # state
        self.score = 0
        self.q_index = 0
        self.session_questions = []
        self.current_q = None
        self.current_opts = None

        # UI
        self.header = ctk.CTkLabel(self, text="🎯 GeoParthy: English Grammar",
                                   font=("Segoe UI", 50, "bold"))
        self.header.pack(pady=10)

        self.stats = ctk.CTkLabel(self, text="Score: 0 / 0", font=("Segoe UI", 20, "bold"))
        self.stats.pack(pady=4)

        self.q_frame = ctk.CTkFrame(self, corner_radius=16)
        self.q_frame.pack(padx=20, pady=12, fill="x")
        self.q_label = ctk.CTkLabel(self.q_frame, text="", wraplength=780,
                                    font=("Segoe UI", 30), justify="left")
        self.q_label.pack(padx=16, pady=16)

        self.opt_frame = ctk.CTkFrame(self, corner_radius=16)
        self.opt_frame.pack(padx=20, pady=8, fill="x")
        self.option_buttons = []
        for i in range(4):
            b = ctk.CTkButton(self.opt_frame, text="", height=46, command=lambda i=i: self.check_answer(i))
            b.pack(pady=6, padx=16, fill="x")
            self.option_buttons.append(b)

        self.feedback = ctk.CTkLabel(self, text="", font=("Segoe UI", 30))
        self.feedback.pack(pady=10)

        self.nav = ctk.CTkFrame(self, corner_radius=16)
        self.nav.pack(pady=10)
        self.play_btn = ctk.CTkButton(self.nav, text="Start ▶", command=self.start_session)
        self.play_btn.grid(row=0, column=0, padx=8)

        if made_files:
            info = ctk.CTkLabel(self, text=f"Created sound files: {', '.join(made_files)}", font=("Segoe UI", 15))
            info.pack(pady=4)

    def start_session(self):
        self.score = 0
        self.q_index = 0
        self.feedback.configure(text="")
        self.session_questions = random.sample(QUESTIONS, 10)
        self.update_stats()
        self.show_question()

    def update_stats(self):
        self.stats.configure(text=f"Score: {self.score} / {self.q_index}")

    def show_question(self):
        qobj = self.session_questions[self.q_index]
        self.current_q = qobj
        opts = qobj["opts"][:]
        random.shuffle(opts)
        self.current_opts = opts

        self.q_label.configure(text=f"Q{self.q_index+1}. {qobj['q']}")
        for i, b in enumerate(self.option_buttons):
            b.configure(text=opts[i], state="normal", fg_color="gray25")
        self.feedback.configure(text="")

    def check_answer(self, idx):
        chosen = self.current_opts[idx]
        correct = self.current_q["ans"]
        if chosen == correct:
            self.score += 1
            self.feedback.configure(text="✅ Correct!", text_color="green")
            play_correct()
            for i, b in enumerate(self.option_buttons):
                b.configure(state="disabled")
                if self.current_opts[i] == correct:
                    b.configure(fg_color="#14532d")
            self.after(2000, self.next_question)    # <-- Wait 2 seconds before proceeding
        else:
            self.feedback.configure(text=f"❌ Wrong! Correct answer: {correct}", text_color="red")
            play_wrong()
            # Disable all buttons and highlight answers
            for i, b in enumerate(self.option_buttons):
                b.configure(state="disabled")
                if self.current_opts[i] == correct:
                    b.configure(fg_color="#14532d")    # correct: green
                elif i == idx:
                    b.configure(fg_color="#7f1d1d")    # wrong: dark red
                else:
                    b.configure(fg_color="gray25")     # others: neutral
            self.after(2000, self.next_question)      # <-- Wait 2 seconds before proceeding

    def next_question(self):
        self.q_index += 1
        self.update_stats()
        if self.q_index < 10:
            self.show_question()
        else:
            self.show_results()

    def show_results(self):
        pct = int(round((self.score / 10) * 100))
        self.q_label.configure(text=f"🎉 Session complete! You scored {self.score}/10  ({pct}%).")
        for b in self.option_buttons:
            b.configure(text="", state="disabled")
        self.feedback.configure(text="Click Play Again to try another random 10.")
        self.play_btn.configure(text="Play Again 🔁", command=self.start_session)

if __name__ == "__main__":
    app = GeoParthyApp()
    app.mainloop()
