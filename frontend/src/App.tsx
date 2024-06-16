import { Layout, Space } from 'antd'
import React from 'react'
import AddressSearch from './components/address-search';
import AnnualSavingsCard from './components/annual-savings';

const App:React.FC = () => {
  return (
    <Layout>
      <Space direction='vertical' style={{ padding: 24 }}>
        <AddressSearch />
        <AnnualSavingsCard/>
      </Space>
    </Layout>
  )
}

export default App;