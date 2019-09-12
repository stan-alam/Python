class Supplier(Contact):
    def order(self, order):
        print( 
            "If this were a prod system you would  send " f"'{order}' order to '{self.name}'"
        )
