const { chromium } = require('playwright-chromium');
const { expect } = require('chai');

let browser, page;
describe('E2E tests', function () {
    this.timeout(6000);

    before(async () => {
        browser = await chromium.launch( {headless: false, slowMo: 500 });
    });

    after(async () => {
        await browser.close();
    });

    beforeEach(async () => {
        page = await browser.newPage();
    });

    afterEach(async () => {
        await page.close();
    });

    it('loads static page', async () => {
        await page.goto('http://localhost:3000');

        const content = await page.textContent('.accordion .head span');
        expect(content).to.contains('Scalable Vector Graphics');
    });

    it('toggles content', async () => {
        await page.goto('http://localhost:3000');

        await page.click('#main>.accordion:first-child >> text=More');

        await page.waitForSelector('#main>.accordion:first-child >> .extra p');

        const visible = await page.isVisible('#main>.accordion:first-child >> .extra p');
        expect(visible).to.be.true;
    });

    it('toggles content', async () => {
        await page.goto('http://localhost:3000');

        await page.click('#main>.accordion:first-child >> text=More');
        await page.waitForSelector('#main>.accordion:first-child >> .extra p');
        await page.click('#main>.accordion:first-child >> text=Less');

        const visible = await page.isVisible('#main>.accordion:first-child >> .extra p');
        expect(visible).to.be.false;
    });
});