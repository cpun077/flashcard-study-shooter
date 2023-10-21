class Gun: 
    def __init__(self, x, y, img, ammoCap):
        self.x = x
        self.y = y
        self.id = 'gun'
        self.img = img
        self.ammoCap = ammoCap
        self.ammo = ammoCap

    def shoot(self):
        self.ammo = self.ammo - 1

    def reload(self):
        self.ammo = self.ammoCap