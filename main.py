from datetime import datetime, timedelta
from abc import ABC, abstractmethod



menu = """
[d] Depositar
[s] Sacar
[e] Extrato


[q] Sair


=> """

texto_pesquisa_usuario = '''
Você está na pagina para localizar os contratos feitos       
Para listar todos digite - [1]
Para buscar um usuario digite - [2]
'''

def login(cookie):

    print("\nOlá Bem vindo ao sistema bancario!")
    login_cliente = str(input("Favor, digite seu cpf para inicio: "))
    usuario_login = pesquisa_cpf(login_cliente)
    print("Ok pesquisa de CPF")
    conta_login = pesquisa_conta(login_cliente)
    print("Ok pesquisa de Conta")

    cookie_login[0] = login_cliente

    return usuario_login, conta_login, login_cliente

    return faltam_horas, faltam_minutos


def teste_dados_iguais(texto_dado):
    opcao = -1
    while opcao != 0 :
        
        teste = 1
        solicitacao_do_dado = input(texto_dado)

        if solicitacao_do_dado.isdigit() == True:
          
            for usuario in usuarios:
                if usuarios[usuario]["CPF"] == int(solicitacao_do_dado):
                    teste = 0

            if teste == 0 :
                print(f'Opa! Esse CPF ({solicitacao_do_dado}) já está na nossa base.\nSe ele for seu, é só recuperar sua conta.\nQuer continuar? Basta informar outro CPF.')
                opcao = -1

            elif teste != 0 :
                opcao = 0
                return solicitacao_do_dado

        else:
            print("Não é digito")
            teste = False
            return teste

def funcao_extrato(opcao_escolhida, conta_escolhida):
    
    print("Opção escolhida - Extrato")
    print("\n=================== EXTRATO ===================")
    if not historico[opcao_escolhida]:
        print("Não foram realaizadas movimentações.")  

    else: 
        for chave, valor in historico[opcao_escolhida]:
            print(f"{chave}                  {valor}")
            
    saldo_atualizado = conta_escolhida.alterar_saldo(valor, conta_escolhida,acao = "deposito")

    print(f"\nSaldo de : R$ {saldo_atualizado:.2f}")
    print("===============================================")
    print("Extrato fechado")

def funcao_criar_usuario():
        
        novo_usuario = len(usuarios) + 1
        print(f"Criando o usuario {novo_usuario:04d}")
        
        texto_cpf = "Digite seu CPF (apenas números, sem pontos ou traços): "
        cpf_testado = teste_dados_iguais(texto_cpf)
        nome = input("Digite seu nome completo: ")
        data_de_nascimento = input("Digite sua data de nascimento: ")
        
        print("\nVamos cadastrar seu endereço!\n")

        endereco_rua = input("Digite a rua: ")
        endereco_numero = input("Digite o numero: ")
        endereco_bairro = input("Digite o bairro: ")
        endereco_cidade = input("Digite a cidade: ")
        endereco_estado = input("Digite a sigla do estado: ")

        print(f"""
Olá {nome}!, vamos confirmar os dados, ok?
Data de Nascimento: {data_de_nascimento}
CPF: {cpf_testado}
Endereço: {endereco_rua}, {endereco_numero} - {endereco_bairro} - {endereco_cidade}/{endereco_estado}.
              """)
        
        confirmacao = input('Você confirma essas informações? \ndigite [s] ou [n]: ').upper()
        if confirmacao == "S" :
            endereco_formatado = f"{endereco_rua}, {endereco_numero} - {endereco_bairro} - {endereco_cidade}/{endereco_estado}"
            usuarios.update({novo_usuario: {
                "Nome":nome,
                "Data de Nascimento": data_de_nascimento,
                "CPF": cpf_testado,
                "Endereço Formatado" : endereco_formatado,
                "Endereço" : {
                    "Logradouro": endereco_rua,
                    "Numero" : endereco_numero,
                    "Bairro" : endereco_bairro,
                    "Cidade" : endereco_cidade,
                    "Sigla" : endereco_estado},
                "Conta Corrente" : None
                    }})
            print("Parabens! Você acaba de cadastrar o usuario!")
            

        else:
            input("Ok, vamos iniciar novamente o cadastro.")

def funcao_criar_conta(cpf):
    nova_conta = len(contas)+1
    contas.update({nova_conta:{
        "Agencia": 1,
        "CPF do Titular": cpf,
        "saldo" : 0,
        "limite" : 500,
        "extrato" : {},
        "numero_saques" : 0,
        "numero_depositos" : 0,
        "numero_transacao" : 0,}
        })
    print(f"\nConta {contas[nova_conta]["Agencia"]:04d}/{nova_conta:08d} Criada com sucesso!")

def pesquisa_cpf (cpf):
    teste_cpf = None
    for usuario in usuarios:
        extrair_cpf = usuarios[usuario].dados["cpf"]
        if str(extrair_cpf) == str(cpf):
            teste_cpf = 1
        else:
            teste_cpf = "Não Localizado"
    return teste_cpf

def pesquisa_conta(cpf):
    contas_localizadas = []

    for conta in contas:
        extrair_conta = contas[conta].dados["cpf"]
        if str(extrair_conta) == str(cpf):
            conta_encontrada = conta
            contas_localizadas.append(f"{contas[conta].dados["agencia"]:04d}/{conta_encontrada:08d}")
    
    if not contas_localizadas:
        contas_localizadas = "Não Localizado Conta Corrente vinculadas a este CPF"
    
    return contas_localizadas

def texto_padrao_usuario(conta):

    trasnformar_cpf_string = str(usuarios[conta]["CPF"])
    cpf_formatado = f"{trasnformar_cpf_string[:3]}.{trasnformar_cpf_string[3:6]}.{trasnformar_cpf_string[6:9]}-{trasnformar_cpf_string[9:]}"
    texto_padrao = f"\nUsuario: {conta:04} \n   Nome: {usuarios[conta]['Nome']}\n   CPF: {cpf_formatado}\n   Endereço: {usuarios[conta]["Endereço Formatado"]}"      
    
    return texto_padrao

'''
usuarios = { 1:{
        "Nome":"Danilo",
        "Data de Nascimento": "29/09/1995",
        "CPF": 441,
        "Endereço Formatado" : "Rua Moema, 53 - Vila Pereta - Poá/SP",
        "Endereço" : {
            "Logradouro": "Rua Moema",
            "Numero" : 53,
            "Bairro" : "Vila Pereta",
            "Cidade" : "Poá",
            "Sigla" : "SP"},
        "Conta Corrente" : {"0001": 1}
        }}
'''
'''
contas = {1:{
    "Agencia": 1,
    "CPF do Titular": usuarios[1]["CPF"],
    "saldo" : 2000,
    "limite" : 500,
    "extrato" : {},
    "numero_saques" : 0,
    "numero_depositos" : 0,
    "numero_transacao" : 0,}
}
'''
historico = {
    441:[]
}

class Conta:
    def __init__(self, saldo, numero_conta, agencia, cpf):
        self._saldo = saldo
        self._numero_conta = numero_conta
        self._agencia = agencia
        self._cpf = cpf
        self._historico = Historico #PONTO DE ATENÇÃO!

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
        
    @property
    def numero_conta(self):
        return self._numero_conta
    @property
    def agencia(self):
        return self._agencia
    @property
    def cpf(self):
        return self._cpf
    @property
    def historico(self):
        return self._historico
    
    def alterar_saldo(self, valor, conta_escolhida, acao):
        if acao == "saque":
            conta_escolhida.saldo -= int(valor)
        elif acao == "deposito":
            conta_escolhida.saldo += int(valor)

        return conta_escolhida.saldo

    
    def nova_conta(cliente: "Cliente", numero:8): Conta

    def sacar(self,valor, conta_escolhida):
        if valor == "" :
            print("Operação falhou! Insira um valor")              

        else:
            valor = float(valor)

            if valor < 0:
                print("Operação falhou! Insira um valor positivo")

            elif valor > conta_escolhida.saldo:
                print("Operação falhou! Não é possivel sacar o dinheiro por falta de saldo")

            elif valor > 500.00:
                print("Operação falhou! Valor acima do limite por saque, escolha um valor abaixo de R$ 500,00")

            else:
                conta_escolhida.numero_saques += 1
                conta_escolhida.numero_transacao += 1
                saldo_atualizado = conta_escolhida.alterar_saldo(valor, conta_escolhida,acao = "saque")
                print("\n===============================================\n")
                print("Saque será realizado")
                print(f"Saldo de R${saldo_atualizado}")
                print(f"Ainda possui {conta_escolhida.limite_transacao - conta_escolhida.numero_transacao} transações.")
                print("\n===============================================\n")

    def depositar(self, valor, conta_escolhida):
        if valor != "":
            valor = float(valor)
            if valor > 0:
                conta_escolhida.numero_depositos += 1
                conta_escolhida.numero_transacao += 1
                saldo_atualizado = conta_escolhida.alterar_saldo(valor, conta_escolhida,acao = "deposito")
                print("\n===============================================\n")
                print(f"O novo saldo é de R${saldo_atualizado:.2f}")
                print(f"Atualizado o Extrato, foram feitas {conta_escolhida.dados["numero_transacao"]} transações.")
                print("\n===============================================")

            else:
                print("Operação falhou! Insira um valor positivo")

        else:
                print("Operação falhou! Insira um valor")

class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()
        
    def registrar(self, conta):

        if conta_escolhida.sacar(valor, conta):
            conta_escolhida.historico.update({agora.strftime("%d/%m/%Y %H:%M:%S"):f"- R$ {valor:.2f}"})
            return True
        return False
    
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data = datetime.now()

    def registrar(self, conta):
        if conta_escolhida.depositar(valor, conta):
            conta_escolhida.historico.update({agora.strftime("%d/%m/%Y %H:%M:%S"):f"- R$ {valor:.2f}"})
            return True
        return False

class Historico:
    def adicionar_transacao(transacao: Transacao, conta_escolhida):
        pass

class ContaCorrente(Conta):
    def __init__(self, saldo, numero_conta, agencia, cpf, limite_transacao, limite_saques, limite_por_saque, numero_transacao, numero_saques, numero_depositos):
        super().__init__(saldo, numero_conta, agencia, cpf)
        self._limite_transacao = limite_transacao
        self._limite_saques = limite_saques
        self._limite_por_saque = limite_por_saque
        self._numero_transacao = numero_transacao
        self._numero_saques = numero_saques
        self._numero_depositos = numero_depositos

    @property
    def limite_transacao(self):
        return self._limite_transacao
    @property
    def limite_saques(self):
        return self._limite_saques
    @property
    def limite_por_saque(self):
        return self._limite_por_saque
    
    @property
    def numero_transacao(self):
        return self._numero_transacao
    @numero_transacao.setter
    def numero_transacao(self, valor):
        self._numero_transacao = valor
    
    @property
    def numero_saques(self):
        return self._numero_saques
    @numero_saques.setter
    def numero_saques(self, valor):
        self._numero_saques = valor

    @property
    def numero_depositos(self):
        return self._numero_depositos
    @numero_depositos.setter
    def numero_depositos(self, valor):
        self._numero_depositos = valor
    
    @property
    def dados(self):
        return {
            "saldo" : self._saldo,
            "numero_conta" : self._numero_conta,
            "agencia" : self._agencia,
            "cpf" : self._cpf,
            "historico" : self._historico,
            "limite_transacao" : self._limite_transacao,
            "limite_saques" : self._limite_saques,
            "limite_por_saque" : self._limite_por_saque,
            "numero_transacao": self._numero_transacao,
            "numero_saques" : self._numero_saques,
            "numero_depositos": self._numero_depositos        
            }

    def teste_excessao_no_dia(self, agora):
        amanha = (agora + timedelta(days=1)).replace(hour=0,minute=0,second=0,microsecond=0)
        diferenca = amanha - agora
        faltam_horas = diferenca.seconds//3600
        faltam_minutos = (diferenca.seconds%3600) // 60
        return faltam_horas, faltam_minutos




class Cliente:
    def __init__(self, endereco, contas):
        self._endereco = endereco
        self._contas = contas

    @property
    def endereco(self):
        return self._endereco

    @property
    def contas(self):
        return self._contas
    
    def realizar_transacao(conta: Conta, transacao: Transacao):
        pass

    def adicionar_conta(conta: Conta):
        pass

class PessoaFisica (Cliente):
    def __init__(self,endereco, contas,cpf,nome,data_nascimento):
        super().__init__(endereco, contas)
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento

    @property
    def cpf(self):
        return self._cpf
    @property
    def nome(self):
        return self._nome
    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def dados(self):
        return {
            "nome" : self._nome,
            "cpf" : self._cpf,
            "data_nascimento" : self._data_nascimento,
            "endereco" : self._endereco,
            "contas" : self._contas
        }

usuarios = {}

usuarios[441] = PessoaFisica(
    nome="Danilo",
    cpf=441, 
    data_nascimento= "29/09/1995", 
    endereco= "Rua Moema, 53 - Vila Pereta - Poá/SP", 
    contas= [{"0001": 1}]
    )

print(usuarios[441].dados["contas"])

contas = {}
contas[1] = ContaCorrente(
    agencia= 1,
    saldo=150,
    numero_conta=1,
    cpf= usuarios[441].cpf,
    limite_transacao= 10,
    limite_saques= 3,
    limite_por_saque= 500,
    numero_transacao=0,
    numero_saques = 0,
    numero_depositos = 0
    )

print(contas[1].dados["limite_por_saque"])

tentativas_login = 0

cookie_login = [0]

while True:
    if cookie_login[0] == 0:
        usuario_login, conta_login, login_cliente = login(cookie_login)
        print(f"usuario_login: {usuario_login}, conta_login: {conta_login}, login_cliente: {login_cliente}")
    

    if usuario_login == 1:
        
        print("\n================== Bem vindo ==================\n"),
        usuario_logado = usuarios[int(login_cliente)]
        print(f"Nome: {usuario_logado.dados["nome"]} \nCPF: {usuario_logado.dados["cpf"]}\n")
        
        contas_pesquisa = pesquisa_conta(login_cliente)

        contagem = 0
        conta_logada = 0

        for conta in contas_pesquisa:
            contagem += 1
            print(f"[{contagem}] {conta}")
    
        menu_usuario_logado ="[n] Nova Conta Corrente\n[q] Sair"

        print(menu_usuario_logado)

        opcao_escolhida = input("\nEscolha a opção desejada =>").upper()
    
        if opcao_escolhida == "Q": 
            print("Sistema fechado.")
            cookie_login[0] = 0
            break

        elif opcao_escolhida == "N":

            print("\n============= Criar Conta Corrente ============\n")

            if cookie_login[0] != 0:
                cpf_para_pesquisa = cookie_login[0]
            else:
                cpf_para_pesquisa = input("Favor digite o CPF do titular da nova conta: ")

            if pesquisa_cpf(cpf_para_pesquisa) == "Não Localizado" :

                print("Não existe usuário com este CPF, deseja criar um novo usuário?")
                teste = input("Digite [C] para Criar Usuário ou [S] para Sair: ")

                if teste == "c":
                    print("Criar Usuário")
                    funcao_criar_usuario()
                
            else:
                contas_pesquisa = pesquisa_conta(cpf_para_pesquisa)
                print("\n Contas já criadas: ")
                for conta in contas_pesquisa:
                    print(f"    Conta Corrente: {conta}")

                print("\nDeseja criar uma nova conta?")

                criar_nova_conta = input("Digite [S] para sim e [N] para não: ").upper()

                if criar_nova_conta == "S":
                    funcao_criar_conta(cpf_para_pesquisa)
                    print("\n Voltando ao menu anterior\n")
                    continue
                else: continue

        elif opcao_escolhida.isdigit() == True:
            if int(opcao_escolhida) <= int(contagem):

                conta_escolhida = contas[int(opcao_escolhida)]

                agora = datetime.now()
                opcao = input(menu).upper()
                
                faltam_horas,faltam_minutos = contas[int(opcao_escolhida)].teste_excessao_no_dia(agora)

                texto_excedeu_transacoes = f"\nVocê excedeu o número de transações permitidas para hoje!\nlimite irá reestabelecer em {faltam_horas} horas e {faltam_minutos} minutos."

                if opcao == "D":

                    if conta_escolhida.dados["numero_transacao"] >= 10 :
                        print(texto_excedeu_transacoes)
                        continue
                    print("===============================================")
                    print("\nOpção escolhida - Depositar")
                    valor = input("insira o valor para depósito: ")
                    Deposito(valor).registrar(conta_escolhida)

                elif opcao =="S":

                    if conta_escolhida.dados["numero_transacao"] >= 10 :
                            print(
                    f'\nVocê excedeu o número de transações permitidas para hoje!\nlimite irá reestabelecer em {faltam_horas} horas e {faltam_minutos} minutos.')
                            continue
                    
                    if conta_escolhida.dados["numero_saques"] >= conta_escolhida.dados["limite_saques"] :
                        print("Operação falhou! Você alcançou o limite diario, novo saque apenas amanhã")

                    else: 
                        print("\n===============================================\n")
                        print("Opção escolhida - Sacar")
                        print(f"Seu saldo é de R$ {conta_escolhida.dados["saldo"]}\n")

                        valor = input("Insira o valor para saque: ")
                        Saque(valor).registrar(conta_escolhida)
                        #conta_escolhida.sacar(conta_escolhida)
                        #funcao_saque(dados = conta_escolhida, agora = agora)

                elif opcao == "E":
                    funcao_extrato(login_cliente, conta_escolhida)

                elif opcao == "Q":

                    print("Sistema fechado.")
                    break

                else:
                    print("Operação inválida, por favor selecione novamente a operação desejada.")

            else:
                print("Opção inválida")
                continue

        else:
            print("Opção inválida, iniciando o sistema novamente")
            continue

    elif tentativas_login <= 2:
         tentativas_login += 1
         print("Não existe usuário com este CPF, deseja criar um novo usuário?")
         teste = input("Digite [C] para Criar Usuário ou [S] para Sair: ")

         if teste == "c":
            print("Criar Usuário")
            funcao_criar_usuario()
         continue

    elif tentativas_login == 2:
        tentativas_login = 0
        break
        

    