# -*- coding: utf-8 -*-
from enum import Enum
from intercom.traits.api_resource import Resource


class Article(Resource):
    pass

class Locale(Enum):
    ARABIC = "ar",
    BULGARIAN = "bg",
    BOSNIAN = "bs",
    CATALAN = "ca",
    CZECH = "cs",
    DANISH = "da",
    GERMAN = "de",
    DE_FORM = "de-form",
    GREEK = "el",
    ENGLISH = "en",
    SPANISH = "es",
    ESTONIAN = "et",
    FINNISH = "fi",
    FRENCH = "fr",
    HEBREW = "he",
    CROATIAN = "hr",
    HUNGARIAN = "hu",
    INDONESIAN = "id",
    ITALIAN = "it",
    JAPANESE = "ja",
    KOREAN = "ko",
    LITHUANIAN = "lt",
    LATVIAN = "lv",
    MONGOLIAN = "mn",
    NORWEGIAN = "nb",
    DUTCH = "nl",
    POLISH = "pl",
    PORTUGUESE_BRAZIL = "pt-BR",
    PORTUGUESE = "pt",
    ROMANIAN = "ro",
    RUSSIAN = "ru",
    SLOVENIAN = "sl",
    SERBIAN = "sr",
    SWEDISH = "sv",
    TURKISH = "tr",
    VIETNAMESE = "vi",
    CHINESE_S = "zh-CN",
    CHINESE_T = "zh-TW"
