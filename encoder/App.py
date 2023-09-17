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

        """self.bgIMG = CTkImage(Image.open('images/bg1.png'), size=(800, 450))
        self.bglabel = CTkLabel(
            self,
            image=self.bgIMG,
            text=" "
        )
        self.bglabel.place(x=0, y=0)"""


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
        self.childrenWidgetHash()
        self.childrenWidgetHex()

        self.copyIMG = CTkImage(Image.open('images/copy.png'), size=(10, 10))
        self.pasteIMG = CTkImage(Image.open('images/paste.png'), size=(10, 10))


    def mainWidgets(self):
        self.tab = CTkTabview(
            self,
            width=600
            )
        self.tab.place(x=75, y=50)

        self.tab.add("Шифр цезаря")
        self.tab.add("Хекс-кодирование")
        self.tab.add("ASCII-кодирование")
        self.tab.add("Бинарное-кодирование")
        self.tab.add("Хеш-кодирование")
        self.tab.set("Хекс-кодирование")

        self.infoButton = CTkButton(
            self,
            command=self.dialog,
            width=20,
            height=20
        )
        self.infoButton.place(x=720, y=430)


    def childenWidgetsCezar(self):

        #Cezar enocode
        self.language = CTkSegmentedButton(
            self.tab.tab("Шифр цезаря"),
            values=["RU", "ENG"]
        )
        self.language.grid(row=1, column=1, padx=10)
        #input widgets for Cezar enocode
        self.inLabel = CTkLabel(
            self.tab.tab("Шифр цезаря"),
            text="Введите текст для шифрации",
            font=("Arial", 12)
            )
        self.inLabel.grid(row=0, column=0)
        self.input = CTkTextbox(
            self.tab.tab("Шифр цезаря"),
            height=70
        )
        self.input.grid(row=1, column=0)
        self.inputKey = CTkEntry(
            self.tab.tab("Шифр цезаря"),
            width=60,
            justify="center",
            placeholder_text="ключ"
        )
        self.inputKey.grid(row=4, column=1)

        #output widges for Cezar enocode
        self.outLabel = CTkLabel(
            self.tab.tab("Шифр цезаря"),
            text="Результат",
            font=("Arial", 12)
        )
        self.outLabel.grid(row=0, column=2)
        self.output = CTkTextbox(
            self.tab.tab("Шифр цезаря"),
            height=70
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
            text="Скопировать текст",
            height=30,
            command=lambda: copyResault(self.output.get(0.1, "end")),
            width=30
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

    def childrenWidgetHash(self):
        #hash input
        self.inputLabelHash = CTkLabel(
            self.tab.tab("Хеш-кодирование"),
            text="Введите текст для шифрации",
            font=("Arial", 12)
        )
        self.inputLabelHash.grid(row=0, column=0, padx=15)
        self.inputHash = CTkTextbox(
            self.tab.tab("Хеш-кодирование"),
            height=70
        )
        self.inputHash.grid(row=1, column=0)
        #hash output
        self.outputLabelHash = CTkLabel(
            self.tab.tab("Хеш-кодирование"),
            text="Резульатат",
            font=("Arial", 12),
            height=50
        )
        self.outputLabelHash.grid(row=0, column=2)
        self.outputHash = CTkTextbox(
            self.tab.tab("Хеш-кодирование"),
            height=70
        )
        self.outputHash.grid(row=1, column=2)
        #hash buttons
        self.hashEnocodeButton = CTkButton(
            self.tab.tab("Хеш-кодирование"),
            text="Зашифровать",
            command= self.startHashEncode
        )
        self.hashEnocodeButton.grid(row=3, column=0, pady=10)
        self.copyButtonHash = CTkButton(
            self.tab.tab("Хеш-кодирование"),
            text="Скопировать текст",
            height=30,
            command=lambda: copyResault(self.outputHash.get(0.1, "end")),
            width=50
        )
        self.copyButtonHash.grid(row=3, column=2)
        self.pasteButton = CTkButton(
            self.tab.tab("Хеш-кодирование"),
            text="Вставить текст",
            height=30,
            command=self.getCopyedHash,
            width=50
        )
        self.pasteButton.grid(row=4, column=2)
        #other
        self.changeTypeHashLabel = CTkLabel(
            self.tab.tab("Хеш-кодирование"),
            text="Выберите метод шифрования",
            font=("Arial", 12)
        )
        self.changeTypeHashLabel.grid(row=2, column=1, padx=5)
        self.changeTypeHash = CTkOptionMenu(
            self.tab.tab("Хеш-кодирование"),
            values=["md5", "sha3_224", "sha3_256", "sha384"]
        )
        self.changeTypeHash.grid(row=3, column=1, padx=5)

    def childrenWidgetHex(self):
        #input
        self.inputLabelHex = CTkLabel(
            self.tab.tab("Хекс-кодирование"),
            text="Введите текст для шифрации",
            font=("Arial", 12)
        )
        self.inputLabelHex.grid(row=0, column=0)
        self.inputHex = CTkTextbox(
            self.tab.tab("Хекс-кодирование"),
            height=70
        )
        self.inputHex.grid(row=1, column=0)
        #output
        self.outLabelHex = CTkLabel(
            self.tab.tab("Хекс-кодирование"),
            text="Результат",
            font=("Arial", 12)
        )
        self.outLabelHex.grid(row=0, column=2)
        self.outputHex = CTkTextbox(
            self.tab.tab("Хекс-кодирование"),
            height=70
        )
        self.outputHex.grid(row=1, column=2)


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

    def startHashEncode(self):
        res = hashEnocode(self.inputHash.get(0.1, "end"), self.changeTypeHash.get())

        self.outputHash.delete(0.1, "end")
        self.outputHash.insert(0.1, res)
    def startHashDecode(self):
        pass

    def getCopyedHash(self):
        buffer = pasteCopyed()

        self.inputHash.delete(0.1, "end")
        self.inputHash.insert(0.1, buffer)

    def getCopyed(self):
        buffer = pasteCopyed()

        self.input.delete(0.1, "end")
        self.input.insert(0.1, buffer)

    def dialog(self):
        self.text = ("1. Программа создана студентом Вологодского колледжа связи и информационных технологий.\n"
                     "2. Шифр цезаря - шифр основанный на сдвиге букв вправо(если ключ больше 0) или влево(если ключ меньше 0)\n"
                     "3. Хеширование является односторонним процессом, то есть хэш-коды не могут быть обратно преобразованы в исходные данные. Хэширование обычно используется для обеспечения безопасности данных, а не для их дешифровки.")
        self.info = CTkInputDialog(
            text=self.text,
            title="INFORMATION"
        )