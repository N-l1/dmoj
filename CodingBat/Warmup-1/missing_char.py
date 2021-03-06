"""
Warmup-1 > missing_char
Find this problem at:
https://codingbat.com/prob/p149524
"""


def missing_char(str, n):
    return str[:n] + str[n+1:]
