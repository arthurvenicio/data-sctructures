class ConferenceRoomScheduler:
    def __init__(self, rooms):
        # Inicializa as salas com um dicionário que contém listas de horários de reuniões para cada sala.
        self.rooms = rooms
        self.schedule = {room: [] for room in self.rooms}

    def schedule_meeting(self, start_time, end_time):
        for room, meetings in self.schedule.items():
            # Verifica se o horário solicitado não conflita com reuniões já existentes na sala.
            if all(end_time <= m[0] or start_time >= m[1] for m in meetings):
                # Adiciona a reunião na agenda da sala.
                meetings.append((start_time, end_time))
                # Ordena as reuniões (opcional, para facilitar a leitura).
                meetings.sort()
                return f"Meeting scheduled in {room} from {start_time} to {end_time}."
        
        # Retorna erro caso nenhuma sala esteja disponível.
        return "ERROR: No rooms available for the requested time."

# Exemplo de uso:
rooms = ["roomA", "roomB"]
scheduler = ConferenceRoomScheduler(rooms)

# Agendando reuniões.
print(scheduler.schedule_meeting(7, 8))  # Deve reservar roomA.
print(scheduler.schedule_meeting(9, 10))  # Deve reservar roomA.
print(scheduler.schedule_meeting(7, 9))  # Deve reservar roomB.
print(scheduler.schedule_meeting(10, 11))  # Deve reservar roomB.
print(scheduler.schedule_meeting(7, 12))  # Deve gerar erro.