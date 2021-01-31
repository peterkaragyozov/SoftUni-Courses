function addItem() {
    const itemText = document.getElementById('newItemText');
    const itemValue = document.getElementById('newItemValue');
    const menu = document.getElementById('menu');
    const newOpt = document.createElement('OPTION');

    if (itemText.value === '' || itemValue.value === '') {
        itemText.value = '';
        itemValue.value = ''
        return;
    }

    newOpt.textContent = itemText.value;
    newOpt.value = itemValue.value;
    menu.appendChild(newOpt);
    itemText.value = '';
    itemValue.value = '';
}
