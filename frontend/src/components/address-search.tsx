// an address search component that allows a user to input an address and postcode and return a result from the heat geek property info API

import React from "react";
import { useAppDispatch } from "../state/dispatch";
import { Button, Card, Form, Input, Space } from "antd";
import { RootState } from "../state";
import { useSelector } from "react-redux";
import { addressSearchSlice } from "../state/address-search";
import { heatpumpSlice } from "../state/heatpump";
import { useLazyGetHeatGeekAddressLookupQuery } from "../state/api";
import CurrentProperty from "./current-property";

const PostcodeSearch: React.FC = () => {
  const dispatch = useAppDispatch();
  const value = useSelector((r: RootState) => r.addressSearch.postcode);
  return (
   <Form.Item label='Postcode'>
     <Input
      placeholder="Postcode"
      onChange={(e) =>
        dispatch(addressSearchSlice.actions.setPostcode(e.target.value))
      }
      value={value}
    />
    </Form.Item>
  );
};

const AddressLine1Search: React.FC = () => {
  const dispatch = useAppDispatch();
  const value = useSelector((r: RootState) => r.addressSearch.address);
  return (
    <Form.Item label='Address'>
    <Input
      value={value}
      placeholder="Address"
      onChange={(e) =>
        dispatch(addressSearchSlice.actions.setAddress(e.target.value))
      }
    />
    </Form.Item>
  );
};

const SearchButton: React.FC = () => {
  const dispatch = useAppDispatch();
  const [query, result] = useLazyGetHeatGeekAddressLookupQuery();
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

            dispatch(heatpumpSlice.actions.setAddressLookup(data))
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
