class Convert_to_miles:
    @staticmethod
    def convert(amount, metrics: str):
        match metrics:
            case "centimetre":
                return amount / 160934

            case "metre":
                return amount / 1609

            case "kilometre":
                return amount / 1.609

            case _:
                raise Exception("You can convert only centimetre, metre and kilometre")


print(Convert_to_miles.convert(100, "metre"))