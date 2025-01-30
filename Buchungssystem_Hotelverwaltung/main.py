class Room:
    def __init__(self, room_number, room_price):
        self.room_number = room_number
        self.room_price = room_price
        self.room_is_booked = False

    def book_room(self):
        self.room_is_booked = True

    def cancel_room(self):
        self.room_is_booked = False


class Einzelzimmer(Room):
    def __init__(self, room_number, room_price=50):
        super().__init__(room_number, room_price)


class Doppelzimmer(Room):
    def __init__(self, room_number, room_price=100):
        super().__init__(room_number, room_price)


class Hotel:
    def __init__(self, name, rooms):
        self.name = name
        self.rooms = rooms

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(room)

    def count_free_rooms(self):
        return sum(1 for room in self.rooms if not room.room_is_booked)

    def get_room_by_number(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None


if __name__ == "__main__":
    hotel_california = Hotel("Hotel California", [Einzelzimmer(101), Doppelzimmer(201), Einzelzimmer(102)])
    hotel_california.add_room(Doppelzimmer(202))

    hotel_california.get_room_by_number(101).book_room()
    print(hotel_california.count_free_rooms())

    hotel_california.get_room_by_number(101).cancel_room()
    print(hotel_california.count_free_rooms())
