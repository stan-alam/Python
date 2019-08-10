class Stats(Assignment):
    def less(self):
        return (
            "Good work, "
            + self.student
            + ". Now calculate the avg of the numbers "
            + " 3, 8, 10, -5 and assign to a var named 'avg'"
        )
        
    def check(self, code):
        import stats
        
        code = "import stats\n" + code
        
        local_vars = { }
        global_vars = { }
        exec(code, global_vars, local_vars)
        
        return local_vars.get("avg") == stats.mean([3, 8, 10, -5])
