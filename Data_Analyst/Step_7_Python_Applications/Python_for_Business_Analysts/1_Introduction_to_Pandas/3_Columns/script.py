# Generated by Haxe 3.3.0

import pandas as pandas_Pandas_Module


class Script:
    __slots__ = ()

    @staticmethod
    def main():
        housing_2013 = pandas_Pandas_Module.read_csv("../Hud_2013.csv")
        columns = housing_2013.columns
        num_columns = len(columns)
        print(str(num_columns))



Script.main()