import tkinter as tk
from tkinter import ttk
from DCMovieData import get_dc_movies
from BubbleSort import BubbleSorter

class DCMovieGUI:
    def __init__(self, root, movies):
        self.root = root
        self.movies = movies
        
        self.root.title("20 อันดับหนังทำรายได้ DC")
        self.root.geometry("1100x600") 
        self.root.configure(bg="#0f111a") 

        self.setup_ui()
        self.sort_by("box_office")

    def setup_ui(self):
        title_label = tk.Label(
            self.root, 
            text="20 อันดับหนังทำรายได้ DC", 
            font=("Tahoma", 18, "bold"), 
            fg="white", 
            bg="#200052",
            padx=15, 
            pady=5
        )
        title_label.place(x=30, y=20)

        btn_style = {
            "font": ("Tahoma", 12, "bold"),
            "fg": "white",
            "bg": "#f04747", 
            "activebackground": "#d03737",
            "activeforeground": "white",
            "bd": 0,
            "width": 14,
            "height": 1,
            "cursor": "hand2"
        }

        btn_boxoffice = tk.Button(self.root, text="รายได้หนัง", command=lambda: self.sort_by("box_office"), **btn_style)
        btn_boxoffice.place(x=450, y=30)

        btn_year = tk.Button(self.root, text="ปีฉาย", command=lambda: self.sort_by("year"), **btn_style)
        btn_year.place(x=620, y=30)

        btn_rating = tk.Button(self.root, text="คะแนน", command=lambda: self.sort_by("rating"), **btn_style)
        btn_rating.place(x=790, y=30)

        table_frame = tk.Frame(self.root, bg="#0f111a")
        table_frame.place(x=30, y=90, width=1040, height=480)

        style = ttk.Style()
        # ป้องกันปัญหาเรื่องธีมไม่รองรับในบางเครื่อง
        try:
            style.theme_use("clamp")
        except tk.TclError:
            style.theme_use("default")

        style.configure("Treeview",
                        background="#161925",
                        foreground="white",
                        fieldbackground="#161925",
                        rowheight=40,
                        font=("Tahoma", 10))
        style.configure("Treeview.Heading",
                        background="#0f111a",
                        foreground="white",
                        font=("Tahoma", 10, "bold"))
        style.map("Treeview", background=[("selected", "#2b304c")])

        columns = ("rank", "title", "year", "genre", "director", "budget", "box_office", "rating", "duration", "mpaa")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        headers = {
            "rank": ("ลำดับ", 50),
            "title": ("ชื่อ", 200),
            "year": ("ปี", 70),
            "genre": ("หมวดหมู่", 110),
            "director": ("ผู้กำกับ", 140),
            "budget": ("ทุนสร้าง", 90),
            "box_office": ("รายได้", 100),
            "rating": ("IMDb", 60),
            "duration": ("ความยาว", 80),
            "mpaa": ("เรทอายุ", 70)
        }

        for col, (text, width) in headers.items():
            self.tree.heading(col, text=text)
            align = "center" if col in ["rank", "year", "rating", "duration", "mpaa", "budget", "box_office"] else "w"
            self.tree.column(col, width=width, anchor=align)

        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def sort_by(self, criterion):
        if criterion == "box_office":
            sorted_movies = BubbleSorter.sort_by_box_office(self.movies, descending=True)
        elif criterion == "year":
            sorted_movies = BubbleSorter.sort_by_year(self.movies, descending=True)
        elif criterion == "rating":
            sorted_movies = BubbleSorter.sort_by_rating(self.movies, descending=True)
        else:
            sorted_movies = self.movies

        self.display_movies(sorted_movies)

    def display_movies(self, movie_list):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for i, movie in enumerate(movie_list, start=1):
            self.tree.insert("", "end", values=(
                i,
                movie.title,
                movie.release_year,
                movie.genre,
                movie.director,
                f"${movie.budget_m:,.0f}M",
                f"${movie.box_office_m:,.0f}M",
                movie.rating,
                f"{movie.duration_mins} นาที",
                movie.mpaa_rating
            ))

if __name__ == "__main__":
    root = tk.Tk()
    movies_data = get_dc_movies()
    app = DCMovieGUI(root, movies_data)
    root.mainloop()