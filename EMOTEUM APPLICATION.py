import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime


# ==========================================
# EMOTION ENTRY CLASS
# ==========================================
class EmotionEntry:

    def __init__(self, emotion, description, privacy, tags):

        self.timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        self.emotion = emotion
        self.description = description
        self.privacy = privacy
        self.tags = tags


# ==========================================
# MAIN APPLICATION
# ==========================================
class EmoteumApplication:

    def __init__(self, root):

        self.root = root
        self.root.title("EMOTEUM APPLICATION")
        self.root.geometry("1100x700")
        self.root.configure(bg="#ED389E")

        self.entries = []

        # =====================================
        # TITLE
        # =====================================

        title = tk.Label(
            root,
            text="EMOTEUM APPLICATION",
            font=("Arial", 28, "bold"),
            bg="#EDE7F6",
            fg="#5E35B1"
        )

        title.pack(pady=10)

        subtitle = tk.Label(
            root,
            text=(
                "Echoes of Muted Outpourings and "
                "Therapeutic Expressions in a Unified Media"
            ),
            font=("Arial", 12),
            bg="#EDE7F6",
            fg="#4527A0"
        )

        subtitle.pack(pady=5)

        # =====================================
        # MAIN FRAME
        # =====================================

        main_frame = tk.Frame(root, bg="#EDE7F6")
        main_frame.pack(fill="both", expand=True, padx=20)

        # =====================================
        # LEFT PANEL
        # =====================================

        left_frame = tk.Frame(
            main_frame,
            bg="white",
            bd=2,
            relief="ridge"
        )

        left_frame.pack(side="left", fill="both",
                        expand=True, padx=10, pady=10)

        # =====================================
        # RIGHT PANEL
        # =====================================

        right_frame = tk.Frame(
            main_frame,
            bg="white",
            bd=2,
            relief="ridge"
        )

        right_frame.pack(side="right", fill="both",
                         expand=True, padx=10, pady=10)

        # =====================================
        # CREATE ENTRY SECTION
        # =====================================

        tk.Label(
            left_frame,
            text="Create Emotion Entry",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#5E35B1"
        ).pack(pady=10)

        # Emotion
        tk.Label(left_frame,
                 text="Emotion",
                 bg="white").pack(anchor="w", padx=20)

        self.emotion_box = ttk.Combobox(
            left_frame,
            values=[
                "Happy",
                "Sad",
                "Angry",
                "Anxious",
                "Excited"
            ]
        )

        self.emotion_box.pack(fill="x", padx=20, pady=5)

        # Description
        tk.Label(left_frame,
                 text="Description",
                 bg="white").pack(anchor="w", padx=20)

        self.description_text = tk.Text(
            left_frame,
            height=8
        )

        self.description_text.pack(
            fill="x",
            padx=20,
            pady=5
        )

        # Tags
        tk.Label(left_frame,
                 text="Tags",
                 bg="white").pack(anchor="w", padx=20)

        self.tags_entry = tk.Entry(left_frame)
        self.tags_entry.pack(fill="x", padx=20, pady=5)

        # Privacy
        tk.Label(left_frame,
                 text="Privacy",
                 bg="white").pack(anchor="w", padx=20)

        self.privacy_box = ttk.Combobox(
            left_frame,
            values=[
                "Private",
                "Public",
                "Anonymous"
            ]
        )

        self.privacy_box.pack(fill="x", padx=20, pady=5)

        # SAVE BUTTON
        save_button = tk.Button(
            left_frame,
            text="Save Emotion Entry",
            bg="#5E35B1",
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.save_entry
        )

        save_button.pack(pady=15)

        # =====================================
        # THERAPEUTIC PROMPT SECTION
        # =====================================

        tk.Label(
            right_frame,
            text="Therapeutic Prompt",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#5E35B1"
        ).pack(pady=10)

        self.prompt_label = tk.Label(
            right_frame,
            text="Select an emotion to receive a prompt.",
            bg="#D1C4E9",
            fg="#311B92",
            wraplength=350,
            font=("Arial", 12),
            padx=20,
            pady=20
        )

        self.prompt_label.pack(padx=20, pady=10, fill="x")

        prompt_button = tk.Button(
            right_frame,
            text="Generate Prompt",
            bg="#7E57C2",
            fg="white",
            command=self.generate_prompt
        )

        prompt_button.pack(pady=10)

        # =====================================
        # EXERCISES SECTION
        # =====================================

        tk.Label(
            right_frame,
            text="Wellness Exercises",
            font=("Arial", 18, "bold"),
            bg="white",
            fg="#5E35B1"
        ).pack(pady=10)

        exercise_frame = tk.Frame(right_frame, bg="white")
        exercise_frame.pack()

        self.timer_label = tk.Label(
            right_frame,
            text="00:00",
            font=("Arial", 35, "bold"),
            bg="white",
            fg="#4527A0"
        )

        self.timer_label.pack(pady=10)

        tk.Button(
            exercise_frame,
            text="Breathing Exercise",
            bg="#42A5F5",
            fg="white",
            command=lambda: self.start_timer(60)
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            exercise_frame,
            text="Meditation",
            bg="#66BB6A",
            fg="white",
            command=lambda: self.start_timer(120)
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            exercise_frame,
            text="Positive Reflection",
            bg="#FFA726",
            fg="white",
            command=lambda: self.start_timer(90)
        ).grid(row=0, column=2, padx=5)

        # =====================================
        # ARCHIVE SECTION
        # =====================================

        tk.Label(
            root,
            text="Emotional Archive",
            font=("Arial", 18, "bold"),
            bg="#EDE7F6",
            fg="#5E35B1"
        ).pack()

        columns = (
            "Date",
            "Emotion",
            "Description",
            "Tags",
            "Privacy"
        )

        self.tree = ttk.Treeview(
            root,
            columns=columns,
            show="headings",
            height=10
        )

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=180)

        self.tree.pack(fill="both",
                       expand=True,
                       padx=20,
                       pady=10)

        self.remaining_time = 0

    # ==========================================
    # SAVE ENTRY
    # ==========================================

    def save_entry(self):

        emotion = self.emotion_box.get()
        description = self.description_text.get(
            "1.0",
            tk.END
        ).strip()

        privacy = self.privacy_box.get()
        tags = self.tags_entry.get()

        if not emotion or not description:
            messagebox.showerror(
                "Error",
                "Please fill all required fields."
            )
            return

        entry = EmotionEntry(
            emotion,
            description,
            privacy,
            tags
        )

        self.entries.append(entry)

        self.tree.insert(
            "",
            tk.END,
            values=(
                entry.timestamp,
                entry.emotion,
                entry.description,
                entry.tags,
                entry.privacy
            )
        )

        messagebox.showinfo(
            "Success",
            "Emotion Entry Saved Successfully!"
        )

        self.description_text.delete("1.0", tk.END)
        self.tags_entry.delete(0, tk.END)

    # ==========================================
    # PROMPT GENERATOR
    # ==========================================

    def generate_prompt(self):

        emotion = self.emotion_box.get().lower()

        prompts = {
            "happy": "Write about your happiest memory today.",
            "sad": "Describe what made you feel sad.",
            "angry": "Express your frustrations safely.",
            "anxious": "List things that calm your mind.",
            "excited": "Share what excites you most today."
        }

        prompt = prompts.get(
            emotion,
            "Reflect on your current feelings."
        )

        self.prompt_label.config(text=prompt)

    # ==========================================
    # TIMER
    # ==========================================

    def start_timer(self, seconds):

        self.remaining_time = seconds
        self.update_timer()

    def update_timer(self):

        mins = self.remaining_time // 60
        secs = self.remaining_time % 60

        self.timer_label.config(
            text=f"{mins:02}:{secs:02}"
        )

        if self.remaining_time > 0:
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)

        else:
            messagebox.showinfo(
                "Exercise Complete",
                "Wellness exercise finished!"
            )


# ==========================================
# RUN APPLICATION
# ==========================================

root = tk.Tk()
app = EmoteumApplication(root)
root.mainloop()
