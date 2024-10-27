class py_solution:
    
    def int_to_Roman(self, num):
        val = [

            1000, 900, 500, 400,

            100, 90, 50, 40,

            10, 9, 5, 4,

            1

            ]
        syb = [

            "M", "CM", "D", "CD",

            "C", "XC", "L", "XL",

            "X", "IX", "V", "IV",

            "I"

            ]
        roman_num = ' '
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num = roman_num + syb[i]
                num = num - val[i]
            i = i+1
        return roman_num
    
while True :
    n = int(input("Enter a number you want to cojnvert into Roman Number:"))
    print(py_solution().int_to_Roman(n))
    
    op = input("Do you want to conver more? Y/N :")
    if op == "N" or op == "n":
        break    
                