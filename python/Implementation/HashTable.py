""" This program implements the Hash Map using list and a simple Hash Function """
# Reference: [ https://www.youtube.com/watch?time_continue=561&v=9HFbhPscPU0 ]
# HashMap
class HashMap:
    def __init__(self):
        """ Initialize the size of the Hash Map and give the initial value of None """
        self.size = 6
        self.map = [None] * self.size

    def _get_hash(self, key):
        """ Compute Hash value by summing up ascii value for each characters in the key string
            and take the mod (%) of it with the size of the Hash Map
        """
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % 5

    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is None:
            return None
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]

    def delete(self, key):
        hash_key = self._get_hash(key)

        if self.map[hash_key] is None:
            return False

        for i in range(len(self.map[hash_key])):
            if self.map[hash_key][i][0] == key:
                self.map[hash_key].pop(i)
                return True

    def print(self):
        print('---PHONEBOOK---')
        for item in self.map:
            if item is not None:
                print(str(item))

my_hash = HashMap()
my_hash.add('Bob', '567-8888')
my_hash.add('Ming', '293-6753')
my_hash.add('Ming', '333-8233')
my_hash.add('Aditya', '852-6551')
my_hash.add('Alicia', '632-4123')
my_hash.add('Mike', '567-2188')
my_hash.add('Aditya','777-8888')
my_hash.print()
my_hash.delete('Bob')
my_hash.print()
print('Ming: ' + my_hash.get('Ming'))