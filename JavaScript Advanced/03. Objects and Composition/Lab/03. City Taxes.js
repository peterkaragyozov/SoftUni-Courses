function cityTaxes(name, population, treasury) {
    const city = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += this.population * this.taxRate;
        },
        applyGrowth(percent) {
            this.population += Math.floor(this.population * percent / 100);
        },
        applyRecession(percent) {
            this.treasury -= Math.ceil(this.treasury * percent / 100);
        },
    };

    return city
}

const result = cityTaxes('Tortuga', 7000, 15000);
console.log(result);

result.taxRate = 15;
result.collectTaxes();
console.log(result);
