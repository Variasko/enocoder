from customtkinter import *
from function import *
from PIL import Image

class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Шифратор")
        self.geometry("800x450+300+200")
        set_appearance_mode("dark")
        set_default_color_theme("green")
        self.resizable(False, False)

        self.pathToIco = r"images/001.ico"
        self.iconbitmap(self.pathToIco)

        self.appearance_mode_optionemenu = CTkOptionMenu(
            self,
            values=["Тёмная", "Светлая", "Системная"],
            command=self.change_appearance_mode_event,
            width=40
        )
        self.appearance_mode_optionemenu.place(x=0, y=0)

        self.mainWidgets()
        self.childenWidgetsCezar()



    def mainWidgets(self):
        self.tab = CTkTabview(
            self,
            width=600
            )
        self.tab.place(x=100, y=50)

        self.tab.add("Шифр цезаря")
        self.tab.add("Шифр 2")
        self.tab.add("Шифр 3")

    def childenWidgetsCezar(self):
        #Cezar enocode
        self.language = CTkOptionMenu(
            self.tab.tab("Шифр цезаря"),
            values=["Русский RU", "Анлийский ENG"]
        )
        self.language.grid(row=1, column=1)
        #input widgets for Cezar enocode
        self.inLabel = CTkLabel(
            self.tab.tab("Шифр цезаря"),
            text="Введите текст для шифрации",
            font=("Arial", 12)
            )
        self.inLabel.grid(row=0, column=0)
        self.input = CTkTextbox(
            self.tab.tab("Шифр цезаря"),
            height=100
        )
        self.input.grid(row=1, column=0)
        self.inpKeyLabel = CTkLabel(
            self.tab.tab("Шифр цезаря"),
            text="Ключ",
            font=("Arial", 12)
        )
        self.inpKeyLabel.grid(row=2, column=1)
        self.inputKey = CTkEntry(
            self.tab.tab("Шифр цезаря"),
            width=40
        )
        self.inputKey.grid(row=3, column=1, padx=70)

        #output widges for Cezar enocode
        self.outLabel = CTkLabel(
            self.tab.tab("Шифр цезаря"),
            text="Результат",
            font=("Arial", 12)
        )
        self.outLabel.grid(row=0, column=2)
        self.output = CTkTextbox(
            self.tab.tab("Шифр цезаря"),
            height=100
        )
        self.output.grid(row=1, column=2)

        #working button for Cezar enocode
        self.encodeButton = CTkButton(
            self.tab.tab("Шифр цезаря"),
            text="Зашифровать",
            height=30,
            command=self.startCezarEncode
        )
        self.encodeButton.grid(row=4, column=0, pady=30, padx=15)
        self.decodeButton = CTkButton(
            self.tab.tab("Шифр цезаря"),
            text="Расшифровать",
            height=30,
            command=self.startCezarDecode
        )
        self.decodeButton.grid(row=4, column=2, pady=30, padx=15)
        self.copyButton = CTkButton(
            self.tab.tab("Шифр цезаря"),
            text="Скопировать рузультат",
            height=30,
            command=lambda: copyResault(self.output.get(0.1, "end")),
            width=50
        )
        self.copyButton.grid(row=5, column=2)
        self.pasteButton = CTkButton(
            self.tab.tab("Шифр цезаря"),
            text="Вставить текст",
            height=30,
            command= self.getCopyed,
            width=50
        )
        self.pasteButton.grid(row=5, column=0)




    def change_appearance_mode_event(self, new_appearance_mode: str):
        if new_appearance_mode == "Светлая":
            set_appearance_mode('light')

        elif new_appearance_mode == "Тёмная":
            set_appearance_mode('dark')
        else:
            set_appearance_mode('system')

    def startCezarEncode(self):
        self.inputedText = self.input.get(0.1, "end")

        try:
            self.key = int(self.inputKey.get())
            self.lang = self.language.get()
            self.resault = cezar_encode(self.inputedText, self.lang, self.key)

            self.output.delete(0.1, "end")
            self.output.insert(0.1, self.resault)
        except ValueError:
            self.output.delete(0.1, "end")
            self.output.insert(0.1, "Ключ введён не правильно")

    def startCezarDecode(self):
        self.inputedText = self.input.get(0.1, "end")

        try:
            self.key = int(self.inputKey.get())
            self.lang = self.language.get()
            self.resault = cezar_decode(self.inputedText, self.lang, self.key)

            self.output.delete(0.1, "end")
            self.output.insert(0.1, self.resault)
        except ValueError:
            self.output.delete(0.1, "end")
            self.output.insert(0.1, "Ключ введён не правильно")

    def getCopyed(self):
        buffer = pasteCopyed()

        self.input.delete(0.1, "end")
        self.input.insert(0.1, buffer)