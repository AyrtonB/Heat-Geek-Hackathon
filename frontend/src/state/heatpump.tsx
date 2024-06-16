import { PayloadAction, createSlice } from "@reduxjs/toolkit";
import { HeatgeekAddressLookupResult } from "./api";

type HeatPumpState = {
   scopIndex: number
   addressLookup?: HeatgeekAddressLookupResult
}

const initialState: HeatPumpState = {
    scopIndex: 0
}

export const heatpumpSlice = createSlice({
    name: "heatpump",
    reducers: {
        setAddressLookup: (state, action: PayloadAction<HeatgeekAddressLookupResult>) => {
            state.addressLookup = action.payload
        },
        setScopIndex: (state, action: PayloadAction<number>) => {
            state.scopIndex = action.payload
        }
    },
    initialState
})