/*
create universal request module (api.js)
create application-specific requests (data.js)
setup routing (page)
create context decorator middleware (utility functions)
implement views
*/

import { render } from '../node_modules/lit-html/lit-html.js';
import page from '../node_modules/page/page.mjs';

import { logout as apiLogout } from './api/data.js';
import { getUserData } from './utility.js';

import { loginPage, registerPage } from './views/auth.js';
import { homePage } from './views/home.js';
import { catalogPage } from './views/catalog.js';
import { detailsPage } from './views/details.js';
import { createPage } from './views/create.js';
import { editPage } from './views/edit.js';
import { searchPage } from './views/search.js';


const main = document.getElementById('main-content');
document.getElementById('logoutBtn').addEventListener('click', logout);

setUserNav();


page('/login', decorateContext, loginPage);
page('/register', decorateContext, registerPage);
page('/', decorateContext, homePage);
page('/catalog', decorateContext, catalogPage);
page('/details/:id', decorateContext, detailsPage);
page('/create', decorateContext, createPage);
page('/edit/:id', decorateContext, editPage);
page('/search', decorateContext, searchPage);


page.start();


function decorateContext(ctx, next) {
    ctx.render = (context) => render(context, main);
    ctx.setUserNav = setUserNav;
    ctx.user = getUserData();

    next();
}

function setUserNav() {
    const user = getUserData();
    if (user) {
        document.getElementById('user').style.display = 'block';
        document.getElementById('guest').style.display = 'none';
    } else {
        document.getElementById('user').style.display = 'none';
        document.getElementById('guest').style.display = 'block';
    }
}

function logout() {
    apiLogout();
    setUserNav();
    page.redirect('/');
}