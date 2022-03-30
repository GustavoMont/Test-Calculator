from email import message


class Calculadora:
    def Soma(self, num1, num2):
        return num1+num2
    def Subtracao(self, num1, num2):
        return num1-num2
    def Multiplicacao(self, num1, num2):
        return num1*num2
    def Divisao(self,num1, num2):
        if (num2 == 0):
            raise ValueError("Impossível dividir por 0")

        return num1/num2
    def Fatorial (self, num):
        if (num < 0):
            raise ValueError("Impossível Fatorial de Negativos")
        elif (num == 0):
            return 1    
        elif (num == 1):
            return 1
        else:
            return num * self.Fatorial(num - 1)
    def Potencia(self, base, potencia):
        resultado = base
        if (potencia < 0):
            raise ValueError("Potencia negativa")
        elif (potencia == 0) :
            return 1
        else:
            for i in range(1, potencia):
                resultado = resultado * base
            return resultado