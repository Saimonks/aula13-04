class Reserva:
    def __init__(
        self,
        id: int,
        usuario_id: int,
        sala_id: int,
        data: str,
        hora_inicio: str,
        hora_fim: str,
        status: str = "active"
    ):
        self.id = id
        self.usuario_id = usuario_id
        self.sala_id = sala_id
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.status = status

    def cancelar(self):
          self.status = "cancelado"


    def finalizar(self, hora_atual: str):
        self.status = "finalizado"
  

    def duracao_em_horas(self) -> float:
        pass

    def conflita_com(self, outra_reserva) -> bool:
        if self.sala != outra_reserva.sala_id or self_data != outra_reserva.data:
        return false

        if self.status == "cancelado" or outra_reserva.status == "cancelado":
            return False 

