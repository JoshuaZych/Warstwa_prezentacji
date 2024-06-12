class DatabaseManager:
    data_store = []

    @classmethod
    def add_data(cls, data):
        cls.data_store.append(data)

    @classmethod
    def get_all_data(cls):
        return cls.data_store
