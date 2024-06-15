import { createSlice } from '@reduxjs/toolkit'

type AddressSearchState = {
    postcode: string
    address: string
}

const initialState: AddressSearchState = {
    postcode: 'pl20 6rt',
    address: '35 bellever close'
}

export const addressSearchSlice = createSlice({
    name: 'addressSearch',
    initialState,
    reducers: {
        setPostcode: (state, action) => {
            state.postcode = action.payload
        },
        setAddress: (state, action) => {
            state.address = action.payload
        }
    }
})