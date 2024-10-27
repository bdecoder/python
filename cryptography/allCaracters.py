import string
import random

# Caractères ASCII
ascii_characters = list(string.ascii_letters + string.digits + string.punctuation + ' ')

# Caractères accentués et symboles divers
additional_characters = [
    'à', 'é', 'è', 'ù', 'ç', 'ô', 'â', 'î', 'û', 'ä', 'ë', 'ï', 'ö', 'ü', 'ÿ',
    'Á', 'É', 'Í', 'Ó', 'Ú', 'Ñ', 'Ü', 'ß', 'à', 'è', 'ì', 'ò', 'ù', 'À', 'È',
    'Ì', 'Ò', 'Ù', 'Œ', 'Æ', 'æ', 'œ'
]

# Lettres cyrilliques
cyrillic_characters = [
    'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
    'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь',
    'Э', 'Ю', 'Я', 'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к',
    'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ',
    'ъ', 'ы', 'ь', 'э', 'ю', 'я'
]

# Lettres grecques
greek_characters = [
    'Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο',
    'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω', 'α', 'β', 'γ', 'δ', 'ε', 'ζ',
    'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ',
    'χ', 'ψ', 'ω'
]

# Caractères arabes
arabic_characters = [
    'ا', 'ب', 'ت', 'ث', 'ج', 'ح', 'خ', 'د', 'ذ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض',
    'ط', 'ظ', 'ع', 'غ', 'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'هـ', 'و', 'ي', 'ى', 'أ',
    'إ', 'آ', 'ة', 'ئ', 'ؤ', 'ر', 'ز', 'س', 'ش', 'ص', 'ض', 'ط', 'ظ', 'ع', 'غ',
    'ف', 'ق', 'ك', 'ل', 'م', 'ن', 'هـ', 'و', 'ي'
]

# Caractères chinois
chinese_characters = [
    '我', '你', '是', '的', '了', '在', '和', '有', '人', '他', '她', '它', '们',
    '这', '那', '一个', '会', '来', '去', '看', '说', '做', '吃', '喝', '玩',
    '学', '习', '中', '国', '汉', '字', '简', '体', '繁', '体'
]

# Caractères japonais (Hiragana et Katakana)
japanese_characters = [
    # Hiragana
    'あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す',
    'せ', 'そ', 'た', 'ち', 'つ', 'て', 'と', 'な', 'に', 'ぬ', 'ね', 'の', 'は',
    'ひ', 'ふ', 'へ', 'ほ', 'ま', 'み', 'む', 'め', 'も', 'や', 'ゆ', 'よ', 'ら',
    'り', 'る', 'れ', 'ろ', 'わ', 'を', 'ん',
    # Katakana
    'ア', 'イ', 'ウ', 'エ', 'オ', 'カ', 'キ', 'ク', 'ケ', 'コ', 'サ', 'シ', 'ス',
    'セ', 'ソ', 'タ', 'チ', 'ツ', 'テ', 'ト', 'ナ', 'ニ', 'ヌ', 'ネ', 'ノ', 'ハ',
    'ヒ', 'フ', 'ヘ', 'ホ', 'マ', 'ミ', 'ム', 'メ', 'モ', 'ヤ', 'ユ', 'ヨ', 'ラ',
    'リ', 'ル', 'レ', 'ロ', 'ワ', 'ヲ', 'ン'
]

# Caractères coréens
korean_characters = [
    '가', '나', '다', '라', '마', '바', '사', '아', '자', '차', '카', '타', '파',
    '하', 'ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ',
    'ㅍ', 'ㅎ', 'ㅏ', 'ㅓ', 'ㅗ', 'ㅜ', 'ㅡ', 'ㅣ'
]

# Tous les caractères combinés
all_characters = (
    ascii_characters +
    additional_characters +
    cyrillic_characters +
    greek_characters +
    arabic_characters +
    chinese_characters +
    japanese_characters +
    korean_characters
)
for i in range (90):
    random.shuffle(all_characters)
# Afficher tous les caractères
print(all_characters)