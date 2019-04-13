var picker = new Pikaday({
    field: document.getElementById('datepicker'),
    format: 'DD.MM.YYYY',
    toString(date, format) {
        const day = date.getDate();
        const month = date.getMonth() + 1;
        const year = date.getFullYear();
        return `${day}.${month}.${year}`;
    }
});