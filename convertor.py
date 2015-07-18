from generator import Generator


class Convertor(Generator):
    def __init__(self, file_name):
        Generator.__init__(self)
        self.file_name = file_name

    def add_testimony(self, new_testimony):
        Generator.add_testimony(self, new_testimony)
        with open(self.file_name, "a") as f:
            f.write(self.str(new_testimony))

    def add_saved_testimonies(self):
        with open(self.file_name, "r") as f:
            saved_testimony = f.readline()
            self.testimonies.append(saved_testimony)

    def remove_testimony(self, testimony):
        Generator.remove_testimony(self, testimony)
        self.update_file()

    def update_file(self):
        with open(self.file_name, "w") as f:
            for testimony in self.testimonies:
                f.write(self.str(testimony))

    def str(self, testimony):
        return "{}\n".format(testimony)
