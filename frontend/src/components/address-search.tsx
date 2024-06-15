// an address search component that allows a user to input an address and postcode and return a result from the heat geek property info API

import React from "react";
import { useAppDispatch } from "../state/dispatch";
import { Button, Card, Input, Space } from "antd";
import { RootState } from "../state";
import { useSelector } from "react-redux";
import { addressSearchSlice } from "../state/address-search";
import { propertySlice } from "../state/property";
import { useLazyGetPropertyInfoQuery } from "../state/property-info-api";
import CurrentProperty from "./current-property";

const PostcodeSearch: React.FC = () => {
  const dispatch = useAppDispatch();
  const value = useSelector((r: RootState) => r.addressSearch.postcode);
  return (
    <Input
      placeholder="Postcode"
      onChange={(e) =>
        dispatch(addressSearchSlice.actions.setPostcode(e.target.value))
      }
      value={value}
    />
  );
};

const AddressLine1Search: React.FC = () => {
  const dispatch = useAppDispatch();
  const value = useSelector((r: RootState) => r.addressSearch.address);
  return (
    <Input
      value={value}
      placeholder="Address"
      onChange={(e) =>
        dispatch(addressSearchSlice.actions.setAddress(e.target.value))
      }
    />
  );
};

const SearchButton: React.FC = () => {
  const dispatch = useAppDispatch();
  const [query, result] = useLazyGetPropertyInfoQuery();
  const params = useSelector((r: RootState) => r.addressSearch);
  return (
    <>
      <Button
        block
        loading={result.isLoading}
        onClick={async () => {
          try {
            const res = await query(params);

            const data = res.data;

            if (!data) return;

            dispatch(propertySlice.actions.setPropertyInfo(data))
          } catch (e) {
            console.error(e);
          }
        }}
      >
        Search
      </Button>
    </>
  );
};

const AddressInputForm: React.FC = () => {
  return (
    <Card title="My Property">
      <Space direction="vertical" style={{ width: "100%" }}>
        <PostcodeSearch />
        <AddressLine1Search />
        <SearchButton />
        <CurrentProperty/>

      </Space>
    </Card>
  );
};

const AddressSearch: React.FC = () => {
  return (
    <>
      <AddressInputForm />
    </>
  );
};

export default AddressSearch;
