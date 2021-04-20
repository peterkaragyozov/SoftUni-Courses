import * as api from './api.js';

const host = 'http://localhost:3030';
api.settings.host = host;

export const login = api.login;
export const register = api.register;
export const logout = api.logout;


//Application-specific requests

//get all recent articles
export async function getAllRecentListings() {
    return await api.get(host + '/data/wiki?sortBy=_createdOn%20desc&distinct=category');
}

//get all articles
export async function getAllListings() {
    return await api.get(host + '/data/wiki?sortBy=_createdOn%20desc');
}

//get article by id
export async function getListingById(id) {
    return await api.get(host + '/data/wiki/' + id);
}

//create article
export async function createListing(listing) {
    return await api.post(host + '/data/wiki', listing);
}

//edit article by id
export async function updateListing(id, listing) {
    return await api.put(host + '/data/wiki/' + id, listing);
}

//delete article by id
export async function deleteListing(id) {
    return await api.del(host + '/data/wiki/' + id);
}

export async function search(query) {
    return await api.get(host + `/data/wiki?where=title%20LIKE%20%22${query}%22`)
}
