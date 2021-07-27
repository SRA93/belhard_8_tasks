class Gardener:

    name: str
    plants: list

    def __init__(self, name, *args):

        self.name = name
        self.plants = list(args)

    def work(self):

        for i in self.plants:
            i.grow_all()

    def harvest(self):

        num_tomato = []

        for i in self.plants:

            if i.all_are_ripe() is False:
                break

            num_tomato.extend(i.tomato_list)

        else:
            return num_tomato

        print('Томаты пока не созрели.')
