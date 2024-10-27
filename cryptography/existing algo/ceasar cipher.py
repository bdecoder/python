def encode(mess, number):
    encodedMessage = []
    for chars in mess:
        try:
            caracterPosition = caracters.index(chars)
            caracterAfterKey = caracterPosition + number
            caracterSanitarized = caracterAfterKey % len(caracters)
            encodedMessage.append(caracters[caracterSanitarized])
        except ValueError:
            print(f"Le caractère '{chars}' n'est pas autorisé.")
    finalMessage = ''.join(encodedMessage)
    print(f"le message chiffré est: {finalMessage}")
    print(f"Il à été chiffré avec la clef {number}")

def decode(mess, number):
    encodedMessage = []
    number = number * (-1)
    for chars in mess:
        try:
            caracterPosition = caracters.index(chars)
            caracterAfterKey = caracterPosition + number
            caracterSanitarized = caracterAfterKey % len(caracters)
            encodedMessage.append(caracters[caracterSanitarized])
        except ValueError:
            print(f"Le caractère '{chars}' n'est pas autorisé.")
    finalMessage = ''.join(encodedMessage)
    print(f"le message déchiffré est: {finalMessage}")

def messageInput():
    message = input("entrez votre message: ")
    message = list(message)
    return message

def keyInput():
    key = input("veuillez entrer le nombre qui servira de clef: ")
    try:
        key = int(key)
    except ValueError:
        print(f"La clef choisie ({key}) n'est pas correct. Veuillez entrer un nombre entier.")
        exit(2)
    return key

def mode():
    print('Deux modes sont disponibles: le mode encoder (1) et le mode décoder (2)')
    choice = input('Veuillez entrer le mode choisi: ')
    try:
        choice = int(choice)
    except ValueError:
        print(f"Le mode choisi ({choice}) n'est pas correct. Veuillez entrer 1 ou 2.")
        exit(2)

    if choice == 1:
        encode(messageInput(), keyInput())
    elif choice == 2:
        decode(messageInput(), keyInput())
    else:
        print(f"Le mode choisi ({choice}) n'est pas correct. Veuillez entrer 1 ou 2")
        exit(2)

caracters = ['ろ', '会', 'م', 'Е', 'г', 'ر', 'ل', 'Æ', 'Α', 'u', '是', 'ل', 'β', '学', 'ㅅ', 'R', 'm', 'エ', 'Π', 'と',
             'à', 'З', '^', 'h', '那', 'p', '!', 'タ', '4', 'フ', '0', 'ô', 'ㄱ', 'd', 'T', '简', '_', 'م', 'ウ', 'ا',
             'そ', 'ز', 'в', 'g', 'W', 'е', 'ò', 'И', 'ظ', '/', 'ы', 'G', 'ㅗ', 'ㄷ', 'ف', '마', 'を', 'Φ', 'В', 'خ',
             'ㅏ', 'Ρ', 'ئ', 'や', '[', '}', 'の', 'Δ', 'я', 'Ш', 'É', 'Μ', '차', 'Б', 'ж', 'ض', 'δ', 'τ', '가', 'هـ',
             'ï', '看', 'χ', 'L', 'ゆ', 'v', 'ヒ', 'む', 'ü', 'ク', 'м', 'マ', 'ك', 'ㅁ', '5', 'イ', 'セ', '|', 'V', 'Χ',
             'お', '了', 's', ':', 'ネ', 'Y', 'Λ', 'w', 'ع', 'ق', 'ん', '它', 'c', 'ワ', 'み', '"', 'ز', 'Ф', 'ش', 'ス',
             'ν', 'ت', 'ヲ', 'у', 'ㅡ', 'Ì', 'ف', 'チ', 'Ё', 'Р', 'も', '바', 'j', 'Á', 'Ц', '`', 'ㅋ', '-', 'K', 'ら',
             '这', '@', 'Ñ', 'き', 'و', 'к', 'i', 'つ', 'Γ', 'Ι', ',', 'Ù', '%', 'Ы', 'ÿ', 'す', 'é', 'р', 'غ', 'ㅊ',
             'い', 'и', 'Q', 'ヤ', 'モ', 'l', 'わ', '国', '玩', 'Ь', 'ニ', 'コ', 'γ', ' ', 'ن', '카', 'ね', 'ц', '.', 'ε',
             '$', 'ζ', 'ß', ')', 'θ', 'أ', 'н', '다', '繁', 'Й', 'Τ', '?', 'f', 'д', 'ù', 'ب', 'Í', '>', '有', 'ك', 'Т',
             'リ', 'هـ', 'ι', 'ㄴ', 'E', 'а', 'ù', 'إ', 'り', 'б', 'ш', 'Κ', '타', 'H', '2', 'ю', 'κ', '7', 'Ξ', 'ア',
             'ω', 'る', 'P', 'O', '파', 'è', 'ㄹ', '+', '字', 'Х', ';', 'カ', 'ي', 'σ', 'サ', 'О', 'Ω', '她', 'ج', 'せ',
             'y', 'Г', 'ツ', 'Я', 'К', '\\', 'Л', 'Z', 'л', 'з', 'か', '做', 'e', 'ي', 'æ', 'あ', 'ヨ', 'à', '(', 'B',
             'Θ', 'r', 'Щ', 'Ю', 'ë', '9', 'φ', 'آ', '在', 'η', 'う', 'ё', 'ヘ', 'ذ', 'ㅓ', 'Β', 'U', 'э', 'щ', 'С', 'I',
             'に', '来', 'È', '人', 'ま', 'ユ', 'へ', 'ふ', 'Ε', 'b', '~', 'Ν', 'ひ', 'キ', 'N', 'ع', 'À', 'け', 'Ú', 'F',
             'ص', 'ㅎ', 'ソ', 'غ', 'ト', 'シ', 'è', 'â', '和', 'く', '中', 'û', 'Ó', 'υ', 'Ч', 'ο', 'こ', '喝', 'ن', 'レ',
             'ㅇ', 't', 'Ψ', 'س', 'د', 'Ο', '하', 'ㅣ', 'ほ', 'Υ', '6', 'ミ', 'Ζ', '汉', 'Ü', '나', 'M', '1', 'ى', 'ヌ',
             'な', 'ㅂ', '的', 'ハ', 'ф', '他', 'т', '体', 'ح', 'ض', 'π', '说', 'C', 'ラ', 'Ъ', 'ö', 'œ', '사', 'Œ', '习',
             'は', 'q', 'D', 'ン', 'ロ', 'î', 'ь', 'A', 'μ', 'ط', 'ㅍ', 'Д', 'ظ', '&', 'ç', '#', 'て', 'テ', 'ъ', '体',
             'و', '去', 'ナ', 'У', '{', 'ش', 'メ', 'ؤ', 'ص', 'п', 'ル', 'ホ', 'й', 'ち', 'z', 'ξ', 'さ', 'k', 'S', 'ث',
             '라', 'ق', 'ㅈ', 'オ', 'α', 'Ж', 'Σ', '8', 'с', 'れ', 'ム', 'ì', 'ぬ', 'ر', 'ㅌ', '아', "'", 'А', '<', 'x',
             'ة', 'М', 'ч', 'o', '자', 'П', '*', 'n', '=', 'え', 'a', 'ㅜ', 'ψ', 'X', 'λ', ']', 'Η', '3', 'た', '我', 'ط',
             '一个', 'ケ', 'х', 'Э', '们', '吃', 'Ò', 'よ', 'ノ', '你', 'س', 'о', 'ä', 'Н', 'J', 'し', 'ρ', 'め']

mode()