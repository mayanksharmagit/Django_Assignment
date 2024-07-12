def number_to_words(number):
    if number == 0:
        return "Zero"

    units = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
    thousands = ["", "Thousand", "Lakh", "Crore"]

    def convert_chunk(number):
        if number < 10:
            return units[number]
        elif number < 20:
            return teens[number - 11]
        elif number < 100:
            return tens[number // 10 - 1] + (" " + units[number % 10] if number % 10 != 0 else "")
        else:
            return units[number // 100] + " Hundred" + (" " + convert_chunk(number % 100) if number % 100 != 0 else "")

    def split_number(number):
        number_str = str(number)
        length = len(number_str)
        
        if length <= 3:
            return [number]
        elif length <= 5:
            return [int(number_str[-3:]), int(number_str[:-3])]
        elif length <= 7:
            return [int(number_str[-3:]), int(number_str[-5:-3]), int(number_str[:-5])]
        elif length <= 9:
            return [int(number_str[-3:]), int(number_str[-5:-3]), int(number_str[-7:-5]), int(number_str[:-7])]
        else:
            return [int(number_str[-3:]), int(number_str[-5:-3]), int(number_str[-7:-5]), int(number_str[-9:-7]), int(number_str[:-9])]

    number_parts = split_number(number)
    words = []

    for i, part in enumerate(number_parts):
        if part > 0:
            words.append(convert_chunk(part))
            if i > 0:
                words.append(thousands[i])
    
    return ' '.join(reversed(words)).strip()

