import { configureStore } from '@reduxjs/toolkit'
import { propertySlice } from './property'
import { propertyInfoApi } from './property-info-api'
import { addressSearchSlice } from './address-search'
import { useSelector } from 'react-redux'

export const store = configureStore({
  reducer: {
    addressSearch: addressSearchSlice.reducer,
    property: propertySlice.reducer,
    propertyInfoApi: propertyInfoApi.reducer,
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware().concat(propertyInfoApi.middleware),
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

