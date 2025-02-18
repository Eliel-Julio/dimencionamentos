# Def de funções
def Mpa_to_Kpsi(Mpa):
    return Mpa/6.895

def calculo(Fat_seg,Sut,Se_,Tm,Ta,Mm,Ma,Kfs,Kf):
    """
    Calculo do diametro do eixo segundo o livro 
    "Elementos de máquinas - Shigley 10° Ed"
    Fat_seg: fator de segurança do projeto
    Sut:
    Se_:
    Tm:
    Ta:
    Kfs:
    """
    from math import pi
    S1=16*Fat_seg/pi
    S2=(((3*((Kfs*Tm)**2))+(4*((Kf*Mm)**2)))**0.5)/Sut
    S3=(((3*((Kfs*Ta)**2))+(4*((Kf*Ma)**2)))**0.5)/Se_
    return (S1*(S2+S3))**(1/3)
def polinomio(x,exp,alfa):
    if len(exp)==len(alfa):
        valor=[]
        for i in exp:
            valor.append(x**i)
        y=0
        for i in range(0,len(exp)):
            val=valor[i]*alfa[i]
            y+=val
    return y
def modf(temperatura, sut, acabamento_superficial="retificado", estado_de_tensao="flexao",d_incial=26.895,confiabilidade=99):
    """define fatores modificadores do limite de resistência à fadiga pag 289
    
    
    """
    ab={"retificado":[1.58,0.085],
        "usinado_lamFrio":[4.51,0.265],
        "lamQuente":[57.7,0.718],
        "forjado":[272,0.995]}
    c={"flexao":1, "axial":0.85,"torcao":0.59}
    if estado_de_tensao=="axial":
        B=1
    else:
        B=1.24/(d_incial**0.107)
    conf={"confiabilidade":[50,90,95,99,99.9,99.99,99.999,99.9999],
                      "Ke":[1,0.897,0.868,0.814,0.753,0.702,0.659,0.620]}
    if temperatura=="false":
        D=1
    else:
        D=polinomio(((temperatura*1.8)+32)/32,
                                [0,1,2,3,4],
                                [0.974,
                                 0.432/10**3,
                                 -0.115/10**5,
                                 0.104/10**8,
                                 -0.595/10**12]),
    
    fatores_modf={"A":ab[acabamento_superficial][0]/((sut/10**6)**ab[acabamento_superficial][1]),
                  "B":B,
                  "C":c[estado_de_tensao],
                  "D":D,
                  "E":conf["Ke"][conf["confiabilidade"].index(confiabilidade)],
                  "F":1}
    return fatores_modf
def prod(dic):
    """
    multiplica os valores de um dicionario
    dic: Dicionario com os valores a ser multiplicado
    """
    prod=1
    for i, valor in dic.items():
        prod*=valor
    return prod
def qq(r,sut,estado_de_tensao="torcao"):
    av={"flexao_axial":[0.246,-3.08/(10**3),1.51/(10**5),-2.67/(10**8)],
              "torcao":[0.190,-2.51/(10**3),1.35/(10**5),-2.67/(10**8)]}
    a=(polinomio(sut,[0,1,2,3],av[estado_de_tensao]))**0.5
    return a#(1/(1+(a/(r**0.5))))