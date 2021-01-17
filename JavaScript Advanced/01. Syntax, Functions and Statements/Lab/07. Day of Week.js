function weekday(dayAsString) {
    let days = {
        'Monday': 1,
        'Tuesday': 2,
        'Wednesday': 3,
        'Thursday': 4,
        'Friday': 5,
        'Saturday': 6,
        'Sunday': 7,
    };

    // if the dayAsString argument is not among the keys, it will return 'undefined', thus being Falsy
    console.log(days[dayAsString] || 'error'); 

}

weekday('Monday');
weekday('Friday');
weekday('Invalid');
