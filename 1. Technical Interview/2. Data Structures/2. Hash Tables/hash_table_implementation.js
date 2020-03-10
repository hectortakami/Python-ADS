console.log("\n\n*********** HASH TABLE IMPLEMENTATION *************\n")

class HashTable {
    constructor(size) {
        // Represents the memory spaces where to fill with addresses and key:value pairs
        this.data = new Array(size);
    }
    _hash(key) {
        let hash = 0;
        for (let i = 0; i < key.length; i++) {
            // This function allow us to constuct the hashing address where the [key:value]
            // will be stored inside the this.data memory allocation representation
            hash = (hash + key.charCodeAt(i) * i) % this.data.length
        }
        return hash;
    }

    set(key, value) {
        let address = this._hash(key);
        if (!this.data[address]) {
            this.data[address] = [];
        }
        // Just verify if the memmory address was already in use, if thats the case we push another
        // [key:value] pair inside of it, otherwise we just create an empty array (currentBucket)
        // to store the tuple and for upcoming maps
        this.data[address].push([key, value]);
        return this.data;
    }

    get(key) {
        const address = this._hash(key);
        const currentBucket = this.data[address]
        // The currentBucket represents a memmory address that can have many values in it 
        // thats why we need to iterate it, in order to retreive each key:value pair stored
        if (currentBucket) {
            for (let i = 0; i < currentBucket.length; i++) {
                if (currentBucket[i][0] === key) {
                    return currentBucket[i][1]
                }
            }
        }
        return undefined;
    }

    getAllKeys() { // O(n^2)
        // Retreives all the keys stored in the memmory address allocation
        const keysArr = [];

        this.data.forEach(currentBucket => {
            currentBucket.forEach(hashTable => {
                keysArr.push(hashTable[0]);
            });
        });

        return keysArr;
    }

}
// Defines the memomry space available (50 addresses possible)
const myHashTable = new HashTable(50);

myHashTable.set('grapes', 27);
myHashTable.set('apples', 78);
myHashTable.set('oranges', 54);

console.log('\n');
console.log(myHashTable.getAllKeys());

console.log('\n grapes => ' + myHashTable.get('grapes'));
console.log(' apples => ' + myHashTable.get('apples'));
console.log(' oranges => ' + myHashTable.get('oranges') + '\n');


console.log("\n***************************************************\n")