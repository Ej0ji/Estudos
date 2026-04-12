# Lista com os nomes já em ordem alfabética
nomesGenericos = [
    "Adriana", "Alan", "Alberto", "Aline", "Amanda", "Ana", "Anderson", "Andre",
    "Angela", "Antonio", "Arthur", "Beatriz", "Brenda", "Bruno", "Camila", "Carlos",
    "Carolina", "Catarina", "Clara", "Claudio", "Cristina", "Daniel", "Daniele", "David",
    "Debora", "Diego", "Douglas", "Eduarda", "Eduardo", "Elaine", "Eliana", "Emerson",
    "Enzo", "Erica", "Fabiana", "Fabio", "Felipe", "Fernanda", "Fernando", "Flavia",
    "Francisco", "Gabriel", "Gabriela", "Gisele", "Gustavo", "Helena", "Henrique", "Hugo",
    "Igor", "Isabela", "Isabelly", "Ivan", "Jaqueline", "Jean", "Jessica", "Joao",
    "Jonas", "Jonathan", "Jorge", "Jose", "Julia", "Juliana", "Julio", "Karen",
    "Karina", "Katia", "Kevin", "Lais", "Larissa", "Laura", "Leandro", "Leonardo",
    "Leticia", "Lucas", "Luciana", "Luciano", "Luiz", "Manuela", "Marcelo", "Marcia",
    "Marcos", "Maria", "Mariana", "Mario", "Matheus", "Mauricio", "Melissa", "Miguel",
    "Monica", "Murilo", "Natalia", "Nicolas", "Otavio", "Paola", "Patricia", "Paulo",
    "Pedro", "Priscila", "Rafael", "Raquel", "Renan", "Renata", "Ricardo", "Roberta",
    "Roberto", "Rodrigo", "Rogerio", "Ronaldo", "Samuel", "Sandra", "Sara", "Sergio",
    "Silvia", "Simone", "Sofia", "Tatiane", "Thiago", "Valeria", "Vanessa", "Victor"
]


# Criando dicionário indexado à partir da enumeração dos nomes da lista 'nomesGenericos'
dicionarioGenerico = {i: nome for i, nome in enumerate(nomesGenericos)}

# Teste unitário para visualizar a saída do dicionário apenas quando 'name_dict.py' é executado diretamente
if __name__ == "__main__":
    print(dicionarioGenerico)
