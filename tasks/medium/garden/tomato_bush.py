from tomato import Tomato


class TomatoBush(Tomato):

    tomato_list: list

    def __init__(self, *args):

        self.tomato_list = list(args)

    def grow_all(self):

        for i in self.tomato_list:
            i.grow()

    def all_are_ripe(self):

        for i in self.tomato_list:
            if i.is_ripe() is False:

                return False

        return True

    def give_away_all(self):

        result = self.tomato_list.copy()
        self.tomato_list.clear()

        return result
