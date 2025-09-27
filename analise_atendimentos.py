#Importação da biblioteca panda
import pandas as pd

#Função para importar e ler o arquivo CSV retornando um DataFrame
caminho_csv = r"C:\\Users\\henri\\OneDrive\Ambiente de Trabalho\\teste-tecnico-henrique\data\\atendimentos_feira.csv"
df = pd.read_csv(caminho_csv)

# Função para a Taxa de Conversão

try:
    total_atendimentos = len(df)
    total_convertidos = df['converteu_venda'].value_counts()
    conversao = total_convertidos / total_atendimentos * 100
    print (conversao)

except: 
    print('Erro ao gerar o Relatório')

# Função para o Tipo de Interesse
try:
    interesse = df["tipo_interesse"].value_counts()
    print(interesse)
except:
    print('Erro ao gerar o Relatório')

# Função para o Horário de Pico

try: 
    def periodo(hora):
        if hora in range(6, 12):
            return "Manhã"
        elif hora in range(12,18):
            return "Tarde"
        else:
            return "Noite"
    df["data_hora"] = pd.to_datetime(df["data_hora"], errors="coerce")
    df["periodo"] = df["data_hora"].dt.hour.apply(periodo)
    contagem_periodos = df["periodo"].value_counts()
    horario_pico = contagem_periodos.idxmax()
    print(horario_pico)
except:
    print('Erro ao gerar o Relatório')

#Função para o Dia Mais Movimentado

try:
    df["dia"] = df["data_hora"].dt.date
    contagem_dias = df["dia"].value_counts()
    dia_pico = contagem_dias.idxmax()
    print(dia_pico)
except: 
    print('Erro ao gerar o Relatório')

# Função para o Top 10 Palavras nas mensagens

try:
    mensagens = df["mensagem"].dropna().astype(str)
    texto = " ".join(mensagens).lower()
    stopwords = {
        "a","o","os","as","de","da","do","das","dos","e","é","em","para","um","uma",
        "com","na","no","nas","nos","que","se","por","ao","aos","à","às","ou","ser",
        "tem","ter","já","mais","menos","sim","não","sobre"
    }
    palavra = texto.split()
    frequencia = {}
    for p in palavra:
        if p not in stopwords and len(p) > 2:
            frequencia[p] = frequencia.get(p, 0) + 1
    top_10 = sorted(frequencia.items(), key=lambda x: x[1], reverse=True)[:10]
    print("Top 10 palavras mais comuns:")
    for palavra, qtd in top_10:
        print(f"{palavra}: {qtd}")
except:
    print('Erro ao gerar o Relatório')


#Função para gerar relatório em arquivo txt

try: 
    with open('relatorio_analise.txt','w', encoding = 'utf-8') as arquivo:
        arquivo.write("Relatório:\n")
 
        arquivo.write("Taxa de Conversão:\n")
        arquivo.write(str(conversao) + "\n\n")

        arquivo.write("Distribuição por Tipo de Interesse:\n")
        arquivo.write(str(interesse) + "\n\n")

        arquivo.write("Horário de Pico:\n")
        arquivo.write(str(horario_pico) + "\n\n")

        arquivo.write("Dia Mais Movimentado:\n")
        arquivo.write(str(dia_pico) + "\n\n")

        arquivo.write("Top 10 Palavras mais comuns:\n")
        for palavra, qtd in top_10:
            arquivo.write(f"{palavra}: {qtd}\n")
except:
    ('Erro ao gerar o Relatório')