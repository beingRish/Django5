from django.dispatch import Signal, receiver

# Creating Signal
notification = Signal()

# Rec Function
@receiver(notification)
def show_notification(sender, **kwargs):
    print("--------------------------")
    print("Notification")
    print(sender)
    print(f"{kwargs}")