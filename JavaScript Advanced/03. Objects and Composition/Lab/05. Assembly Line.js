function solve() {
    function hasClima(obj) {
        const props = {
            temp: 21,
            tempSettings: 21,
            adjustTemp
        }
 
        function adjustTemp() {
            if (this.temp < this.tempSettings) {
                this.temp++;
            } else if (this.temp > this.tempSettings) {
                this.temp--;
            }
        }
 
        Object.assign(obj, props);
    }
 
    function hasAudio(obj) {
        const props = {
            currentTrack: null,
            nowPlaying
        }
 
        function nowPlaying() {
            if (this.currentTrack !== null) {
                console.log(`Now playing '${this.currentTrack.name}' by ${this.currentTrack.artist}`);
            }
        }
 
        Object.assign(obj, props);
    }
 
    function hasParktronic(obj) {
        function checkDistance(distance) {
            if (distance < 0.1) {
                console.log('Beep! Beep! Beep!');
            } else if (distance < 0.25) {
                console.log('Beep! Beep!');
            } else if (distance < 0.5) {
                console.log('Beep!');
            } else {
                console.log('');
            }
        }
        Object.assign(obj, { checkDistance });
    }
 
    return {
        hasClima,
        hasAudio,
        hasParktronic
    }
}

const assemblyLine = solve();

const myCar = {
    make: 'Toyota',
    model: 'Avensis'
};

assemblyLine.hasClima(myCar);
console.log(myCar.temp);
myCar.tempSettings = 18;
myCar.adjustTemp();
console.log(myCar.temp);

assemblyLine.hasAudio(myCar);
myCar.currentTrack = {
    name: 'Never Gonna Give You Up',
    artist: 'Rick Astley'
};
myCar.nowPlaying();

assemblyLine.hasParktronic(myCar);
myCar.checkDistance(0.4);
myCar.checkDistance(0.2);

console.log(myCar);
