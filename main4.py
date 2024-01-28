class InformationSystem:
    _data = {}

    @classmethod
    def add(cls):
        user = input("Enter name of user: ")
        amount_of_contacts = int(input("Enter amount of contacts: "))

        lst = [input("Enter contact: ") for _ in range(amount_of_contacts)]

        cls._data[user] = lst

        lst_keys = list(cls._data.keys())

        for i in range(len(lst_keys)):
            print(f"{lst_keys[i]}: {cls._data[lst_keys[i]]}")


InformationSystem.add()
