from abc import ABC, abstractmethod

class usuario(ABC):
    def __init__(self):
        self.__login = None
        self.__senha = None
        self.__gmail = None
        self.__tipoUsuario = None
        self.__emprestimos = []

    def setLogin(self, login):
        self.__login = login

    def getLogin(self):
        return self.__login

    def setSenha(self, senha):
        self.__senha = senha

    def getSenha(self):
        return self.__senha

    def setGmail(self, email):
        self.__gmail = email

    def getGmail(self):
        return self.__gmail

    def setTipoUsuario(self, tipoUsuario):
        self.__tipoUsuario = tipoUsuario

    def getTipoUsuario(self):
        return self.__tipoUsuario

    def setEmprestimos(self, emprestimos):
        self.__emprestimos = emprestimos

    def addEmprestimo(self, emprestimo):
        self.__emprestimos.append(emprestimo)

    def removeEmprestimo(self, emprestimo):
        self.__emprestimos.remove(emprestimo)

    def getEmprestimos(self):
        return self.__emprestimos
