from .notificator_interface import NotificatorInterface

class NotificatorSMS(NotificatorInterface):
    def send_notification(self, message: str):
        print(f"Enviando notificação por SMS: {message}")