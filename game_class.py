from game import health, level, strength
class battleTime:
    def __init__(self, enemies):
        self.enemies = enemies
        enemy_list = []
        enemy_list.append(enemies)
        print('health:', health, ' attack', ' defend', 'items')
        if len(enemy_list) == 1:
            Attacker = enemy_list[1]        
            if Attacker == '1':
                monster_health = 10
                monster_attack = 2
        
