import * as api from './api.js';

const host = 'http://localhost:3030';
api.settings.host = host;

export const login = api.login;
export const register = api.register;
export const logout = api.logout;

//Application-specific requests

//get all listings
export async function getAllListings() {
    return await api.get(host + '/data/pets?sortBy=_createdOn%20desc');
}

//get listing by id
export async function getListingById(id) {
    return await api.get(host + '/data/pets/' + id);
}

//create listing
export async function createListing(listing) {
    return await api.post(host + '/data/pets', listing);
}

//edit listing by id
export async function editListing(id, listing) {
    return await api.put(host + '/data/pets/' + id, listing);
}

//delete listing by id
export async function deleteListing(id) {
    return await api.del(host + '/data/pets/' + id);
}

//get my listings
export async function getMyListings(userId) {
    return await api.get(host + `/data/pets?where=_ownerId%3D%22${userId}%22&sortBy=_createdOn%20desc`);
}

//get likes
export async function getLikes(petId, userId) {
    return await api.get(host + `/data/likes?where=petId%3D%22${petId}%22%20and%20_ownerId%3D%22${userId}%22&count`);
}

//get total likes
export async function getTotalLikes(petId) {
    return await api.get(host + `/data/likes?where=petId%3D%22${petId}%22&distinct=_ownerId&count`);
}

//post likes
export async function postLikes(like) {
    return await api.post(host + `/data/likes`, like);
}