from customtkinter import *
from function import *
from PIL import Image
from datetime import *


class App(CTk):
    def __init__(self):
        super().__init__()
        self.title("Шифратор")
        self.geometry("800x450+300+200")
        set_appearance_mode("dark")
        set_default_color_theme("green")
        self.resizable(False, False)

        self.bgIMG = CTkImage(Image.open('images/bg.png'), size=(1000, 500))
        self.bglabel = CTkLabel(
            self,
            image=self.bgIMG,
            text=" "
        )
        self.bglabel.place(x=0, y=0)


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
        self.childrenWidgetASCII()
        self.childrenWidgetsBinary()



    def mainWidgets(self):

        bImg = CTkImage(Image.open('images/info.png'))

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

        self.infoButton = CTkButton(
            self,
            command=self.dialog,
            text='',
            width=20,
            height=20,
            image=bImg
        )
        self.infoButton.place(x=762, y=422)


    def childenWidgetsCezar(self):

        #Cezar enocode
        self.language = CTkSegmentedButton(
            self.tab.tab("Шифр цезаря"),
            values=["RU", "ENG"],

        )
        self.language.grid(row=1, column=1, padx=15)
        #input widgets for Cezar enocode
        self.inLabel = CTkLabel(
            self.tab.tab("Шифр цезаря"),
            text="Введите текст для шифрации",
            font=("Arial", 12)
            )
        self.inLabel.grid(row=0, column=0, padx=50)
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
        self.outLabel.grid(row=0, column=2, padx=105)
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
        self.inputLabelHash.grid(row=0, column=0)
        self.inputHash = CTkTextbox(
            self.tab.tab("Хеш-кодирование"),
            height=70
        )
        self.inputHash.grid(row=1, column=0, padx=(20,10))
        #hash output
        self.outputLabelHash = CTkLabel(
            self.tab.tab("Хеш-кодирование"),
            text="Резульатат",
            font=("Arial", 12),
            height=50
        )
        self.outputLabelHash.grid(row=0, column=2, padx=30)
        self.outputHash = CTkTextbox(
            self.tab.tab("Хеш-кодирование"),
            height=70
        )
        self.outputHash.grid(row=1, column=2, padx=(10, 20))
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

    def childrenWidgetASCII(self):
        #input widgets
        self.inputLabelASCII = CTkLabel(
            self.tab.tab('ASCII-кодирование'),
            text="Введите текст для шифрации",
            font=("Arial", 12)
        )
        self.inputLabelASCII.grid(row=0, column=0, padx=(45, 20))
        self.inputASCII = CTkTextbox(
            self.tab.tab('ASCII-кодирование'),
            height=70
        )
        self.inputASCII.grid(row=1,column=0, padx=(30, 15))

        #output widgets
        self.outputLabelASCII = CTkLabel(
            self.tab.tab('ASCII-кодирование'),
            text="Результат",
            font=("Arial", 12)
        )
        self.outputLabelASCII.grid(row=0, column=2, padx=(20, 45))
        self.outputASCII = CTkTextbox(
            self.tab.tab('ASCII-кодирование'),
            height=70
        )
        self.outputASCII.grid(row=1, column=2, padx=(15, 30))
        #BUTTONS
        self.ASCIIencodeButton = CTkButton(
            self.tab.tab('ASCII-кодирование'),
            text="Зашифровать",
            command=self.start_ASCII_encode
        )
        self.ASCIIencodeButton.grid(row=2, column=0, padx=(30, 10), pady=(20, 10))
        self.ASCIIdecodeButton = CTkButton(
            self.tab.tab('ASCII-кодирование'),
            text="Расшифровать",
            command=self.start_ASCII_decode
        )
        self.ASCIIdecodeButton.grid(row=2, column=2, padx=(10, 30), pady=(20, 10))
        self.copyButtonASCII = CTkButton(
            self.tab.tab('ASCII-кодирование'),
            text='Скопировать',
            command= lambda: copyResault(self.outputASCII.get(0.1, "end"))
        )
        self.copyButtonASCII.grid(row=2, column=1, pady=(20, 10))
        self.pasteButtonASCII = CTkButton(
            self.tab.tab('ASCII-кодирование'),
            text='Вставить',
            command= self.pasteASCII
        )
        self.pasteButtonASCII.grid(row=3, column=1, pady=(20, 10))

    def childrenWidgetsBinary(self):
        #input
        self.inputLabelBinary = CTkLabel(
            self.tab.tab('Бинарное-кодирование'),
            text="Введите текст для шифрации",
            font=("Arial", 12)
        )
        self.inputLabelBinary.grid(row=0, column=0, padx=(45, 20))
        self.inputBinary = CTkTextbox(
            self.tab.tab('Бинарное-кодирование'),
            height=70
        )
        self.inputBinary.grid(row=1, column=0, padx=(30, 15))

        # output widgets
        self.outputLabelBinary = CTkLabel(
            self.tab.tab('Бинарное-кодирование'),
            text="Результат",
            font=("Arial", 12)
        )
        self.outputLabelBinary.grid(row=0, column=2, padx=(20, 45))
        self.outputBinary = CTkTextbox(
            self.tab.tab('Бинарное-кодирование'),
            height=70
        )
        self.outputBinary.grid(row=1, column=2, padx=(15, 30))
        #buttons
        self.BinaryencodeButton = CTkButton(
            self.tab.tab('Бинарное-кодирование'),
            text="Зашифровать",
            command=self.start_Binary_encode
        )
        self.BinaryencodeButton.grid(row=2, column=0, padx=(30, 10), pady=(20, 10))
        self.BinarydecodeButton = CTkButton(
            self.tab.tab('Бинарное-кодирование'),
            text="Расшифровать",
            command=self.start_Binary_decode
        )
        self.BinarydecodeButton.grid(row=2, column=2, padx=(10, 30), pady=(20, 10))
        self.copyButtonBinary = CTkButton(
            self.tab.tab('Бинарное-кодирование'),
            text='Скопировать',
            command=lambda: copyResault(self.outputBinary.get(0.1, "end"))
        )
        self.copyButtonBinary.grid(row=2, column=1, pady=(20, 10))
        self.pasteButtonBinary = CTkButton(
            self.tab.tab('Бинарное-кодирование'),
            text='Вставить',
            command=self.pasteBinary
        )
        self.pasteButtonBinary.grid(row=3, column=1, pady=(20, 10))
        self.lang_bin = CTkSegmentedButton(
            self.tab.tab('Бинарное-кодирование'),
            values=['RU', 'ENG']
        )
        self.lang_bin.grid(row=1, column=1)




    def start_ASCII_encode(self):
        text = self.inputASCII.get(0.1, 'end')

        result = ASCII_encode(text)

        self.outputASCII.delete(0.1, 'end')
        self.outputASCII.insert(0.1, result)

    def start_ASCII_decode(self):
        text = self.inputASCII.get(0.1, 'end')

        result = ASCII_decode(text)

        self.outputASCII.delete(0.1, 'end')
        self.outputASCII.insert(0.1, result)


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
        self.inputHex.grid(row=1, column=0, pady=(0,30), padx=(20, 30))
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
        self.outputHex.grid(row=1, column=2, pady=(0,30), padx=(30, 20))
        #buttons
        self.hexEncodeButton = CTkButton(
            self.tab.tab("Хекс-кодирование"),
            text="Зашифровать",
            command=self.startHexEncode
        )
        self.hexEncodeButton.grid(row=2, column=0)
        self.hexDecodeButton = CTkButton(
            self.tab.tab("Хекс-кодирование"),
            text="Расшифровать",
            command=self.startHexDecode
        )
        self.hexDecodeButton.grid(row=2, column=2)
        self.hexCopyButton = CTkButton(
            self.tab.tab("Хекс-кодирование"),
            text="Скопировать текст",
            command=self.getCopyedHex
        )
        self.hexCopyButton.grid(row=2, column=1)
        self.hexPasteButton = CTkButton(
            self.tab.tab("Хекс-кодирование"),
            text="Вставить текст",
            command=self.pasteHex
        )
        self.hexPasteButton.grid(row=3, column=1, pady=20)

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

    def start_Binary_encode(self):
        text = self.inputBinary.get(0.1, 'end')

        language = self.lang_bin.get()

        if language.lower() == "ru":

            result = binary_encode_russian(text)

        elif language.lower() == 'eng':

            result = binary_encode_english(text)

        else:
            self.outputBinary.delete(0.1, 'end')
            self.outputBinary.insert(0.1, 'Не выбран язык!')
            return 0

        self.outputBinary.delete(0.1, 'end')
        self.outputBinary.insert(0.1, result)


    def start_Binary_decode(self):
        text_1 = self.inputBinary.get(0.1, 'end')

        text_1 = text_1.split('\n')

        text = ''

        for i in text_1:
            text += i

        language = self.lang_bin.get()

        if language.lower() == "ru":

            result = binary_decode_russian(text)

        elif language.lower() == 'eng':

            result = binary_decode_english(text)

        else:
            self.outputBinary.delete(0.1, 'end')
            self.outputBinary.insert(0.1, 'Не выбран язык!')
            return 0

        self.outputBinary.delete(0.1, 'end')
        self.outputBinary.insert(0.1, result)

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
                     "3. Хеш - это число, которое генерируется из текста с помощью алгоритма. Алгоритм работает так, что для каждого текста, генерируется уникальных хэш и восстановить текст из хеша, перехватив сообщение, практически невозможно.\n"
                     "4. Хекс кодирование - кодирование, при котором каждый символ переводится в своё шестнадцатиричное представление\n"
                     "5. Бинарное кодирование - кодирование, при котором каждый символ переводится в своё бинарное представление")
        self.info = CTkInputDialog(
            text=self.text,
            title="INFORMATION"
        )


    def startHexEncode(self):
        text = self.inputHex.get(0.1, "end")
        res = hex_encoder(text)
        self.outputHex.delete(0.1, "end")
        self.outputHex.insert(0.1, res)

    def startHexDecode(self):
        res = hex_decoder(self.inputHex.get(0.1, "end"))
        self.outputHex.delete(0.1, "end")
        self.outputHex.insert(0.1, res)
    def getCopyedHex(self):
        copyResault(self.outputHex.get(0.1, "end"))
    def pasteHex(self):
        res = pasteCopyed()
        self.inputHex.delete(0.1, "end")
        self.inputHex.insert(0.1, res)

    def pasteASCII(self):
        res = pasteCopyed()
        self.inputASCII.delete(0.1, "end")
        self.inputASCII.insert(0.1, res)

    def pasteBinary(self):

        res = pasteCopyed()
        self.inputBinary.delete(0.1, "end")
        self.inputBinary.insert(0.1, res)
