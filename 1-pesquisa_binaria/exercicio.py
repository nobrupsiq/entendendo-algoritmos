"""
Suponha que você tenha uma lista com 128 nomes e esteja fezendo uma pesquisa binária. Qual seria o número máximo de etapas que você levaria para encontrar o nome desejado?
"""

lista_de_nomes = sorted([
    "Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Hannah", "Isaac", 
    "Julia", "Kevin", "Liam", "Mona", "Nathan", "Olivia", "Paul", "Quincy", "Rachel", 
    "Steve", "Tina", "Uma", "Victor", "Wendy", "Xander", "Yara", "Zane", "Aaron", 
    "Bianca", "Carter", "Denise", "Ethan", "Fiona", "Gabe", "Helen", "Ian", "Jack", 
    "Kara", "Laura", "Miles", "Nina", "Oscar", "Paula", "Quinn", "Rebecca", "Sam", 
    "Tiffany", "Ursula", "Vincent", "Willow", "Xavier", "Yasmine", "Zara", "Adam", 
    "Bella", "Caleb", "Danielle", "Elliot", "Felicia", "George", "Holly", "Ivy", 
    "Jason", "Kim", "Lila", "Mason", "Naomi", "Owen", "Penelope", "Quentin", 
    "Rose", "Simon", "Tracy", "Ulrich", "Vera", "Wesley", "Xenia", "Yvonne", "Zack", 
    "Alan", "Brooke", "Chris", "Daisy", "Edward", "Faith", "Gary", "Hazel", "Iris", 
    "Jacob", "Kayla", "Logan", "Maria", "Nick", "Opal", "Peter", "Quiana", "Ruth", 
    "Scott", "Taylor", "Ulysses", "Vanessa", "Warren", "Ximena", "Yosef", "Zoey", 
    "Amelia", "Blake", "Cindy", "Dean", "Emanuel", "Faye", "Greg", "Hailey", "Isaiah", 
    "Jenna", "Kyle", "Leah", "Megan", "Neil", "Orion", "Patricia", "Quill", "Ron", 
    "Sophia", "Trevor", "Ula", "Vivian", "Wyatt", "Xandra"
])

def busca_binaria(lista, nome):
  baixo = 0
  alto = len(lista) -1
  contador = 0

  while baixo <= alto:
    meio = (baixo + alto) // 2
    chute = lista[meio]
    contador += 1

    if chute == nome:
      print(f'Numero máximo de etapas {contador}')
      return chute
    if chute > nome:
      alto = meio -1
    else: 
      baixo = meio + 1

  print(f'Numero máximo de etapas {contador}')
  return None

print(busca_binaria(lista_de_nomes, "Vera"))
