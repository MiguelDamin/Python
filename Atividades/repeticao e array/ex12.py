'''Um sistema gerador de boletin escolar que recebe 4 notas do alunos e devolve se ele foi aprovado
ou reprovado. utilize funções para cada operação.
extra: Utilizando python, gere um pdf com as notas do aluno e a situação dele.'''
from fpdf import FPDF

def gerar_pdf(notas, media_final, situacao):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Boletim Escolar", ln=True, align='C')
    pdf.ln(10)

    for i, nota in enumerate(notas):
        pdf.cell(200, 10, txt=f"Nota {i+1}: {nota}", ln=True)

    pdf.ln(5)
    pdf.cell(200, 10, txt=f"Média Final: {media_final:.2f}", ln=True)
    pdf.cell(200, 10, txt=f"Situação: {situacao}", ln=True)

    pdf.output("/home/miguel/Documentos/Python/boletim.pdf")
    print("PDF salvo como boletim.pdf")
    


notas = []
notafn = float
def media(notas):
    notafn = sum(notas) / 4
    return notafn

for i in range(4):
    notas.append(float(input(f"Nota {i}: ")))



notafn = media(notas)
if notafn >= 6:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(situacao)
gerar_pdf(notas, notafn, situacao)



#INACABADO, FINAL DE SEMANA -- TERMINAR.





