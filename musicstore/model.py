from datetime import datetime


# TODO: Add code here
class Transaction:
    SELL: int = 1
    SUPPLY: int = 2

    def __init__(self, type: int, copies: int):
        self.type: int = type
        self.copies: int = copies
        self.date: datetime = datetime.now()


class Disc:
    def __init__(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        self.sid: str = sid
        self.title: str = title
        self.artist: str = artist
        self.sale_price: float = sale_price
        self.purchase_price: float = purchase_price
        self.quantity: int = quantity
        self.transactions: list[Transaction] = []
        self.song_list: list[str] = []

    def add_song(self, song: str):
        self.song_list.append(song)

    def sell(self, copies: int) -> bool:
        if copies > self.quantity:
            return False
        else:
            self.quantity -= copies
            self.transactions.append(Transaction(Transaction.SELL, copies))
            return True

    def supply(self, copies: int):
        self.quantity += copies
        self.transactions.append(Transaction(Transaction.SUPPLY, copies))

    def copies_sold(self) -> int:
        total_copies = 0
        for transaction in self.transactions:
            if transaction.type == Transaction.SELL:
                total_copies += transaction.copies
        return total_copies

    def __str__(self) -> str:
        return f"SID: {self.sid}\nTitle: {self.title}\nArtist: {self.artist}\nSong List: {", ".join(self.song_list)}"


class MusicStore:
    def __init__(self):
        self.discs: dict[str, Disc] = {}

    def add_disc(self, sid: str, title: str, artist: str, sale_price: float, purchase_price: float, quantity: int):
        if sid not in self.discs:
            new_disc = Disc(sid, title, artist, sale_price, purchase_price, quantity)
            self.discs[sid] = new_disc

    def search_by_sid(self, sid: str) -> Disc | None:
        return self.discs.get(sid)

    def search_by_artist(self, artist: str) -> list[Disc]:
        list_artist = []
        for disc in self.discs.values():
            if disc.artist == artist:
                list_artist.append(disc)
        return list_artist

    def sell_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False

        return disc.sell(copies)

    def supply_disc(self, sid: str, copies: int) -> bool:
        disc = self.search_by_sid(sid)
        if disc is None:
            return False

        disc.supply(copies)
        return True

    def worst_selling_disc(self) -> Disc | None:
        worst_disc = None
        cant_disc = 10000000
        for disc in self.discs.values():
            disc_sold = disc.copies_sold()
            if disc_sold < cant_disc:
                cant_disc = disc_sold
                worst_disc = disc
        return worst_disc
