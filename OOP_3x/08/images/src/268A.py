#268.A
def process_include(self, match, argument):
    with(self.working_dir / argument).open() as include_file:
        self.outfile.write(include_file.read())
        self.pos = match.end()

def process_variable(self, match, argument):
    self.outfile.write(self.context.get(argument, ''))
    self.pos = match.end()
