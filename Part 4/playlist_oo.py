class Titles:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    # Define properties

    @property
    def likes(self):
        return self._likes

    @property
    def name(self):
        return self._name

    # Define setters

    @name.setter
    def name(self, name):
        self._name = name

    # Define methods

    def give_like(self):
        self._likes += 1


class Movie(Titles):
    def __init__(self, name, year, length):
        super().__init__(name, year)
        self.length = length

    # Define dunder methods

    def __str__(self):
        return f'Name: {self._name} - {self.length} min - Likes: {self._likes}'


class Sitcom(Titles):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    # Define dunder methods

    def __str__(self):
        return f'Name: {self._name} - {self.seasons} seasons - Likes: {self._likes}'


class Playlist():
    def __init__(self, playlist_name, titles):
        self.playlist_name = playlist_name
        self.titles = titles

    # Define dunder methods

    def __getitem__(self, item):
        return self.titles[item]

    def __len__(self):
        return len(self.titles)