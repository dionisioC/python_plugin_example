from plugins.plugin import Plugin


class AdditionPlugin(Plugin):
    op = '+'

    @staticmethod
    def calc(num_1, num_2):
        return num_1 + num_2
