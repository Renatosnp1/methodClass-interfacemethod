from abc import ABC, abstractmethod

# CLasse abstrata "forçando" que cada classe herdada tenha pelo menos
# 2 metodos "get_conn" e "close_conn" garantindo assim uma qualidade
# e garantia do padrão do codigo.
class Conexao(ABC):
    def __init__(self, user, password) -> None:
        self.user = user
        self.password = password

    @abstractmethod
    def get_conn(self):
        pass
    
    @abstractmethod
    def close_conn(self):
        pass

# Classe concreta implementado os metodos que são "forçado" a implementar 
# casa um com sua lógica.
class ConexaoMysql(Conexao):
    def get_conn(self):
        return "Conexão aberta Mysql"
    
    def close_conn(self):
        return "Conexão fechada Mysql"


# Classe concreta implementado os metodos que são "forçado" a implementar 
# casa um com sua lógica.
class ConexaoPostgres(Conexao):
    def get_conn(self):
        return "Conexão aberta Postgres"
    
    def close_conn(self):
        return "Conexão fechada Postgres"


# Instanciando as classes concretas
connmysql = ConexaoMysql("Renato", "123456")
print(connmysql.get_conn())
print(connmysql.close_conn())
print("="*60)
print("="*60)
connpostgres = ConexaoPostgres("Renato", "123456")
print(connpostgres.get_conn())
print(connpostgres.close_conn())

