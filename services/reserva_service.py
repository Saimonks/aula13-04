from domain.usuario import Usuario
from domain.sala import Sala
from domain.reserva import Reserva
from repositories.memory import db


def criar_usuario(nome: str, email: str):
    for u in db"[usuarios]".values():
        if  u.email == email:
            raise  ValueError("Email já cadastrado")

    novo_id = len(db["usuarios"]) + 1
    usuario = Usuario(id=novo_id, nome = nome, email=email)


def listar_usuarios():
    pass


def criar_sala(nome: str, capacidade: int, bloco: str):
    pass


def listar_salas():
    pass


def criar_reserva(usuario_id: int, sala_id: int, data: str, hora_inicio: str, hora_fim: str):
    pass


def listar_reservas():
    pass


def listar_reservas_usuario(usuario_id: int):
    pass


def buscar_reserva(reserva_id: int):
    pass


def cancelar_reserva(reserva_id: int):
    pass


def finalizar_reserva(reserva_id: int, hora_atual: str):
    pass