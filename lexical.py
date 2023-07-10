#!/usr/bin/env python3

# palavras reservadas if, else, while, or, and, not
# identificadores apenas letras minusculas
# simbolos especiais (,),{,},-,+,*,^,/,=,==,<,>,"
# constantes inteiros

import sys

afd = {
	'1': {'final': False, '"': '55', 'a': '20,57', '{': '32', 'o': '17,57', '(': '28', '^': '42', 'w': '11,57', '/': '44', '+': '38', 'n': '24,57', '=': '46,48', '<': '51', '*': '40', '-': '36', 'i': '3,57', 'e': '6,57', '>': '53', '}': '34', 'r': '57', ')': '30', 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': '59', '1': '59', '2': '59', '3': '59', '4': '59', '5': '59', '6': '59', '7': '59', '8': '59', '9': '59', 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'55': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'20,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '21,57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'32': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'17,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '18,57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'28': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'42': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'11,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '12,57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'44': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'38': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'24,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '25,57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'46,48': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': '49', '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'51': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'40': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'36': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'3,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '4,57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'6,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '7,57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'53': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'21,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '22,57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'34': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'18,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'30': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'12,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '13,57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'25,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '26,57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'49': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'4,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'7,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '8,57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'22,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'13,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '14,57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'26,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'8,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '8,57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'14,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '15,57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'9,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'15,57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
	'59': {'final': True, '"': None, 'a': None, '{': None, 'o': None, '(': None, '^': None, 'w': None, '/': None, '+': None, 'n': None, '=': None, '<': None, '*': None, '-': None, 'i': None, 'e': None, '>': None, '}': None, 'r': None, ')': None, 'h': None, 'f': None, 'l': None, 'd': None, 't': None, 's': None, '0': '59', '1': '59', '2': '59', '3': '59', '4': '59', '5': '59', '6': '59', '7': '59', '8': '59', '9': '59', 'b': None, 'c': None, 'g': None, 'j': None, 'k': None, 'm': None, 'p': None, 'q': None, 'u': None, 'v': None, 'x': None, 'y': None, 'z': None},
	'57': {'final': True, '"': None, 'a': '57', '{': None, 'o': '57', '(': None, '^': None, 'w': '57', '/': None, '+': None, 'n': '57', '=': None, '<': None, '*': None, '-': None, 'i': '57', 'e': '57', '>': None, '}': None, 'r': '57', ')': None, 'h': '57', 'f': '57', 'l': '57', 'd': '57', 't': '57', 's': '57', '0': None, '1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, 'b': '57', 'c': '57', 'g': '57', 'j': '57', 'k': '57', 'm': '57', 'p': '57', 'q': '57', 'u': '57', 'v': '57', 'x': '57', 'y': '57', 'z': '57'},
}

estado = '1'  # Define o estado inicial do analisador léxico como '1'
token = ''  # Inicializa uma string vazia para armazenar o token atual

with open('program.txt') as programa, open('out_lexical.txt', 'w') as output:
    # Abre o arquivo 'program.txt' para leitura e o arquivo 'out_lexical.txt' para escrita como 'output'
    
    for nlinha, linha in enumerate(programa):
        # Itera sobre as linhas do arquivo 'programa.txt', atribuindo o número da linha a 'nlinha' e o conteúdo da linha a 'linha'
        
        for nchar, char in enumerate(linha):
            # Itera sobre os caracteres da linha atual, atribuindo o número do caractere a 'nchar' e o caractere a 'char'
            
            if char == ' ' or char == '\n' or char == '\t':
                # Verifica se o caractere é um espaço, uma quebra de linha ou uma tabulação
                
                if token == '':
                    continue
                    # Se o token estiver vazio, continua para o próximo caractere sem fazer nada
                
                elif afd[estado]['final']:
                    if estado in ['20,57', '17,57', '11,57', '24,57', '3,57', '6,57', '21,57', '12,57', '25,57', '7,57', '13,57', '8,57', '14,57']:
                        estado = '57'
                    output.write('{} {} {}\n'.format(nlinha, estado, token))
                    # Escreve no arquivo de saída o número da linha, o estado atual e o token atual
                    print('{} {} {}'.format(nlinha, estado, token))
                    # Imprime na tela o número da linha, o estado atual e o token atual
                    estado = '1'
                    token = ''
                    # Reseta o estado para '1' e o token para uma string vazia
                else:
                    sys.exit('erro (token indefinido) linha {} char {}'.format(nlinha, nchar))
                    # Encerra o programa com uma mensagem de erro se o token não estiver definido
                
            elif char not in afd[estado]:
                sys.exit('erro (caractere invalido) linha {} char {}'.format(nlinha, nchar))
                # Encerra o programa com uma mensagem de erro se o caractere não for válido para o estado atual
                
            elif not afd[estado][char]:
                sys.exit('erro (token invalido) linha {} char {}'.format(nlinha, nchar))
                # Encerra o programa com uma mensagem de erro se o token não for válido para o estado atual
                
            else:
                estado = afd[estado][char]
                token += char
                # Atualiza o estado para o próximo estado e adiciona o caractere ao token atual
                
    output.write('0 $ $\n')
    # Escreve uma linha indicando o fim da análise léxica no arquivo de saída