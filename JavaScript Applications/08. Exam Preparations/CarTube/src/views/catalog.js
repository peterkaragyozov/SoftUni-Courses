import { html } from '../../node_modules/lit-html/lit-html.js';

import { getAllListings, getCollectionSize } from '../api/data.js';
import { carTemplate } from './common/car.js';

const catalogTemplate = (cars, page, pages) => html`
<section id="car-listings">
            <h1>Car Listings</h1>
            <div class="listings">
            
            <div>
            ${page > 1 ? html`<a class="button-list" href="/all-listings?page=${page - 1}"> &lt;  </a>` : ''}
            Page ${page} / ${pages} 
            ${page < pages ? html`<a class="button-list" href="/all-listings?page=${page + 1}"> &gt; </a>` : ''}
            </div>

               ${cars.length == 0 ? html`<p class="no-cars">No cars in database.</p>` : cars.map(carTemplate)}

            <div>
            ${page > 1 ? html`<a class="button-list" href="/all-listings?page=${page - 1}">&lt; Previous </a>` : ''}
            Page ${page} / ${pages} 
            ${page < pages ? html`<a class="button-list" href="/all-listings?page=${page + 1}">Next &gt; </a>` : ''}
            </div>
                
            </div>
        </section>`;

export async function catalogPage(ctx) {
    const page = Number(ctx.querystring.split('=')[1]) || 1;
    const count = await getCollectionSize();
    const pages = Math.ceil(count / 6);
    const cars = await getAllListings(page);
    ctx.render(catalogTemplate(cars, page, pages));
}