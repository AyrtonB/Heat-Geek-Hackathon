import { configureStore } from '@reduxjs/toolkit'
import { heatpumpSlice } from './property'
import { apiSlice } from './api'
import { addressSearchSlice } from './address-search'
import { useSelector } from 'react-redux'

export const store = configureStore({
  reducer: {
    addressSearch: addressSearchSlice.reducer,
    property: heatpumpSlice.reducer,
    api: apiSlice.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(apiSlice.middleware),
})

// Infer the `RootState` and `AppDispatch` types from the store itself
export type RootState = ReturnType<typeof store.getState>
// Inferred type: {posts: PostsState, comments: CommentsState, users: UsersState}
export type AppDispatch = typeof store.dispatch

export type UseAppSelector = (
  selector: (state: RootState) => unknown
) => unknown;

// export use selector for the app
export const useAppSelector: UseAppSelector = (selector) =>
  useSelector((state: RootState) => selector(state));

