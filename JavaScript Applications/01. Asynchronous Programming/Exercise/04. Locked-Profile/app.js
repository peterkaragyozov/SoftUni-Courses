async function lockedProfile() {
    
    const url = 'http://localhost:3030/jsonstore/advanced/profiles';
    const promise = await fetch(url);
    const data = await promise.json();
    const divEl = document.querySelector('main > div');
    const mainEl = document.querySelector('main');
    mainEl.innerHTML = '';
    Object.entries(data).forEach((e) => {
        let clone = divEl.cloneNode(true);
        clone.getElementsByTagName('input').user1Age.value = e[1].age;
        clone.getElementsByTagName('input').user1Username.value = e[1].username;
        clone.getElementsByTagName('input').user1Email.value = e[1].email;
        clone.getElementsByTagName('input').user1Locked.name = e[1].username + 'Locked';
        clone.getElementsByTagName('input').user1Locked.name = e[1].username + 'Locked';
        mainEl.appendChild(clone)
        
        
    })

    mainEl.addEventListener('click', (ev) => {
        if (ev.target.tagName == 'BUTTON') {
            const profile = ev.target.parentNode
            const isLocked = profile.querySelector('input[type=radio]:checked').value == 'lock';
            if (isLocked) {
                return;
            }

            let div = profile.querySelector('div');
            let isVisible = div.style.display == 'block';
            div.style.display = isVisible ? 'none' : 'block';
            ev.target.textContent = !isVisible ? 'Hide it' : 'Show more'
        }
    })

}