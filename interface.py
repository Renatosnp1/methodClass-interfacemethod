class Animal:

    def __init__(self, nome, estado, ano_nascimento) -> None:
        self.nome = nome
        self.estado = estado
        self.ano_nascimento = ano_nascimento

    def me_apresentado(self):
        return f"Olá, meu nome é {self.nome} e estou {self.estado}"

    def minha_idade(self):
        idade = 2024 - self.ano_nascimento
        return f"Minha idade é {idade} anos"


class Gato(Animal):  # Gato herda de Animal
    def __init__(self, nome, estado, ano_nascimento, patas) -> None:
        Animal.__init__(self, nome, estado, ano_nascimento)  # Chama o construtor de Animal
        self.patas = patas

    def quantidade_patas(self):
        return f"Eu tenho {self.patas} patas"


class Tartaruga(Animal):  # Tartaruga herda de Animal
    def __init__(self, nome, estado, ano_nascimento, cor_casco) -> None:
        Animal.__init__(self, nome, estado, ano_nascimento)  # Chama o construtor de Animal
        self.cor_casco = cor_casco

    def cor_do_casco(self):
        return f"Meu casco é cor {self.cor_casco}"


class Cavalo(Gato, Tartaruga):  # Cavalo herda de Gato e Tartaruga

    def __init__(self, nome, estado, ano_nascimento, patas, peso, cor_casco) -> None:
        Gato.__init__(self, nome, estado, ano_nascimento, patas)  # Chama o __init__ de Gato
        Tartaruga.__init__(self, nome, estado, ano_nascimento, cor_casco)  # Chama o __init__ de Tartaruga
        self.peso = peso

    def meu_peso(self):
        return f"Meu peso é de {self.peso}Kg"


# # Testando a classe Gato
# gato = Gato("Garfield", "vivo", 2006, 4)
# print(gato.quantidade_patas())
# print(gato.me_apresentado())
# print(gato.minha_idade())
# print("=" * 60)

# # Testando a classe Tartaruga
# tartaruga = Tartaruga("Garfild", "vivo", 2006, "verde")
# print(tartaruga.me_apresentado())
# print(tartaruga.minha_idade())
# print(tartaruga.cor_do_casco())
# print("=" * 60)

# # Testando a classe Cavalo
# cavalo = Cavalo("Spirit", "vivo", 2006, 4, 200, "marrom")
# print(cavalo.me_apresentado())
# print(cavalo.minha_idade())
# print(cavalo.cor_do_casco())
# print(cavalo.meu_peso())
# print("=" * 60)
