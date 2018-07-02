class Legend:


    def __init__(self):
        self.navi = Navi()
        self.cv_actor = ''
        self.cv_volume = 100


    def set_cv(self):
        name = self.navi.ask('Hay! Listen! What is your name?')
        if name == 'Link':
            self.cv_actor = 'Hayami'
        else:
            self.cv_volume = 0


    def is_princess(self, name):

        # Actually, Malon is not a princess

        if name in ['Zelda', 'Seek', 'Ruto', 'Malon']:
            return True
        else:
            return False


class Navi:

    def ask(self, message):
        print(message)
        return input('>> ')


if __name__ == '__main__':
    legend = Legend()
    legend.set_cv()
    print("actor:%s, volume:%d" % (legend.cv_actor, legend.cv_volume))
