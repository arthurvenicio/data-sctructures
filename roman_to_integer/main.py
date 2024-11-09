class Solution:
    def romanToInt(self, s: str) -> int:
        # Dicionário que mapeia cada símbolo romano para seu valor numérico.
        roman_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        # Variável que armazenará o valor final do número.
        final_number = 0
    
        # Loop que percorre pares de caracteres adjacentes em 's'.  O zip(s, s[1:]) permite comparar cada símbolo com o próximo. 
        # Ex: em XII, vai ficar (X,I) (I, I) nessa conta o ultimo caractere não é contabilizado, devemos somar ele ao número final.
        # E por que somar e não subtrair, pois ele está mais a direita possível.
        for x, y in zip(s, s[1:]):
            # Se o valor do símbolo atual (x) for menor que o valor do próximo (y),
            # subtrai o valor de 'x' do total, pois indica uma combinação como "IV" ou "IX".
            if roman_map[x] < roman_map[y]:
                final_number -= roman_map[x]
            # Caso contrário, adiciona o valor de 'x' ao total.
            else:
                final_number += roman_map[x]
        
        # Adiciona o valor do último símbolo em 's' ao total,
        # pois ele não é incluído no loop.
        return final_number + roman_map[s[-1]]
