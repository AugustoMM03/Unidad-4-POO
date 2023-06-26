class Imaginario(object):

    __operando1 : float
    __operando2 : float

    def __init__(self, num1, num2):
        self.__operando1 = num1
        self.__operando2 = num2 

    def parseNumero(self, numero):
        numero = str(numero)
        numero = numero.replace(' ', '')
        if 'i' in numero:
            if '+' in numero:
                partes = numero.split('+')
                real = float(partes[0]) if partes[0] else 0.0
                imag = float(partes[1].replace('i', ''))
            elif '-' in numero:
                partes = numero.split('-')
                real = float(partes[0]) if partes[0] else 0.0
                imag = float(partes[1].replace('i', ''))
            else:
                real = 0.0
                imag = float(numero.replace('i', ''))
        else:
            real = float(numero)
            imag = 0.0
        return real, imag
    
    def construirComplejo(self, real, imag):
        if float(imag) >=0:
            resultado = f"{float(real)} + {float(imag)}i"
        else:
            resultado = f"{float(real)} + {abs(float(imag))}i"
        return resultado


    def imaginarioSuma(self):

        op1real, op1imag = self.parseNumero(self.__operando1)
        op2real,op2imag = self.parseNumero(self.__operando2)
        resultadoReal = op1real + op2real
        resultadoImag = op1imag + op2imag
        resultado = self.construirComplejo(resultadoReal,resultadoImag)
        return resultado

    def imaginarioResta(self):

        op1real, op1imag = self.parseNumero(self.__operando1)
        op2real,op2imag = self.parseNumero(self.__operando2)
        resultadoReal = float(op1real) - float(op2real)
        resultadoImag = float(op1imag) - float(op2imag)
        resultado = self.construirComplejo(resultadoReal,resultadoImag)
        return resultado


    def imaginarioMultiplicacion(self):

        op1real, op1imag = self.parseNumero(self.__operando1)
        op2real,op2imag = self.parseNumero(self.__operando2)
        resultadoReal = float(op1real) * float(op2real) - float(op1imag) * float(op2imag)
        resultadoImag = float(op1real) *float(op2imag) + float(op1imag) * float(op2real)
        resultado = self.construirComplejo(resultadoReal,resultadoImag)
        return resultado

    def imaginarioDivision(self):
        
        op1real, op1imag = self.parseNumero(self.__operando1)
        op2real,op2imag = self.parseNumero(self.__operando2)
        denominador = float(op2real)**2 + float(op2imag)**2 
        resultadoReal = (float(op1real) * float(op2real) + float(op1imag) * float(op2imag)) / float(denominador)
        resultadoImag = (float(op1imag) * float(op2real) - float(op1real) * float(op2imag)) / float(denominador)
        resultado = self.construirComplejo(resultadoReal,resultadoImag)
        return resultado
    


