#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Cryptography Advanced Tool - продвинутый инструмент для шифрования и криптографии на Python
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
import sys
from modules.caesar import encode_caesar, decode_caesar

logo = '''
   _________  ______
  / ____/   |/_  __/     Cryptography
 / /   / /| | / /        Advanced
/ /___/ ___ |/ /         Tool
\\____/_/  |_/_/
'''
help_docs = '''
Справка по CAT:

  --help/-h    Показать справку

  Шифр Цезаря:
  	--encode-caesar    Кодирование шифром цезаря: --encode-caesar <текст> <длина-шага> <язык (ru/en)>
  	--decode-caesar    Декодирование шифром цезаря: --decode-caesar <текст> <длина-шага> <язык (ru/en)>

  Хеширование:
    Доступные алгоритмы: md5, sha1, sha256, sha224, sha384, sha3_224, sha3_256, sha3_384, sha3_512, sha512, shake_128, shake_256
'''


def main():
	print(logo)
	if len(sys.argv) > 1:
		if sys.argv[1] == '--help' or sys.argv[1] == '-h':
			print(help_docs)
		elif sys.argv[1] == '--encode-caesar':
			try:
				result = encode_caesar(sys.argv[2], int(sys.argv[3]), sys.argv[4])
			except IndexError:
				print('[!] Ошибка: Вы ввели не все параметры. Для просмотра справки запустите CAT с флагом --help')
			except ValueError:
				print('[!] Ошибка: Вы ввели не числовой параметр шагов/дистанции для шифрования. Для просмотра справки запустите CAT с флагом --help')
		elif sys.argv[1]
