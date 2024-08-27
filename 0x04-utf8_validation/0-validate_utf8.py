#!/usr/bin/python3
'''Validating UTF-8 Format'''


def validUTF8(data):
    '''checks if the data represents a valid utf format'''
    bytes_list = [format(el, '08b')[-8:] for el in data]
    idx = 0
    while idx < len(bytes_list):
        n0_bytes = count_leading_ones(bytes_list[idx])
        if n0_bytes > 0:
            if n0_bytes == 1 or n0_bytes > 4:
                return False
            start = idx + 1
            end = idx + n0_bytes
            for i in range(start, end):
                if i >= len(bytes_list) or not bytes_list[i].startswith('10'):
                    return False
                idx += 1
        idx += 1

    return True


def count_leading_ones(byt: str):
    '''counts the number of "1" digits at the start of the string'''
    count = 0

    for bit in byt:
        if bit == '1':
            count += 1
        else:
            break

    return count
