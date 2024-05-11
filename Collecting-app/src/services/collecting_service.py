from repositories.collecting_repository import collecting_repository


class CollectingService:

    def __init__(self, collecting_repository):
        self._collecting_repository = collecting_repository

    def add_phone(self, phone_data):

        required_fields = ['image', 'series', 'model_year', 'price']
        if not all(field in phone_data for field in required_fields):
            raise ValueError("All fields must be provided.")

        self._collecting_repository.add_phone(phone_data)

    def fetch_data(self):
        raw_data = self._collecting_repository.fetch_data()
        return raw_data

    def update_phone(self, phone_id, update_data):
        self._collecting_repository.update_phone(phone_id, update_data)

    def delete_phone(self, phone_id):
        del_row = self._collecting_repository.delete_phone(phone_id)
        return del_row

    def get_phone_stats(self):
        return self._collecting_repository.fetch_phone_stats()

collecting_service = CollectingService(collecting_repository)
