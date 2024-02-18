#!/usr/bin/env python3

# Sprawdzić, czy podany wyraz jest palindromem

is_palindrom = lambda txt: txt == txt[::-1]

print(is_palindrom(input("> ")))
