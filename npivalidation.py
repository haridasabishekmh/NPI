def luhn_checksum(NPI_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(NPI_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

print('Valid') if luhn_checksum("808401940282308")==0 else print('Invalid')