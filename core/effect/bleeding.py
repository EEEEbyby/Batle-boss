from rich import print

from core.effect.poison import PoisonEffect

class BleedingEffect(PoisonEffect) :

    """Эффект Кровотечение: Каждый ход отнимает damage. Длится duration ходов """

    def __init__(self, duration: int, damage: int):
        """ Создаём новый эффект. Принимаем duration и damage"""
        super().__init__(duration, damage)
        print(f"[red]У вас кровопотеря![/red] Эффект будет действовать [blue]{duration}[/blue] ходов. А так же сила [blue]{damage}[/blue] ")
        self.damage = damage

    def apply(self, target):
        """Обновляем эффект. Отнимаем у target урон эффекта"""
        target.hp -= self.damage
