#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""caesar.py - алгоритм шифрования цезаря
Cryptography Advanced Tool - продвинутый инструмент для шифрования и криптографии на Python
Copyright (C) 2023  Okulus Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
from string import ascii_lowercase

alphabet_ru = u'абвгдеёжзийклмнопрстуфхцчшщьъэюя'
alphabet_en = u'{}'.format(ascii_lowercase)


def encode_caesar(text: str, step: int, lang: str) -> str:
	"""Шифрование текста шифром Цезаря

	Аргументы:
	 + text: str - исходный текст
	 + step: int - размер шага-дистанции
	 + lang: str - тип алфавита (ru, en)

	Возвращает: str (зашифрованный текст)"""
	if lang.lower() == 'ru':
		return text.translate(
			str.maketrans(alphabet_ru, alphabet_ru[step:] + alphabet_ru[:step]))
	else:
		return text.translate(
			str.maketrans(alphabet_en, alphabet_en[step:] + alphabet_en[:step]))


def decode_caesar(text: str, step: int, lang: str):
	"""Дешифрование текста шифром Цезаря

	Аргументы:
	 + text: str - исходный текст
	 + step: int - размер шага-дистанции
	 + lang: str - тип алфавита (ru, en)

	Возвращает: str (расшифрованный текст)"""
	if lang.lower() == 'ru':
		return text.translate(
			str.maketrans(alphabet_ru[step:] + alphabet_ru[:step], alphabet_ru))
	else:
		return text.translate(
			str.maketrans(alphabet_en[step:] + alphabet_en[:step], alphabet_en))
